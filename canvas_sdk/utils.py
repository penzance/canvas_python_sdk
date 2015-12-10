from canvas_sdk import client
from collections import defaultdict

"""
The util module contains helper methods for the SDK
"""


def validate_attr_is_acceptable(value, acceptable_values=[], allow_none=True):
    """
    Test an input value against a list of acceptable values.  A value of None may or may
    not be considered valid.  If the input is not valid, an Attribute error is raised, otherwise
    nothing is returned.
    """
    if type(value) not in (list, tuple):
        value = [value]
    for v in value:
        if v not in acceptable_values:
            # We know the value is not one of the acceptable values, but we need to also make sure
            # that the value is not None and that None is not an allowable value before raising
            # an exception
            if v is not None or not allow_none:
                raise AttributeError("%s must be one of %s" % (v, acceptable_values))


# todo: unit test
def validate_any(param_choices, *args, **kwargs):
    """
    If all of the arguments are None or blank strings, an Attribute error is
    raised (configurable with accept_blank kwarg), otherwise nothing is returned
    """
    accept_blank = kwargs.pop('accept_blank', False)
    args_to_check = args
    if not accept_blank:
        args_to_check = [a for a in args if a and a != '']
    if not any(args_to_check):
        raise AttributeError(
            "One of the following parameters must be included: "
            "%s" % param_choices)


def get_next(request_context, response):
    """
    Generator function that will iterate over a given response's "next" header links.

        :param :class:RequestContext request_context: The context required to make a "get" request
        :return: next response object retrieved by client
        :rtype: iterator
    """
    while 'next' in response.links:
        response = client.get(request_context, response.links["next"]["url"])
        yield response


def get_all_list_data(request_context, function, *args, **kwargs):
    """
    Make a function request with args and kwargs and iterate over the "next" responses until exhausted.
    Return initial response json data or all json data as a single list.  Responses that have a series of
    next responses (as retrieved by get_next generator) are expected to have data returned as a list.
    If an exception is raised during the initial function call or in the process of paging over results,
    that exception will be bubbled back to the caller and any intermediary results will be lost.  Worst case
    complexity O(n).


        :param RequestContext request_context: The context required to make an API call
        :param function function: The API function to call
        :return: A list of all json data retrieved while iterating over response links, or the initial json
            function response if there are no paged results
        :rtype: list of json data or json
    """
    response = function(request_context, *args, **kwargs)
    data = response.json()
    for next_response in get_next(request_context, response):
        data.extend(next_response.json())
    return data


def masquerade(request_context, function, as_user_id, *args, **kwargs):
    """
    Make a function request on behalf of another user.  In order to masquerade, the calling user must
    have the "Become other users" permission in Canvas. If the target user is also an admin, the
    calling user must additionally have every permission that the target user has.

        :param function function: The API function to call
        :param str as_user_id: The Canvas user ID or an SIS user ID (SIS IDs are described at
            https://canvas.instructure.com/doc/api/file.object_ids.html)
        :return: Response from function call
    """
    function_kwargs = defaultdict(dict, **kwargs)
    # Merge or create as_user_id into params kwarg - use defaultdict to reduce conditional logic
    function_kwargs['params'].update(as_user_id=as_user_id)
    return function(request_context, *args, **function_kwargs)


def get_count(request_context, function, *args, **kwargs):
    """
    Make a function request with args and kwargs and return the total result count.  Worst case complexity
    is O(n).

        :param RequestContext request_context: The context required to make an API call
        :param function function: The API function to call
        :return: Total result count
        :rtype: int
    """
    return len(get_all_list_data(request_context, function, *args, **kwargs))
