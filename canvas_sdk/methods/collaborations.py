from canvas_sdk import client, utils

def list_members_of_collaboration(request_ctx, id, per_page=None, **request_kwargs):
    """
    Examples
    
      curl https://<canvas>/api/v1/courses/1/collaborations/1/members

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List members of a collaboration.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/collaborations/{id}/members'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


