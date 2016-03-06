from canvas_sdk import client, utils


def create_enrollment_term(request_ctx, account_id, enrollment_term_name=None, enrollment_term_start_at=None, enrollment_term_end_at=None, enrollment_term_sis_term_id=None, **request_kwargs):
    """
    Create a new enrollment term for the specified account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param enrollment_term_name: (optional) The name of the term.
        :type enrollment_term_name: string or None
        :param enrollment_term_start_at: (optional) The day/time the term starts.
Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :type enrollment_term_start_at: DateTime or None
        :param enrollment_term_end_at: (optional) The day/time the term ends.
Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :type enrollment_term_end_at: DateTime or None
        :param enrollment_term_sis_term_id: (optional) The unique SIS identifier for the term.
        :type enrollment_term_sis_term_id: string or None
        :return: Create enrollment term
        :rtype: requests.Response (with EnrollmentTerm data)

    """

    path = '/v1/accounts/{account_id}/terms'
    payload = {
        'enrollment_term[name]': enrollment_term_name,
        'enrollment_term[start_at]': enrollment_term_start_at,
        'enrollment_term[end_at]': enrollment_term_end_at,
        'enrollment_term[sis_term_id]': enrollment_term_sis_term_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_enrollment_term(request_ctx, account_id, id, enrollment_term_name=None, enrollment_term_start_at=None, enrollment_term_end_at=None, enrollment_term_sis_term_id=None, **request_kwargs):
    """
    Update an existing enrollment term for the specified account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param enrollment_term_name: (optional) The name of the term.
        :type enrollment_term_name: string or None
        :param enrollment_term_start_at: (optional) The day/time the term starts.
Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :type enrollment_term_start_at: DateTime or None
        :param enrollment_term_end_at: (optional) The day/time the term ends.
Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        :type enrollment_term_end_at: DateTime or None
        :param enrollment_term_sis_term_id: (optional) The unique SIS identifier for the term.
        :type enrollment_term_sis_term_id: string or None
        :return: Update enrollment term
        :rtype: requests.Response (with EnrollmentTerm data)

    """

    path = '/v1/accounts/{account_id}/terms/{id}'
    payload = {
        'enrollment_term[name]': enrollment_term_name,
        'enrollment_term[start_at]': enrollment_term_start_at,
        'enrollment_term[end_at]': enrollment_term_end_at,
        'enrollment_term[sis_term_id]': enrollment_term_sis_term_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_enrollment_term(request_ctx, account_id, id, **request_kwargs):
    """
    Delete the specified enrollment term.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete enrollment term
        :rtype: requests.Response (with EnrollmentTerm data)

    """

    path = '/v1/accounts/{account_id}/terms/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_enrollment_terms(request_ctx, account_id, workflow_state=None, per_page=None, **request_kwargs):
    """
    Return all of the terms in the account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param workflow_state: (optional) If set, only returns terms that are in the given state.
Defaults to 'active'.
        :type workflow_state: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enrollment terms
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    workflow_state_types = ('active', 'deleted', 'all')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/accounts/{account_id}/terms'
    payload = {
        'workflow_state': workflow_state,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


