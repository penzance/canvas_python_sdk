from canvas_sdk import client, utils

def list_enrollment_terms(request_ctx, account_id, workflow_state=None, per_page=None, **request_kwargs):
    """
    Return all of the terms in the account. Account must be a root account and
    requires permission to manage the account (when called on non-root
    accounts, will be directed to the appropriate root account).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param workflow_state: (optional) no description
        :type workflow_state: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enrollment terms
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/terms'
    payload = {
        'workflow_state' : workflow_state,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


