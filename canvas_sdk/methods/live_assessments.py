from canvas_sdk import client, utils

def create_live_assessment_results(request_ctx, course_id, assessment_id, **request_kwargs):
    """
    Creates live assessment results and adds them to a live assessment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assessment_id: (required) ID
        :type assessment_id: string
        :return: Create live assessment results
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/live_assessments/{assessment_id}/results'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assessment_id=assessment_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def list_live_assessment_results(request_ctx, course_id, assessment_id, user_id=None, per_page=None, **request_kwargs):
    """
    Returns a list of live assessment results

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assessment_id: (required) ID
        :type assessment_id: string
        :param user_id: (optional) If set, restrict results to those for this user
        :type user_id: integer or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List live assessment results
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/live_assessments/{assessment_id}/results'
    payload = {
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assessment_id=assessment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_or_find_live_assessment(request_ctx, course_id, **request_kwargs):
    """
    Creates or finds an existing live assessment with the given key and aligns it with
    the linked outcome

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Create or find a live assessment
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/live_assessments'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def list_live_assessments(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns a list of live assessments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List live assessments
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/live_assessments'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


