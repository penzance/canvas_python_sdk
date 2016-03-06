from canvas_sdk import client, utils


def list_available_tabs_for_course_or_group_courses(request_ctx, course_id, include=None, per_page=None, **request_kwargs):
    """
    Returns a list of navigation tabs available in the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) Optionally include external tool tabs in the returned list of tabs
(Only has effect for courses, not groups)
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List available tabs for a course or group
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('external')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/tabs'
    payload = {
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_available_tabs_for_course_or_group_groups(request_ctx, group_id, include=None, per_page=None, **request_kwargs):
    """
    Returns a list of navigation tabs available in the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param include: (optional) Optionally include external tool tabs in the returned list of tabs
(Only has effect for courses, not groups)
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List available tabs for a course or group
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('external')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/groups/{group_id}/tabs'
    payload = {
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_tab_for_course(request_ctx, course_id, tab_id, position=None, hidden=None, **request_kwargs):
    """
    Home and Settings tabs are not manageable, and can't be hidden or moved
    
    Returns a tab object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param tab_id: (required) ID
        :type tab_id: string
        :param position: (optional) The new position of the tab, 1-based
        :type position: integer or None
        :param hidden: (optional) no description
        :type hidden: boolean or None
        :return: Update a tab for a course
        :rtype: requests.Response (with Tab data)

    """

    path = '/v1/courses/{course_id}/tabs/{tab_id}'
    payload = {
        'position': position,
        'hidden': hidden,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, tab_id=tab_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


