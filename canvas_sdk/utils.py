from canvas_sdk import client

"""
The util module contains helper methods for the SDK
"""


def validate_attr_is_acceptable(value, acceptable_values=[], allow_none=True):
    """
    Test an input value against a list of acceptable values.  A value of None may or may
    not be considered valid.  If the input is not valid, an Attribute error is raised, otherwise
    nothing is returned.
    """
    if value not in acceptable_values:
        # We know the value is not one of the acceptable values, but we need to also make sure
        # that the value is not None and that None is not an allowable value before raising
        # an exception
        if value is not None or not allow_none:
            raise AttributeError("%s must be one of %s" % (value, acceptable_values))


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
    that exception will be bubbled back to the caller and any intermediary results will be lost.

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
