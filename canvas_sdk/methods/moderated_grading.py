from canvas_sdk import client, utils

def list_students_selected_for_moderation(request_ctx, course_id, assignment_id, per_page=None, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List students selected for moderation
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def select_students_for_moderation(request_ctx, course_id, assignment_id, student_ids=None, per_page=None, **request_kwargs):
    """
    Returns an array of users that were selected for moderation

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param student_ids: (optional) user ids for students to select for moderation
        :type student_ids: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Select students for moderation
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students'
    payload = {
        'student_ids' : student_ids,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_provisional_grade_status_for_student(request_ctx, course_id, assignment_id, student_id=None, **request_kwargs):
    """
    Tell whether the student's submission needs one or more provisional grades.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param student_id: (optional) The id of the student to show the status for
        :type student_id: integer or None
        :return: Show provisional grade status for a student
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status'
    payload = {
        'student_id' : student_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def select_provisional_grade(request_ctx, course_id, assignment_id, provisional_grade_id, **request_kwargs):
    """
    Choose which provisional grade the student should receive for a submission.
    The caller must have :moderate_grades rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param provisional_grade_id: (required) ID
        :type provisional_grade_id: string
        :return: Select provisional grade
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, provisional_grade_id=provisional_grade_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def copy_provisional_grade(request_ctx, course_id, assignment_id, provisional_grade_id, **request_kwargs):
    """
    Given a provisional grade, copy the grade (and associated submission comments and rubric assessments)
    to a "final" mark which can be edited or commented upon by a moderator prior to publication of grades.
    
    Notes:
    * The student must be in the moderation set for the assignment.
    * The newly created grade will be selected.
    * The caller must have "Moderate Grades" rights in the course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param provisional_grade_id: (required) ID
        :type provisional_grade_id: string
        :return: Copy provisional grade
        :rtype: requests.Response (with ProvisionalGrade data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/copy_to_final_mark'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, provisional_grade_id=provisional_grade_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def publish_provisional_grades_for_assignment(request_ctx, course_id, assignment_id, **request_kwargs):
    """
    Publish the selected provisional grade for all submissions to an assignment.
    Use the "Select provisional grade" endpoint to choose which provisional grade to publish
    for a particular submission.
    
    Students not in the moderation set will have their one and only provisional grade published.
    
    WARNING: This is irreversible. This will overwrite existing grades in the gradebook.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :return: Publish provisional grades for an assignment
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


