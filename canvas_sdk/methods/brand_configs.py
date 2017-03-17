from canvas_sdk import client, utils


def get_brand_config_variables_that_should_be_used_for_this_domain(request_ctx, **request_kwargs):
    """
    Will redirect to a static json file that has all of the brand
    variables used by this account. Even though this is a redirect,
    do not store the redirected url since if the account makes any changes
    it will redirect to a new url. Needs no authentication.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Get the brand config variables that should be used for this domain
        :rtype: requests.Response (with void data)

    """

    path = '/v1/brand_variables'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


