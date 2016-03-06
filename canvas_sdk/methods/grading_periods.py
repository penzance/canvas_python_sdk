from canvas_sdk import client, utils


def list_grading_periods_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of grading periods for the current course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List grading periods
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/grading_periods'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_grading_periods_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the list of grading periods for the current course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List grading periods
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/grading_periods'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_grading_period_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Returns the grading period with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/grading_periods/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_grading_period_accounts(request_ctx, account_id, id, **request_kwargs):
    """
    Returns the grading period with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/grading_periods/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_grading_period_courses(request_ctx, course_id, grading_periods_start_date, grading_periods_end_date, grading_periods_weight=None, **request_kwargs):
    """
    Create a new grading period for the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param grading_periods_start_date: (required) The date the grading period starts.
        :type grading_periods_start_date: array
        :param grading_periods_end_date: (required) no description
        :type grading_periods_end_date: array
        :param grading_periods_weight: (optional) The percentage weight of how much the period should count toward the course grade.
        :type grading_periods_weight: array or None
        :return: Create a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/grading_periods'
    payload = {
        'grading_periods[start_date]': grading_periods_start_date,
        'grading_periods[end_date]': grading_periods_end_date,
        'grading_periods[weight]': grading_periods_weight,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_single_grading_period_accounts(request_ctx, account_id, grading_periods_start_date, grading_periods_end_date, grading_periods_weight=None, **request_kwargs):
    """
    Create a new grading period for the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param grading_periods_start_date: (required) The date the grading period starts.
        :type grading_periods_start_date: array
        :param grading_periods_end_date: (required) no description
        :type grading_periods_end_date: array
        :param grading_periods_weight: (optional) The percentage weight of how much the period should count toward the course grade.
        :type grading_periods_weight: array or None
        :return: Create a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/grading_periods'
    payload = {
        'grading_periods[start_date]': grading_periods_start_date,
        'grading_periods[end_date]': grading_periods_end_date,
        'grading_periods[weight]': grading_periods_weight,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_single_grading_period_courses(request_ctx, course_id, id, grading_periods_start_date, grading_periods_end_date, grading_periods_weight=None, **request_kwargs):
    """
    Update an existing grading period.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param grading_periods_start_date: (required) The date the grading period starts.
        :type grading_periods_start_date: array
        :param grading_periods_end_date: (required) no description
        :type grading_periods_end_date: array
        :param grading_periods_weight: (optional) The percentage weight of how much the period should count toward the course grade.
        :type grading_periods_weight: array or None
        :return: Update a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/grading_periods/{id}'
    payload = {
        'grading_periods[start_date]': grading_periods_start_date,
        'grading_periods[end_date]': grading_periods_end_date,
        'grading_periods[weight]': grading_periods_weight,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_single_grading_period_accounts(request_ctx, account_id, id, grading_periods_start_date, grading_periods_end_date, grading_periods_weight=None, **request_kwargs):
    """
    Update an existing grading period.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param grading_periods_start_date: (required) The date the grading period starts.
        :type grading_periods_start_date: array
        :param grading_periods_end_date: (required) no description
        :type grading_periods_end_date: array
        :param grading_periods_weight: (optional) The percentage weight of how much the period should count toward the course grade.
        :type grading_periods_weight: array or None
        :return: Update a single grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/grading_periods/{id}'
    payload = {
        'grading_periods[start_date]': grading_periods_start_date,
        'grading_periods[end_date]': grading_periods_end_date,
        'grading_periods[weight]': grading_periods_weight,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_grading_period_courses(request_ctx, course_id, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/grading_periods/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_grading_period_accounts(request_ctx, account_id, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a grading period
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/grading_periods/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


