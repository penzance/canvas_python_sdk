from canvas_sdk import client, utils


def list_rubrics_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of active rubrics for the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List rubrics
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/rubrics'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_rubrics_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of active rubrics for the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List rubrics
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/rubrics'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_rubric_accounts(request_ctx, account_id, id, include=None, style=None, **request_kwargs):
    """
    Returns the rubric with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) If included, the type of associated rubric assessments to return. If not included, assessments will be omitted.
        :type include: string or None
        :param style: (optional) Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted.
        :type style: string or None
        :return: Get a single rubric
        :rtype: requests.Response (with Rubric data)

    """

    include_types = ('assessments', 'graded_assessments', 'peer_assessments')
    style_types = ('full', 'comments_only')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(style, style_types)
    path = '/v1/accounts/{account_id}/rubrics/{id}'
    payload = {
        'include': include,
        'style': style,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_rubric_courses(request_ctx, course_id, id, include=None, style=None, **request_kwargs):
    """
    Returns the rubric with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) If included, the type of associated rubric assessments to return. If not included, assessments will be omitted.
        :type include: string or None
        :param style: (optional) Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted.
        :type style: string or None
        :return: Get a single rubric
        :rtype: requests.Response (with Rubric data)

    """

    include_types = ('assessments', 'graded_assessments', 'peer_assessments')
    style_types = ('full', 'comments_only')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(style, style_types)
    path = '/v1/courses/{course_id}/rubrics/{id}'
    payload = {
        'include': include,
        'style': style,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


