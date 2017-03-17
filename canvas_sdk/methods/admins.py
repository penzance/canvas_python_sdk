from canvas_sdk import client, utils


def make_account_admin(request_ctx, account_id, user_id, role=None, role_id=None, send_confirmation=None, **request_kwargs):
    """
    Flag an existing user as an admin within the account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (required) The id of the user to promote.
        :type user_id: integer
        :param role: (optional) (deprecated)
The user's admin relationship with the account will be created with the
given role. Defaults to 'AccountAdmin'.
        :type role: string or None
        :param role_id: (optional) The user's admin relationship with the account will be created with the
given role. Defaults to the built-in role for 'AccountAdmin'.
        :type role_id: integer or None
        :param send_confirmation: (optional) Send a notification email to
the new admin if true. Default is true.
        :type send_confirmation: boolean or None
        :return: Make an account admin
        :rtype: requests.Response (with Admin data)

    """

    path = '/v1/accounts/{account_id}/admins'
    payload = {
        'user_id': user_id,
        'role': role,
        'role_id': role_id,
        'send_confirmation': send_confirmation,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_account_admin(request_ctx, account_id, user_id, role=None, role_id=None, **request_kwargs):
    """
    Remove the rights associated with an account admin role from a user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param role: (optional) (Deprecated)
Account role to remove from the user. Defaults to 'AccountAdmin'. Any
other account role must be specified explicitly.
        :type role: string or None
        :param role_id: (optional) The user's admin relationship with the account will be created with the
given role. Defaults to the built-in role for 'AccountAdmin'.
        :type role_id: integer or None
        :return: Remove account admin
        :rtype: requests.Response (with Admin data)

    """

    path = '/v1/accounts/{account_id}/admins/{user_id}'
    payload = {
        'role': role,
        'role_id': role_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, user_id=user_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_account_admins(request_ctx, account_id, user_id=None, per_page=None, **request_kwargs):
    """
    List the admins in the account

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (optional) Scope the results to those with user IDs equal to any of the IDs specified here.
        :type user_id: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List account admins
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/admins'
    payload = {
        'user_id[]': user_id,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


