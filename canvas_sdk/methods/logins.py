from canvas_sdk import client, utils

def list_user_logins_accounts(request_ctx, account_id, **request_kwargs):
    """
    Given a user ID, return that user's logins for the given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: List user logins
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/logins'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_user_logins_users(request_ctx, user_id, **request_kwargs):
    """
    Given a user ID, return that user's logins for the given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :return: List user logins
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/logins'
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_user_login(request_ctx, account_id, user_id, login_unique_id, login_password=None, login_sis_user_id=None, **request_kwargs):
    """
    Create a new login for an existing user in the given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (required) The ID of the user to create the login for.
        :type user_id: string
        :param login_unique_id: (required) The unique ID for the new login.
        :type login_unique_id: string
        :param login_password: (optional) The new login's password.
        :type login_password: string or None
        :param login_sis_user_id: (optional) SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        :type login_sis_user_id: string or None
        :return: Create a user login
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/logins'
    payload = {
        'user[id]' : user_id,
        'login[unique_id]' : login_unique_id,
        'login[password]' : login_password,
        'login[sis_user_id]' : login_sis_user_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_user_login(request_ctx, account_id, id, login_unique_id=None, login_password=None, login_sis_user_id=None, **request_kwargs):
    """
    Update an existing login for a user in the given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param login_unique_id: (optional) The new unique ID for the login.
        :type login_unique_id: string or None
        :param login_password: (optional) The new password for the login. Can only be set by an admin user if admins are allowed to change passwords for the account.
        :type login_password: string or None
        :param login_sis_user_id: (optional) SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        :type login_sis_user_id: string or None
        :return: Edit a user login
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/logins/{id}'
    payload = {
        'login[unique_id]' : login_unique_id,
        'login[password]' : login_password,
        'login[sis_user_id]' : login_sis_user_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_user_login(request_ctx, user_id, id, **request_kwargs):
    """
    Delete an existing login.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a user login
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/logins/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


