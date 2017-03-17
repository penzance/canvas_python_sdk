from canvas_sdk import client, utils


def create_new_grading_standard_accounts(request_ctx, account_id, title, grading_scheme_entry_name, grading_scheme_entry_value, **request_kwargs):
    """
    Create a new grading standard
    
    If grading_scheme_entry arguments are omitted, then a default grading scheme
    will be set. The default scheme is as follows:
         "A" : 94,
         "A-" : 90,
         "B+" : 87,
         "B" : 84,
         "B-" : 80,
         "C+" : 77,
         "C" : 74,
         "C-" : 70,
         "D+" : 67,
         "D" : 64,
         "D-" : 61,
         "F" : 0,

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param title: (required) The title for the Grading Standard.
        :type title: string
        :param grading_scheme_entry_name: (required) The name for an entry value within a GradingStandard that describes the range of the value
e.g. A-
        :type grading_scheme_entry_name: array
        :param grading_scheme_entry_value: (required) The value for the name of the entry within a GradingStandard.
The entry represents the lower bound of the range for the entry.
This range includes the value up to the next entry in the GradingStandard,
or 100 if there is no upper bound. The lowest value will have a lower bound range of 0.
e.g. 93
        :type grading_scheme_entry_value: array
        :return: Create a new grading standard
        :rtype: requests.Response (with GradingStandard data)

    """

    path = '/v1/accounts/{account_id}/grading_standards'
    payload = {
        'title': title,
        'grading_scheme_entry[name][]': grading_scheme_entry_name,
        'grading_scheme_entry[value][]': grading_scheme_entry_value,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_grading_standard_courses(request_ctx, course_id, title, grading_scheme_entry_name, grading_scheme_entry_value, **request_kwargs):
    """
    Create a new grading standard
    
    If grading_scheme_entry arguments are omitted, then a default grading scheme
    will be set. The default scheme is as follows:
         "A" : 94,
         "A-" : 90,
         "B+" : 87,
         "B" : 84,
         "B-" : 80,
         "C+" : 77,
         "C" : 74,
         "C-" : 70,
         "D+" : 67,
         "D" : 64,
         "D-" : 61,
         "F" : 0,

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param title: (required) The title for the Grading Standard.
        :type title: string
        :param grading_scheme_entry_name: (required) The name for an entry value within a GradingStandard that describes the range of the value
e.g. A-
        :type grading_scheme_entry_name: array
        :param grading_scheme_entry_value: (required) The value for the name of the entry within a GradingStandard.
The entry represents the lower bound of the range for the entry.
This range includes the value up to the next entry in the GradingStandard,
or 100 if there is no upper bound. The lowest value will have a lower bound range of 0.
e.g. 93
        :type grading_scheme_entry_value: array
        :return: Create a new grading standard
        :rtype: requests.Response (with GradingStandard data)

    """

    path = '/v1/courses/{course_id}/grading_standards'
    payload = {
        'title': title,
        'grading_scheme_entry[name][]': grading_scheme_entry_name,
        'grading_scheme_entry[value][]': grading_scheme_entry_value,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_grading_standards_available_in_context_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of grading standards in the given context that are visible to user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the grading standards available in a context.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/grading_standards'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_grading_standards_available_in_context_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the list of grading standards in the given context that are visible to user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the grading standards available in a context.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/grading_standards'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


