from canvas_sdk import client, utils

def search_account_domains(request_ctx, name=None, domain=None, latitude=None, longitude=None, **request_kwargs):
    """
    Returns a list of up to 5 matching account domains
    
    Partial match on name / domain are supported

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param name: (optional) campus name
        :type name: string or None
        :param domain: (optional) no description
        :type domain: string or None
        :param latitude: (optional) no description
        :type latitude: string or None
        :param longitude: (optional) no description
        :type longitude: string or None
        :return: 
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/search'
    payload = {
        'name' : name,
        'domain' : domain,
        'latitude' : latitude,
        'longitude' : longitude,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


