from canvas_sdk import client, utils


def get_department_level_participation_data_terms(request_ctx, account_id, term_id, **request_kwargs):
    """
    Returns page view hits summed across all courses in the department. Two
    groupings of these counts are returned; one by day (+by_date+), the other
    by category (+by_category+). The possible categories are announcements,
    assignments, collaborations, conferences, discussions, files, general,
    grades, groups, modules, other, pages, and quizzes.
    
    This and the other department-level endpoints have three variations which
    all return the same style of data but for different subsets of courses. All
    share the prefix /api/v1/accounts/<account_id>/analytics. The possible
    suffixes are:
    
     * /current: includes all available courses in the default term
     * /completed: includes all concluded courses in the default term
     * /terms/<term_id>: includes all available or concluded courses in the
       given term.
    
    Courses not yet offered or which have been deleted are never included.
    
    /current and /completed are intended for use when the account has only one
    term. /terms/<term_id> is intended for use when the account has multiple
    terms.
    
    The action follows the suffix.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param term_id: (required) ID
        :type term_id: string
        :return: Get department-level participation data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/terms/{term_id}/activity'
    url = request_ctx.base_api_url + path.format(account_id=account_id, term_id=term_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_participation_data_current(request_ctx, account_id, **request_kwargs):
    """
    Returns page view hits summed across all courses in the department. Two
    groupings of these counts are returned; one by day (+by_date+), the other
    by category (+by_category+). The possible categories are announcements,
    assignments, collaborations, conferences, discussions, files, general,
    grades, groups, modules, other, pages, and quizzes.
    
    This and the other department-level endpoints have three variations which
    all return the same style of data but for different subsets of courses. All
    share the prefix /api/v1/accounts/<account_id>/analytics. The possible
    suffixes are:
    
     * /current: includes all available courses in the default term
     * /completed: includes all concluded courses in the default term
     * /terms/<term_id>: includes all available or concluded courses in the
       given term.
    
    Courses not yet offered or which have been deleted are never included.
    
    /current and /completed are intended for use when the account has only one
    term. /terms/<term_id> is intended for use when the account has multiple
    terms.
    
    The action follows the suffix.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level participation data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/current/activity'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_participation_data_completed(request_ctx, account_id, **request_kwargs):
    """
    Returns page view hits summed across all courses in the department. Two
    groupings of these counts are returned; one by day (+by_date+), the other
    by category (+by_category+). The possible categories are announcements,
    assignments, collaborations, conferences, discussions, files, general,
    grades, groups, modules, other, pages, and quizzes.
    
    This and the other department-level endpoints have three variations which
    all return the same style of data but for different subsets of courses. All
    share the prefix /api/v1/accounts/<account_id>/analytics. The possible
    suffixes are:
    
     * /current: includes all available courses in the default term
     * /completed: includes all concluded courses in the default term
     * /terms/<term_id>: includes all available or concluded courses in the
       given term.
    
    Courses not yet offered or which have been deleted are never included.
    
    /current and /completed are intended for use when the account has only one
    term. /terms/<term_id> is intended for use when the account has multiple
    terms.
    
    The action follows the suffix.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level participation data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/completed/activity'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_grade_data_terms(request_ctx, account_id, term_id, **request_kwargs):
    """
    Returns the distribution of grades for students in courses in the
    department.  Each data point is one student's current grade in one course;
    if a student is in multiple courses, he contributes one value per course,
    but if he's enrolled multiple times in the same course (e.g. a lecture
    section and a lab section), he only constributes on value for that course.
    
    Grades are binned to the nearest integer score; anomalous grades outside
    the 0 to 100 range are ignored. The raw counts are returned, not yet
    normalized by the total count.
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param term_id: (required) ID
        :type term_id: string
        :return: Get department-level grade data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/terms/{term_id}/grades'
    url = request_ctx.base_api_url + path.format(account_id=account_id, term_id=term_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_grade_data_current(request_ctx, account_id, **request_kwargs):
    """
    Returns the distribution of grades for students in courses in the
    department.  Each data point is one student's current grade in one course;
    if a student is in multiple courses, he contributes one value per course,
    but if he's enrolled multiple times in the same course (e.g. a lecture
    section and a lab section), he only constributes on value for that course.
    
    Grades are binned to the nearest integer score; anomalous grades outside
    the 0 to 100 range are ignored. The raw counts are returned, not yet
    normalized by the total count.
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level grade data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/current/grades'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_grade_data_completed(request_ctx, account_id, **request_kwargs):
    """
    Returns the distribution of grades for students in courses in the
    department.  Each data point is one student's current grade in one course;
    if a student is in multiple courses, he contributes one value per course,
    but if he's enrolled multiple times in the same course (e.g. a lecture
    section and a lab section), he only constributes on value for that course.
    
    Grades are binned to the nearest integer score; anomalous grades outside
    the 0 to 100 range are ignored. The raw counts are returned, not yet
    normalized by the total count.
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level grade data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/completed/grades'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_statistics_terms(request_ctx, account_id, term_id, **request_kwargs):
    """
    Returns numeric statistics about the department and term (or filter).
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param term_id: (required) ID
        :type term_id: string
        :return: Get department-level statistics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics'
    url = request_ctx.base_api_url + path.format(account_id=account_id, term_id=term_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_statistics_current(request_ctx, account_id, **request_kwargs):
    """
    Returns numeric statistics about the department and term (or filter).
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level statistics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/current/statistics'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_department_level_statistics_completed(request_ctx, account_id, **request_kwargs):
    """
    Returns numeric statistics about the department and term (or filter).
    
    Shares the same variations on endpoint as the participation data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Get department-level statistics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/analytics/completed/statistics'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_course_level_participation_data(request_ctx, course_id, **request_kwargs):
    """
    Returns page view hits and participation numbers grouped by day through the
    entire history of the course. Page views is returned as a hash, where the
    hash keys are dates in the format "YYYY-MM-DD". The page_views result set
    includes page views broken out by access category. Participations is
    returned as an array of dates in the format "YYYY-MM-DD".

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Get course-level participation data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/analytics/activity'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_course_level_assignment_data(request_ctx, course_id, async=None, **request_kwargs):
    """
    Returns a list of assignments for the course sorted by due date. For
    each assignment returns basic assignment information, the grade breakdown,
    and a breakdown of on-time/late status of homework submissions.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param async: (optional) If async is true, then the course_assignments call can happen asynch-
ronously and MAY return a response containing a progress_url key instead
of an assignments array. If it does, then it is the caller's
responsibility to poll the API again to see if the progress is complete.
If the data is ready (possibly even on the first async call) then it
will be passed back normally, as documented in the example response.
        :type async: boolean or None
        :return: Get course-level assignment data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/analytics/assignments'
    payload = {
        'async': async,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_course_level_student_summary_data(request_ctx, course_id, sort_column=None, student_id=None, **request_kwargs):
    """
    Returns a summary of per-user access information for all students in
    a course. This includes total page views, total participations, and a
    breakdown of on-time/late status for all homework submissions in the course.
    
    Each student's summary also includes the maximum number of page views and
    participations by any student in the course, which may be useful for some
    visualizations (since determining maximums client side can be tricky with
    pagination).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param sort_column: (optional) The order results in which results are returned.  Defaults to "name".
        :type sort_column: string or None
        :param student_id: (optional) If set, returns only the specified student.
        :type student_id: string or None
        :return: Get course-level student summary data
        :rtype: requests.Response (with void data)

    """

    sort_column_types = ('name', 'name_descending', 'score', 'score_descending', 'participations', 'participations_descending', 'page_views', 'page_views_descending')
    utils.validate_attr_is_acceptable(sort_column, sort_column_types)
    path = '/v1/courses/{course_id}/analytics/student_summaries'
    payload = {
        'sort_column': sort_column,
        'student_id': student_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_user_in_a_course_level_participation_data(request_ctx, course_id, student_id, **request_kwargs):
    """
    Returns page view hits grouped by hour, and participation details through the
    entire history of the course.
    
    `page_views` are returned as a hash, where the keys are iso8601 dates, bucketed by the hour.
    `participations` are returned as an array of hashes, sorted oldest to newest.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param student_id: (required) ID
        :type student_id: string
        :return: Get user-in-a-course-level participation data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/analytics/users/{student_id}/activity'
    url = request_ctx.base_api_url + path.format(course_id=course_id, student_id=student_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_user_in_a_course_level_assignment_data(request_ctx, course_id, student_id, **request_kwargs):
    """
    Returns a list of assignments for the course sorted by due date. For
    each assignment returns basic assignment information, the grade breakdown
    (including the student's actual grade), and the basic submission
    information for the student's submission if it exists.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param student_id: (required) ID
        :type student_id: string
        :return: Get user-in-a-course-level assignment data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/analytics/users/{student_id}/assignments'
    url = request_ctx.base_api_url + path.format(course_id=course_id, student_id=student_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_user_in_a_course_level_messaging_data(request_ctx, course_id, student_id, **request_kwargs):
    """
    Returns messaging "hits" grouped by day through the entire history of the
    course. Returns a hash containing the number of instructor-to-student messages,
    and student-to-instructor messages, where the hash keys are dates
    in the format "YYYY-MM-DD". Message hits include Conversation messages and
    comments on homework submissions.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param student_id: (required) ID
        :type student_id: string
        :return: Get user-in-a-course-level messaging data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/analytics/users/{student_id}/communication'
    url = request_ctx.base_api_url + path.format(course_id=course_id, student_id=student_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


