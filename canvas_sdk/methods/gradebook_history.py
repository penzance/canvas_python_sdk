from canvas_sdk import client, utils

def days_in_gradebook_history_for_this_course(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns a map of dates to grader/assignment groups

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) The id of the contextual course for this API call
        :type course_id: integer
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Days in gradebook history for this course
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/gradebook_history/days'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def details_for_given_date_in_gradebook_history_for_this_course(request_ctx, course_id, date, per_page=None, **request_kwargs):
    """
    Returns the graders who worked on this day, along with the assignments they worked on.
    More details can be obtained by selecting a grader and assignment and calling the
    'submissions' api endpoint for a given date.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) The id of the contextual course for this API call
        :type course_id: integer
        :param date: (required) The date for which you would like to see detailed information
        :type date: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Details for a given date in gradebook history for this course
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/gradebook_history/{date}'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, date=date)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def lists_submissions(request_ctx, course_id, date, grader_id, assignment_id, per_page=None, **request_kwargs):
    """
    Gives a nested list of submission versions

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) The id of the contextual course for this API call
        :type course_id: integer
        :param date: (required) The date for which you would like to see submissions
        :type date: string
        :param grader_id: (required) The ID of the grader for which you want to see submissions
        :type grader_id: integer
        :param assignment_id: (required) The ID of the assignment for which you want to see submissions
        :type assignment_id: integer
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Lists submissions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, date=date, grader_id=grader_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_uncollated_submission_versions(request_ctx, course_id, assignment_id=None, user_id=None, ascending=None, per_page=None, **request_kwargs):
    """
    Gives a paginated, uncollated list of submission versions for all matching
    submissions in the context. This SubmissionVersion objects will not include
    the +new_grade+ or +previous_grade+ keys, only the +grade+; same for
    +graded_at+ and +grader+.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) The id of the contextual course for this API call
        :type course_id: integer
        :param assignment_id: (optional) The ID of the assignment for which you want to see submissions. If absent, versions of submissions from any assignment in the course are included.
        :type assignment_id: integer or None
        :param user_id: (optional) The ID of the user for which you want to see submissions. If absent, versions of submissions from any user in the course are included.
        :type user_id: integer or None
        :param ascending: (optional) Returns submission versions in ascending date order (oldest first). If absent, returns submission versions in descending date order (newest first).
        :type ascending: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List uncollated submission versions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/gradebook_history/feed'
    payload = {
        'assignment_id' : assignment_id,
        'user_id' : user_id,
        'ascending' : ascending,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


