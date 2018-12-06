from __future__ import unicode_literals
from canvas_sdk import client, utils

def get_kaltura_config(request_ctx, **request_kwargs):
    """
    Return the config information for the Kaltura plugin in json format.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Get Kaltura config
        :rtype: requests.Response (with void data)

    """

    path = '/v1/services/kaltura'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def start_kaltura_session(request_ctx, **request_kwargs):
    """
    Start a new Kaltura session, so that new media can be recorded and uploaded
    to this Canvas instance's Kaltura instance.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Start Kaltura session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/services/kaltura_session'
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, **request_kwargs)

    return response


