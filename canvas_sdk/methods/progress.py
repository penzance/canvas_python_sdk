from canvas_sdk import client, utils

def query_progress(request_ctx, id, **request_kwargs):
    """
    Return completion and status information about an asynchronous job

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Query progress
        :rtype: requests.Response (with Progress data)

    """

    path = '/v1/progress/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


