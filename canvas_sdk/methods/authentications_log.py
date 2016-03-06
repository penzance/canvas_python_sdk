from canvas_sdk import client, utils


def query_by_login(request_ctx, login_id, start_time=None, end_time=None, **request_kwargs):
    """
    List authentication events for a given login.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param login_id: (required) ID
        :type login_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: DateTime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: DateTime or None
        :return: Query by login.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/audit/authentication/logins/{login_id}'
    payload = {
        'start_time': start_time,
        'end_time': end_time,
    }
    url = request_ctx.base_api_url + path.format(login_id=login_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def query_by_account(request_ctx, account_id, start_time=None, end_time=None, **request_kwargs):
    """
    List authentication events for a given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: DateTime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: DateTime or None
        :return: Query by account.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/audit/authentication/accounts/{account_id}'
    payload = {
        'start_time': start_time,
        'end_time': end_time,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def query_by_user(request_ctx, user_id, start_time=None, end_time=None, **request_kwargs):
    """
    List authentication events for a given user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: DateTime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: DateTime or None
        :return: Query by user.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/audit/authentication/users/{user_id}'
    payload = {
        'start_time': start_time,
        'end_time': end_time,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


