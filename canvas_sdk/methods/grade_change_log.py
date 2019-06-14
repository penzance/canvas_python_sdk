from canvas_sdk import client, utils

def query_by_assignment(request_ctx, assignment_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    List grade change events for a given assignment.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Query by assignment.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/audit/grade_change/assignments/{assignment_id}'
    payload = {
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def query_by_course(request_ctx, course_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    List grade change events for a given course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Query by course.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/audit/grade_change/courses/{course_id}'
    payload = {
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def query_by_student(request_ctx, student_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    List grade change events for a given student.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param student_id: (required) ID
        :type student_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Query by student.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/audit/grade_change/students/{student_id}'
    payload = {
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(student_id=student_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def query_by_grader(request_ctx, grader_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    List grade change events for a given grader.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param grader_id: (required) ID
        :type grader_id: string
        :param start_time: (optional) The beginning of the time range from which you want events.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range from which you want events.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Query by grader.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/audit/grade_change/graders/{grader_id}'
    payload = {
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(grader_id=grader_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


