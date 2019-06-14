from canvas_sdk import client, utils

def list_accounts(request_ctx, per_page=None, as_user_id=None, **request_kwargs):
    """
    List accounts that the current user can view or manage.  Typically,
    students and even teachers will get an empty list in response, only
    account admins can view the accounts that they are in.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :param as_user_id: (optional) Masquerade as the given canvas user
        :type as_user_id: integer or None
        :return: List accounts
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts'
    payload = {
        'per_page': per_page,
    }
    if as_user_id:
        payload['as_user_id'] = as_user_id
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_sub_accounts_of_account(request_ctx, account_id, recursive=None, per_page=None, as_user_id=None, **request_kwargs):
    """
    List accounts that are sub-accounts of the given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param recursive: (optional) If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false.
        :type recursive: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get the sub-accounts of an account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/sub_accounts'
    payload = {
        'recursive': recursive,
        'per_page': per_page,
    }
    if as_user_id:
        payload['as_user_id'] = as_user_id
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response
