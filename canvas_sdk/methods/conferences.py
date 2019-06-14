from canvas_sdk import client, utils

def list_conferences_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Retrieve the list of conferences for this context
    
    This API returns a JSON object containing the list of conferences,
    the key for the list of conferences is "conferences"
    
     Examples:
        curl 'https://<canvas>/api/v1/courses/<course_id>/conferences' \
            -H "Authorization: Bearer <token>"
    
        curl 'https://<canvas>/api/v1/groups/<group_id>/conferences' \
            -H "Authorization: Bearer <token>"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List conferences
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/conferences'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_conferences_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Retrieve the list of conferences for this context
    
    This API returns a JSON object containing the list of conferences,
    the key for the list of conferences is "conferences"
    
     Examples:
        curl 'https://<canvas>/api/v1/courses/<course_id>/conferences' \
            -H "Authorization: Bearer <token>"
    
        curl 'https://<canvas>/api/v1/groups/<group_id>/conferences' \
            -H "Authorization: Bearer <token>"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List conferences
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/conferences'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


