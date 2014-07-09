

import urllib2
import json
import re
import os
import sys
import errno
#import getopt
import argparse

"""
Constants for python indentation
"""
NONE = 0
FOUR = 4
EIGHT = 8
TWELVE = 12

"""
Current working directory
"""
BASE_DIR = os.path.dirname(os.getcwd())

"""
The script will create a new directory relative to the CWD called
/canvas_sdk/methods
"""
METHODS_DIR = BASE_DIR+'/canvas_sdk/methods'


def line_format(line, spacing):
    '''
    pad lines with preceding spaces to provide the indentation required 
    by python
    '''
    line_lenth = len(line) + spacing
    format_string = '{:>' + str(line_lenth) + '}'
    new_line = format_string.format(line)
    new_line += '\n'
    return new_line


def format_field_name(field_name):
    """
    format_field_name creates an entry for a dictionary with the field_name 
    being the key and the value being the variable named field_name
    Ex: 
        sometext[thefieldname] becomes
        'thefieldname' = sometext_thefieldname,

        The canvas api has form fields with the same name as non form fields
        so it is necessary to preappend the dict name
    
        thefield becomes
        'thefield' = thefield

    """
    fieldmatch = re.search(r'(\w+)\[(\w+)\]', field_name)
    line = ''
    if fieldmatch:
        field = fieldmatch.group(1) + '_' + fieldmatch.group(2)
        line = "'{0}' : {1},".format(field_name.strip(), field.strip())
    else:
        line = "'{0}' : {1},".format(field_name.strip(), field_name.strip())

    return line


def build_payload(parameters):
    """
    build_payload creates a list of parameters to be used in the payload of 
    the api call
    """
    payload = []
    for param in parameters:
        if param['paramType'] not in 'path':
            field_name = param['name']
            payload.append(format_field_name(field_name))

    return payload


def format_parameter(param, required):
    """
    format_parameter build the a parameter to be used in the paramter list 
    of the methods calls we are creating
    """

    param_match = re.search(r'(\w+)\[(\w+)\]', param)
    param_string = ''
    if param_match:
        param_string = param_match.group(1)+'_'+param_match.group(2)
    else:
        param_string = param
    
    """
    Some parameters have brackets around them like [param],
    we want to remove those here. they wont be caught by the check above.
    """

    param_match = re.search(r'\[(\w+)\]', param_string) 
    if param_match:
        param_string = param_match.group(1)

    if not required:
        param_string += '=None'

    return param_string


def get_parameters(parameters):
    """
    get paramters creates the parameter list for the method call
    """
    
    arg_list = []
    opt_list = []
    for param in parameters:
        param_name = param['name']
        param_required = param['required']
        if param_required:
            arg_list.append(format_parameter(param_name, param_required))
        else:
            opt_list.append(format_parameter(param_name, param_required))

    return arg_list + opt_list

def get_parameter_descriptions(parameters):
    """
    get paramters creates the parameter list for the method calls in rst format
    """

    lines = []
    opt_lines = []
    for param in parameters:
        param_match = re.search(r'(\w+)\[(\w+)\]', param['name'])
        if param_match:
            param_name = param_match.group(1) + '_' + param_match.group(2)
        else:
            param_name = param['name']

        if param['required']:
            required = 'required'
            lines.append(':param {0}: ({1}) {2}'.format(param_name, required, 
                param['description']))
            lines.append(':type {0}: {1}'.format(param_name, param['type']))
        else:
            required = 'optional'
            opt_lines.append(':param {0}: ({1}) {2}'.format(param_name, 
                required, param['description']))
            opt_lines.append(':type {0}: {1} or None'.format(param_name, 
                param['type']))

    return lines + opt_lines


def get_path_parameters(parameters):
    """
    get paramters creates the parameter list for the method call
    """
    
    arg_list = []
    for param in parameters:
        if param['paramType'] == 'path':
            param_name = param['name']
            arg_list.append('{0}={1}'.format(param_name, param_name))

    return arg_list


def get_param_name(param):
    """
    extract the param name from a form parameter. 
    Ex.  'course[name]' will return 'name'
    """
    
    match_name = re.search(r'\[(\w+)\]', param)
    if match_name:
        return match_name.group(1)
    else:
        return param


def check_for_enums(parameters):
    """
    Check for the existance of enums in the parameter list. 
    If an enum exists, we need to build a tuple of the emum names
    as well as the code that will validate the the enum. We create
    two lists one that has the enums as tuples and another that has
    the valdiate code. The method returns a list that consistes of these
    two lists joined. 
    """
    
    enum_line = ''
    enum_lines = []
    validate_enums = []
    for param in parameters:
        if 'enum' in param:
            param_name = get_param_name(param['name'])
            param_enum = param['enum']
            enum_line = param_name + '_types = ('
            enums = ", ".join("'{0}'".format(p) for p in param_enum)
            enum_line += enums + ')'
            enum_lines.append(enum_line)
            validate_enums.append('utils.validate_attr_is_acceptable('+param_name+', ' +param_name+'_types)')
    return enum_lines + validate_enums


def build_method(method_name, description, parameters, api_path, http_method, summary, return_type):
    """
    build method is used build the methods of the class we are processing.
    """
    
    allow_per_page = False
    arg_list = get_parameters(parameters)
    param_descriptions = get_parameter_descriptions(parameters)
    payload = build_payload(parameters)
    enums = check_for_enums(parameters)

    """
    If the method returns an array, allow the per_page parameter for paging
    """
    if return_type == 'array':
        arg_list.append('per_page=None')
        param_descriptions.append(':param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE')
        param_descriptions.append(':type per_page: integer or None')
        payload.append('\'per_page\' : per_page,')
        allow_per_page = True
        
    arg_list.append('**request_kwargs')
    
    """
    Create the method signature
    """
    
    content = line_format('def ' + method_name + '(request_ctx, ' + ', '.join(arg_list) + '):', NONE)
    content += line_format('"""', FOUR)

    """
    Create the method description text from the description in the meta api
    """
    for line in description.splitlines(True):
        content += line_format(line.rstrip(), FOUR)
    
    """
    list out the method paramters
    """
    content += line_format('', NONE)
    content += line_format(':param request_ctx: The request context', EIGHT)
    content += line_format(':type request_ctx: :class:RequestContext', EIGHT)
    for param in param_descriptions:
        content += line_format(param, EIGHT)
    content += line_format(':return: '+summary, EIGHT)
    content += line_format(':rtype: requests.Response (with ' + return_type + ' data)', EIGHT)
    content += line_format('', NONE)
    content += line_format('"""', FOUR)
    content += line_format('', NONE)
    
    """
    build the per_page check
    """
    if allow_per_page:
        content += line_format('if per_page is None:', FOUR)
        content += line_format('per_page = request_ctx.per_page', EIGHT)

    """
    Add any enums if they exist
    """
    if enums: 
        for enum in enums:
            content += line_format(enum, FOUR)
    
    """
    Add the api path
    """
    path_formatted = 'path = \'' + api_path + '\''
    content += line_format(path_formatted, FOUR)
    
    """
    Add a payload if one exists
    """
    payload_string = ''
    if payload:
        content += line_format('payload = {', FOUR)
        for item in payload:
            content += line_format(item, EIGHT)
        content += line_format('}', FOUR)
        payload_string = ', payload=payload'

    content += line_format('url = request_ctx.base_api_url + path.format(' + ', '.join(get_path_parameters(parameters)) + ')', FOUR)
    content += line_format(
        'response = client.'+http_method.lower()+'(request_ctx, url' + payload_string + ', **request_kwargs)', FOUR)
    
    content += line_format('', NONE)
    content += line_format('return response', FOUR)
    content += line_format('', NONE)
    content += line_format('', NONE)
    return content


def build_module(json_api_url):
    """
    build class reads in the api call for a class and contructs a class object 
    to be written to a file.
    """
    resp = urllib2.urlopen(json_api_url)
    json_resp = json.load(resp)
    apis = json_resp['apis']

    content = line_format('from canvas_sdk import client, utils', NONE)
    content += line_format('', NONE)
    
    for item in apis:
        api_path = item['path']
        description = item['description']
        operations = item['operations'][0]
        method_name = operations['nickname']
        http_method = operations['method']
        parameters = operations['parameters']
        summary = operations['summary']
        return_type = operations['type']
        content += build_method(
            method_name, description, parameters, api_path, http_method, 
            summary, return_type)

    return content

def create_sdk_directories():
    """
    Create the canvas_sdk/methods directory if it doesn't already exist
    """
    try:
        os.makedirs(METHODS_DIR)
        init_file = METHODS_DIR+'/__init__.py'
        if not os.path.isfile(init_file):
            new_init_file = open(init_file, 'w')
            new_init_file.close()

    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def check_url(url_string):
    """
    Check if the url contains http or https
    """
    

def main(argv=None):
    """
    the main method of the script calls the url provided by the user via 
    command line arguments or a displays a usage message
    """
    if argv is None:
        argv = sys.argv
    
    parser = argparse.ArgumentParser(description='Build Canvas SDK methods')
    parser.add_argument('-u','--url', help='Base Canvas url, default is (https://canvas.instructure.com)')
    args = vars(parser.parse_args())

    """
    Default to instructure if no url is given
    """
    base_canvas_url = 'https://canvas.instructure.com'
    
    if 'url' in args:
        url = args['url']

    if 'u' in args:
        url = args['u']   
    
    if url:
        if 'http' not in url:
            print 'Error: invalid url [%s]' % url   
            return 2
        else:
            base_canvas_url = url
   
    try:
        response = urllib2.urlopen(base_canvas_url+'/doc/api/api-docs.json')
    except urllib2.HTTPError as err:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', err.code
        return 2
    except urllib2.URLError as err:
        print 'We failed to reach a server.'
        print 'Reason: ', err.reason
        return 2

    base_api_url = base_canvas_url+'/doc/api'

    json_data = json.load(response)
    create_sdk_directories()
    apis = json_data['apis']
    
    for api in apis:
        path = api['path']
        url = base_api_url + path
        match = re.match(r'\/(\w+)\.json', path)
        file_name = match.group(1)
        python_file_name = file_name + '.py'
        python_file = open(METHODS_DIR + '/' + python_file_name, 'w')
        print 'Creating '+METHODS_DIR + '/' + python_file_name + '...'
        python_file_content = build_module(url)
        python_file.write(python_file_content)
        python_file.close()


if __name__ == "__main__":
    sys.exit(main())

