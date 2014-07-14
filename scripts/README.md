##Autogenerate SDK Methods##


** USE AT YOUR OWN RISK - This script will overwrite existing files.**

The script will automatically generate python modules containing SDK methods from the Canvas LMS REST API. The Canvas LMS REST API provides a meta-api interface describing each of the methods in JSON format. See the links below for an example on the instructure site:

* [main api-docs page](https://canvas.instructure.com/doc/api/api-docs.json)
* [view the accounts.json page](https://canvas.instructure.com/doc/api/accounts.json) 
* This can also be viewed as [accounts.html](https://canvas.instructure.com/doc/api/accounts.html).

The script output will be python modules, the code below shows what the output looks like for the first
method of the sections module, *list_course_sections*.

```python
from canvas_sdk import client, utils

def list_course_sections(request_ctx, course_id, include=None, per_page=None, **request_kwargs):
    """
    Returns the list of sections for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) - "students": Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned.
        :type include: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List course sections
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('students', 'avatar_url')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/sections'
    payload = {
        'include' : include,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response

```


### Where to run the script ###

The script can be run from any directory. However, keep in mind that it will look for and create
if needed, a directory called "../canvas_sdk/methods" relative (note the up and over '..') to the location of the script. It is recommended that you run the script from the scripts directory.

```
canvas_sdk_project
        |
        └─--canvas_sdk
        |		└─methods (this directory will be created if needed by the script)
        |			|
        |			└─--accounts.py (these files will either be created or overwritten)
        |			└─--sections.py
        |			└─--...
        └─--scripts
        |		|
        |	    └─--generate_sdk_methods.py (run the script from here)
        ...
```

### Usage ###

usage: generate_sdk_methods.py [-h] [-u URL]

Build Canvas SDK methods

optional arguments:
    -h, --help         show this help message and exit
    -u URL, --url URL  Base Canvas url, default is (https://canvas.instructure.com)

If run with no arguments, the script will default to the instructure url https://canvas.instructure.com



### Examples ###

```
$ python generate_sdk_methods.py -h or --help ( print the help message )
```

```
$ python generate_sdk_methods.py -u https://canvas.instructure.com
```

creates the sdk methods from the base url canvas.instructure.com, if you run 
your own instance of canvas replace this url with yours.



