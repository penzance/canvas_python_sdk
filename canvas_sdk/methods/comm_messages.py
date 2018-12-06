from __future__ import unicode_literals
from canvas_sdk import client, utils

def list_of_commmessages_for_user(request_ctx, user_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    Retrieve messages sent to a user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) The user id for whom you want to retrieve CommMessages
        :type user_id: string
        :param start_time: (optional) The beginning of the time range you want to retrieve message from.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range you want to retrieve messages for.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List of CommMessages for a user
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/comm_messages'
    payload = {
        'user_id' : user_id,
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


