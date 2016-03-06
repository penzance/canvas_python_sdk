from canvas_sdk import client, utils


def create_jwt(request_ctx, **request_kwargs):
    """
    Create a unique jwt for using with other canvas services
    
    Generates a different JWT each time it's called, each one expires
    after a short window (1 hour)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Create JWT
        :rtype: requests.Response (with void data)

    """

    path = '/v1/jwts'
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, **request_kwargs)

    return response


