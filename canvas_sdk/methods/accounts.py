from canvas_sdk import client, utils

def list_accounts(request_ctx, per_page=None, **request_kwargs):
    """
    List accounts that the current user can view or manage.  Typically,
    students and even teachers will get an empty list in response, only
    account admins can view the accounts that they are in.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List accounts
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_account(request_ctx, id, **request_kwargs):
    """
    Retrieve information on an individual account, given by id or sis
    sis_account_id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get a single account
        :rtype: requests.Response (with Account data)

    """

    path = '/v1/accounts/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_sub_accounts_of_account(request_ctx, account_id, recursive=None, per_page=None, **request_kwargs):
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
        'recursive' : recursive,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_active_courses_in_account(request_ctx, account_id, with_enrollments=None, published=None, completed=None, by_teachers=None, by_subaccounts=None, hide_enrollmentless_courses=None, state=None, enrollment_term_id=None, search_term=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of courses in this account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param with_enrollments: (optional) If true, include only courses with at least one enrollment. If false, include only courses with no enrollments. If not present, do not filter on course enrollment status.
        :type with_enrollments: boolean or None
        :param published: (optional) If true, include only published courses. If false, exclude published courses. If not present, do not filter on published status.
        :type published: boolean or None
        :param completed: (optional) If true, include only completed courses (these may be in state 'completed', or their enrollment term may have ended). If false, exclude completed courses. If not present, do not filter on completed status.
        :type completed: boolean or None
        :param by_teachers: (optional) List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users.
        :type by_teachers: integer or None
        :param by_subaccounts: (optional) List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts.
        :type by_subaccounts: integer or None
        :param hide_enrollmentless_courses: (optional) If present, only return courses that have at least one enrollment. Equivalent to 'with_enrollments=true'; retained for compatibility.
        :type hide_enrollmentless_courses: boolean or None
        :param state: (optional) If set, only return courses that are in the given state(s). By default, all states but "deleted" are returned.
        :type state: string or None
        :param enrollment_term_id: (optional) If set, only includes courses from the specified term.
        :type enrollment_term_id: integer or None
        :param search_term: (optional) The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters.
        :type search_term: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List active courses in an account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('created', 'claimed', 'available', 'completed', 'deleted', 'all')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/accounts/{account_id}/courses'
    payload = {
        'with_enrollments' : with_enrollments,
        'published' : published,
        'completed' : completed,
        'by_teachers' : by_teachers,
        'by_subaccounts' : by_subaccounts,
        'hide_enrollmentless_courses' : hide_enrollmentless_courses,
        'state' : state,
        'enrollment_term_id' : enrollment_term_id,
        'search_term' : search_term,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_account(request_ctx, id, account_name=None, account_default_time_zone=None, account_default_storage_quota_mb=None, account_default_user_storage_quota_mb=None, account_default_group_storage_quota_mb=None, **request_kwargs):
    """
    Update an existing account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param account_name: (optional) Updates the account name
        :type account_name: string or None
        :param account_default_time_zone: (optional) The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type account_default_time_zone: string or None
        :param account_default_storage_quota_mb: (optional) The default course storage quota to be used, if not otherwise specified.
        :type account_default_storage_quota_mb: integer or None
        :param account_default_user_storage_quota_mb: (optional) The default user storage quota to be used, if not otherwise specified.
        :type account_default_user_storage_quota_mb: integer or None
        :param account_default_group_storage_quota_mb: (optional) The default group storage quota to be used, if not otherwise specified.
        :type account_default_group_storage_quota_mb: integer or None
        :return: Update an account
        :rtype: requests.Response (with Account data)

    """

    path = '/v1/accounts/{id}'
    payload = {
        'account[name]' : account_name,
        'account[default_time_zone]' : account_default_time_zone,
        'account[default_storage_quota_mb]' : account_default_storage_quota_mb,
        'account[default_user_storage_quota_mb]' : account_default_user_storage_quota_mb,
        'account[default_group_storage_quota_mb]' : account_default_group_storage_quota_mb,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_sub_account(request_ctx, account_id, account_name, account_default_storage_quota_mb=None, account_default_user_storage_quota_mb=None, account_default_group_storage_quota_mb=None, per_page=None, **request_kwargs):
    """
    Add a new sub-account to a given account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param account_name: (required) The name of the new sub-account.
        :type account_name: string
        :param account_default_storage_quota_mb: (optional) The default course storage quota to be used, if not otherwise specified.
        :type account_default_storage_quota_mb: integer or None
        :param account_default_user_storage_quota_mb: (optional) The default user storage quota to be used, if not otherwise specified.
        :type account_default_user_storage_quota_mb: integer or None
        :param account_default_group_storage_quota_mb: (optional) The default group storage quota to be used, if not otherwise specified.
        :type account_default_group_storage_quota_mb: integer or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Create a new sub-account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/sub_accounts'
    payload = {
        'account[name]' : account_name,
        'account[default_storage_quota_mb]' : account_default_storage_quota_mb,
        'account[default_user_storage_quota_mb]' : account_default_user_storage_quota_mb,
        'account[default_group_storage_quota_mb]' : account_default_group_storage_quota_mb,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


