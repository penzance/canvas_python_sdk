from canvas_sdk import client, utils


def list_your_courses(request_ctx, include, enrollment_type=None, enrollment_role=None, state=None, per_page=None, as_user_id=None, **request_kwargs):
    """
    Returns the list of active courses for the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param include: (required) - "needs_grading_count": Optional information to include with each Course. When needs_grading_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned. - "syllabus_body": Optional information to include with each Course. When syllabus_body is given the user-generated html for the course syllabus is returned. - "total_scores": Optional information to include with each Course. When total_scores is given, any enrollments with type 'student' will also include the fields 'calculated_current_score', 'calculated_final_score', 'calculated_current_grade', and 'calculated_final_grade'. calculated_current_score is the student's score in the course, ignoring ungraded assignments. calculated_final_score is the student's score in the course including ungraded assignments with a score of 0. calculated_current_grade is the letter grade equivalent of calculated_current_score (if available). calculated_final_grade is the letter grade equivalent of calculated_final_score (if available). This argument is ignored if the course is configured to hide final grades. - "term": Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned. - "course_progress": Optional information to include with each Course. When course_progress is given, each course will include a 'course_progress' object with the fields: 'requirement_count', an integer specifying the total number of requirements in the course, 'requirement_completed_count', an integer specifying the total number of requirements in this course that have been completed, and 'next_requirement_url', a string url to the next requirement item, and 'completed_at', the date the course was completed (null if incomplete). 'next_requirement_url' will be null if all requirements have been completed or the current module does not require sequential progress. "course_progress" will return an error message if the course is not module based or the user is not enrolled as a student in the course. - "sections": Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start_at, end_at), as well as the enrollment type (enrollment_role, e.g. 'StudentEnrollment').
        :type include: string
        :param enrollment_type: (optional) When set, only return courses where the user is enrolled as this type. For example, set to "teacher" to return only courses where the user is enrolled as a Teacher. This argument is ignored if enrollment_role is given.
        :type enrollment_type: string or None
        :param enrollment_role: (optional) When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'.
        :type enrollment_role: string or None
        :param state: (optional) If set, only return courses that are in the given state(s). By default, "available" is returned for students and observers, and anything except "deleted", for all other enrollment types
        :type state: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List your courses
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    enrollment_type_types = ('teacher', 'student', 'ta', 'observer', 'designer')
    include_types = ('needs_grading_count', 'syllabus_body', 'total_scores', 'term', 'course_progress', 'sections')
    state_types = ('unpublished', 'available', 'completed', 'deleted')
    utils.validate_attr_is_acceptable(enrollment_type, enrollment_type_types)
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/courses'
    payload = {
        'enrollment_type' : enrollment_type,
        'enrollment_role' : enrollment_role,
        'include[]' : include,
        'state[]' : state,
        'per_page' : per_page,
    }
    if as_user_id:
        payload['as_user_id'] = as_user_id
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_course(request_ctx, account_id, course_name=None, course_course_code=None, course_start_at=None, course_end_at=None, course_license=None, course_is_public=None, course_is_public_to_auth_users=None, course_public_syllabus=None, course_public_description=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_allow_student_forum_attachments=None, course_open_enrollment=None, course_self_enrollment=None, course_restrict_enrollments_to_course_dates=None, course_term_id=None, course_sis_course_id=None, course_integration_id=None, course_hide_final_grades=None, course_apply_assignment_group_weights=None, offer=None, enroll_me=None, course_syllabus_body=None, **request_kwargs):
    """
    Create a new course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The unique ID of the account to create to course under.
        :type account_id: integer
        :param course_name: (optional) The name of the course. If omitted, the course will be named "Unnamed Course."
        :type course_name: string or None
        :param course_course_code: (optional) The course code for the course.
        :type course_course_code: string or None
        :param course_start_at: (optional) Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type course_start_at: datetime or None
        :param course_end_at: (optional) Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type course_end_at: datetime or None
        :param course_license: (optional) The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain).
        :type course_license: string or None
        :param course_is_public: (optional) Set to true if course if public.
        :type course_is_public: boolean or None
        :param course_is_public_to_auth_users: (optional) Set to true if course is public to authorized users.
        :type course_is_public_to_auth_users: boolean or None
        :param course_public_syllabus: (optional) Set to true to make the course syllabus public.
        :type course_public_syllabus: boolean or None
        :param course_public_description: (optional) A publicly visible description of the course.
        :type course_public_description: string or None
        :param course_allow_student_wiki_edits: (optional) If true, students will be able to modify the course wiki.
        :type course_allow_student_wiki_edits: boolean or None
        :param course_allow_wiki_comments: (optional) If true, course members will be able to comment on wiki pages.
        :type course_allow_wiki_comments: boolean or None
        :param course_allow_student_forum_attachments: (optional) If true, students can attach files to forum posts.
        :type course_allow_student_forum_attachments: boolean or None
        :param course_open_enrollment: (optional) Set to true if the course is open enrollment.
        :type course_open_enrollment: boolean or None
        :param course_self_enrollment: (optional) Set to true if the course is self enrollment.
        :type course_self_enrollment: boolean or None
        :param course_restrict_enrollments_to_course_dates: (optional) Set to true to restrict user enrollments to the start and end dates of the course.
        :type course_restrict_enrollments_to_course_dates: boolean or None
        :param course_term_id: (optional) The unique ID of the term to create to course in.
        :type course_term_id: integer or None
        :param course_sis_course_id: (optional) The unique SIS identifier.
        :type course_sis_course_id: string or None
        :param course_integration_id: (optional) The unique Integration identifier.
        :type course_integration_id: string or None
        :param course_hide_final_grades: (optional) If this option is set to true, the totals in student grades summary will be hidden.
        :type course_hide_final_grades: boolean or None
        :param course_apply_assignment_group_weights: (optional) Set to true to weight final grade based on assignment groups percentages.
        :type course_apply_assignment_group_weights: boolean or None
        :param offer: (optional) If this option is set to true, the course will be available to students immediately.
        :type offer: boolean or None
        :param enroll_me: (optional) Set to true to enroll the current user as the teacher.
        :type enroll_me: boolean or None
        :param course_syllabus_body: (optional) The syllabus body for the course
        :type course_syllabus_body: string or None
        :return: Create a new course
        :rtype: requests.Response (with Course data)

    """

    path = '/v1/accounts/{account_id}/courses'
    payload = {
        'course[name]' : course_name,
        'course[course_code]' : course_course_code,
        'course[start_at]' : course_start_at,
        'course[end_at]' : course_end_at,
        'course[license]' : course_license,
        'course[is_public]' : course_is_public,
        'course[is_public_to_auth_users]' : course_is_public_to_auth_users,
        'course[public_syllabus]' : course_public_syllabus,
        'course[public_description]' : course_public_description,
        'course[allow_student_wiki_edits]' : course_allow_student_wiki_edits,
        'course[allow_wiki_comments]' : course_allow_wiki_comments,
        'course[allow_student_forum_attachments]' : course_allow_student_forum_attachments,
        'course[open_enrollment]' : course_open_enrollment,
        'course[self_enrollment]' : course_self_enrollment,
        'course[restrict_enrollments_to_course_dates]' : course_restrict_enrollments_to_course_dates,
        'course[term_id]' : course_term_id,
        'course[sis_course_id]' : course_sis_course_id,
        'course[integration_id]' : course_integration_id,
        'course[hide_final_grades]' : course_hide_final_grades,
        'course[apply_assignment_group_weights]' : course_apply_assignment_group_weights,
        'offer' : offer,
        'enroll_me' : enroll_me,
        'course[syllabus_body]' : course_syllabus_body,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def upload_file(request_ctx, course_id, **request_kwargs):
    """
    Upload a file to the course.

    This API endpoint is the first step in uploading a file to a course.
    See the {file:file_uploads.html File Upload Documentation} for details on
    the file upload workflow.

    Only those with the "Manage Files" permission on a course can upload files
    to the course. By default, this is Teachers, TAs and Designers.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/files'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def list_students(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of students enrolled in this course.

    DEPRECATED: Please use the `CoursesController#users <https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb>`_ endpoint
    and pass "student" as the enrollment_type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List students
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/students'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_users_in_course_users(request_ctx, course_id, include, search_term=None, enrollment_type=None, enrollment_role=None, user_id=None, per_page=None, **request_kwargs):
    """
    Returns the list of users in this course. And optionally the user's enrollments in the course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (required) - "email": Optional user email. - "enrollments": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "test_student": Optionally include the course's Test Student, if present. Default is to not include Test Student.
        :type include: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the results list.
        :type search_term: string or None
        :param enrollment_type: (optional) When set, only return users where the user is enrolled as this type. This argument is ignored if enrollment_role is given.
        :type enrollment_type: string or None
        :param enrollment_role: (optional) When set, only return users enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'.
        :type enrollment_role: string or None
        :param user_id: (optional) If included, the user will be queried and if the user is part of the users set, the page parameter will be modified so that the page containing user_id will be returned.
        :type user_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in course
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    enrollment_type_types = ('teacher', 'student', 'ta', 'observer', 'designer')
    include_types = ('email', 'enrollments', 'locked', 'avatar_url', 'test_student')
    utils.validate_attr_is_acceptable(enrollment_type, enrollment_type_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/users'
    payload = {
        'search_term' : search_term,
        'enrollment_type' : enrollment_type,
        'enrollment_role' : enrollment_role,
        'include[]' : include,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_users_in_course_search_users(request_ctx, course_id, include, search_term=None, enrollment_type=None, enrollment_role=None, user_id=None, per_page=None, **request_kwargs):
    """
    Returns the list of users in this course. And optionally the user's enrollments in the course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (required) - "email": Optional user email. - "enrollments": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "test_student": Optionally include the course's Test Student, if present. Default is to not include Test Student.
        :type include: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the results list.
        :type search_term: string or None
        :param enrollment_type: (optional) When set, only return users where the user is enrolled as this type. This argument is ignored if enrollment_role is given.
        :type enrollment_type: string or None
        :param enrollment_role: (optional) When set, only return users enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'.
        :type enrollment_role: string or None
        :param user_id: (optional) If included, the user will be queried and if the user is part of the users set, the page parameter will be modified so that the page containing user_id will be returned.
        :type user_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in course
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    enrollment_type_types = ('teacher', 'student', 'ta', 'observer', 'designer')
    include_types = ('email', 'enrollments', 'locked', 'avatar_url', 'test_student')
    utils.validate_attr_is_acceptable(enrollment_type, enrollment_type_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/search_users'
    payload = {
        'search_term' : search_term,
        'enrollment_type' : enrollment_type,
        'enrollment_role' : enrollment_role,
        'include[]' : include,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_recently_logged_in_students(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of users in this course, ordered by how recently they have
    logged in. The records include the 'last_login' field which contains
    a timestamp of the last time that user logged into canvas.  The querying
    user must have the 'View usage reports' permission.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List recently logged in students
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/recent_students'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_user(request_ctx, course_id, id, **request_kwargs):
    """
    Return information on a single user.

    Accepts the same include[] parameters as the :users: action, and returns a
    single user with the same fields as that action.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get single user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/courses/{course_id}/users/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def preview_processed_html(request_ctx, course_id, html, **request_kwargs):
    """
    Preview html content processed for this course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param html: (required) The html content to process
        :type html: string
        :return: Preview processed html
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/preview_html'
    payload = {
        'html' : html,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def course_activity_stream(request_ctx, course_id, **request_kwargs):
    """
    Returns the current user's course-specific activity stream, paginated.

    For full documentation, see the API documentation for the user activity
    stream, in the user api.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Course activity stream
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/activity_stream'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def course_activity_stream_summary(request_ctx, course_id, **request_kwargs):
    """
    Returns a summary of the current user's course-specific activity stream.

    For full documentation, see the API documentation for the user activity
    stream summary, in the user api.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Course activity stream summary
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/activity_stream/summary'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def course_todo_items(request_ctx, course_id, **request_kwargs):
    """
    Returns the current user's course-specific todo items.

    For full documentation, see the API documentation for the user todo items, in the user api.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Course TODO items
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/todo'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def conclude_course(request_ctx, id, event, **request_kwargs):
    """
    Delete or conclude an existing course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param event: (required) The action to take on the course.
        :type event: string
        :return: Conclude a course
        :rtype: requests.Response (with void data)

    """

    event_types = ('delete', 'conclude')
    utils.validate_attr_is_acceptable(event, event_types)
    path = '/v1/courses/{id}'
    payload = {
        'event' : event,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_course_settings(request_ctx, course_id, **request_kwargs):
    """
    Returns some of a course's settings.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Get course settings
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/settings'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_course_settings(request_ctx, course_id, allow_student_discussion_topics, allow_student_forum_attachments, allow_student_discussion_editing, **request_kwargs):
    """
    Can update the following course settings:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param allow_student_discussion_topics: (required) no description
        :type allow_student_discussion_topics: boolean
        :param allow_student_forum_attachments: (required) no description
        :type allow_student_forum_attachments: boolean
        :param allow_student_discussion_editing: (required) no description
        :type allow_student_discussion_editing: boolean
        :return: Update course settings
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/settings'
    payload = {
        'allow_student_discussion_topics' : allow_student_discussion_topics,
        'allow_student_forum_attachments' : allow_student_forum_attachments,
        'allow_student_discussion_editing' : allow_student_discussion_editing,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_course_courses(request_ctx, id, include, **request_kwargs):
    """
    Return information on a single course.

    Accepts the same include[] parameters as the list action plus:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param include: (required) - "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has for the course.
        :type include: string
        :return: Get a single course
        :rtype: requests.Response (with Course data)

    """

    include_types = ('all_courses', 'permissions')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{id}'
    payload = {
        'include[]' : include,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_course_accounts(request_ctx, account_id, id, include, **request_kwargs):
    """
    Return information on a single course.

    Accepts the same include[] parameters as the list action plus:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param include: (required) - "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has for the course.
        :type include: string
        :return: Get a single course
        :rtype: requests.Response (with Course data)

    """

    include_types = ('all_courses', 'permissions')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/accounts/{account_id}/courses/{id}'
    payload = {
        'include[]' : include,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_course(request_ctx, id, course_account_id=None, course_name=None, course_course_code=None, course_start_at=None, course_end_at=None, course_license=None, course_is_public=None, course_is_public_to_auth_users=None, course_public_syllabus=None, course_public_description=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_allow_student_forum_attachments=None, course_open_enrollment=None, course_self_enrollment=None, course_restrict_enrollments_to_course_dates=None, course_term_id=None, course_sis_course_id=None, course_integration_id=None, course_hide_final_grades=None, course_apply_assignment_group_weights=None, offer=None, course_syllabus_body=None, course_grading_standard_id=None, course_course_format=None, course_event=None, **request_kwargs):

    """
    Update an existing course.

    For possible arguments, see the Courses#create documentation (note: the enroll_me param is not allowed in the update action).

    Additional arguments available for Courses#update
        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param account_id: (optional) The unique ID of the account to move course into. If ommitted, do not change the course's account.
        :type account_id: integer
        :param course_name: (optional) The name of the course. If omitted, the course will be named "Unnamed Course."
        :type course_name: string or None
        :param course_course_code: (optional) The course code for the course.
        :type course_course_code: string or None
        :param course_start_at: (optional) Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type course_start_at: datetime or None
        :param course_end_at: (optional) Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type course_end_at: datetime or None
        :param course_license: (optional) The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain).
        :type course_license: string or None
        :param course_is_public: (optional) Set to true if course if public.
        :type course_is_public: boolean or None
        :param course_is_public_to_auth_users: (optional) Set to true if course is public to authorized users.
        :type course_is_public_to_auth_users: boolean or None
        :param course_public_syllabus: (optional) Set to true to make the course syllabus public.
        :type course_public_syllabus: boolean or None
        :param course_public_description: (optional) A publicly visible description of the course.
        :type course_public_description: string or None
        :param course_allow_student_wiki_edits: (optional) If true, students will be able to modify the course wiki.
        :type course_allow_student_wiki_edits: boolean or None
        :param course_allow_wiki_comments: (optional) If true, course members will be able to comment on wiki pages.
        :type course_allow_wiki_comments: boolean or None
        :param course_allow_student_forum_attachments: (optional) If true, students can attach files to forum posts.
        :type course_allow_student_forum_attachments: boolean or None
        :param course_open_enrollment: (optional) Set to true if the course is open enrollment.
        :type course_open_enrollment: boolean or None
        :param course_self_enrollment: (optional) Set to true if the course is self enrollment.
        :type course_self_enrollment: boolean or None
        :param course_restrict_enrollments_to_course_dates: (optional) Set to true to restrict user enrollments to the start and end dates of the course.
        :type course_restrict_enrollments_to_course_dates: boolean or None
        :param course_term_id: (optional) The unique ID of the term to create to course in.
        :type course_term_id: integer or None
        :param course_sis_course_id: (optional) The unique SIS identifier.
        :type course_sis_course_id: string or None
        :param course_integration_id: (optional) The unique Integration identifier.
        :type course_integration_id: string or None
        :param course_hide_final_grades: (optional) If this option is set to true, the totals in student grades summary will be hidden.
        :type course_hide_final_grades: boolean or None
        :param course_apply_assignment_group_weights: (optional) Set to true to weight final grade based on assignment groups percentages.
        :type course_apply_assignment_group_weights: boolean or None
        :param offer: (optional) If this option is set to true, the course will be available to students immediately.
        :type offer: boolean or None
        :param enroll_me: (optional) Set to true to enroll the current user as the teacher.
        :type enroll_me: boolean or None
        :param course_syllabus_body: (optional) The syllabus body for the course
        :type course_syllabus_body: string or None
        :param course_event: (optional) Change the course workflow state: 'claim' for unpublished; 'offer' for published
        :type course_event: string or None
        :return: Update a course
        :rtype: requests.Response (with void data)

    """

    payload = {
        'course[account_id]' : course_account_id,
        'course[name]' : course_name,
        'course[course_code]' : course_course_code,
        'course[start_at]' : course_start_at,
        'course[end_at]' : course_end_at,
        'course[license]' : course_license,
        'course[is_public]' : course_is_public,
        'course[is_public_to_auth_users]' : course_is_public_to_auth_users,
        'course[public_syllabus]' : course_public_syllabus,
        'course[public_description]' : course_public_description,
        'course[allow_student_wiki_edits]' : course_allow_student_wiki_edits,
        'course[allow_wiki_comments]' : course_allow_wiki_comments,
        'course[allow_student_forum_attachments]' : course_allow_student_forum_attachments,
        'course[open_enrollment]' : course_open_enrollment,
        'course[self_enrollment]' : course_self_enrollment,
        'course[restrict_enrollments_to_course_dates]' : course_restrict_enrollments_to_course_dates,
        'course[term_id]' : course_term_id,
        'course[sis_course_id]' : course_sis_course_id,
        'course[integration_id]' : course_integration_id,
        'course[hide_final_grades]' : course_hide_final_grades,
        'course[apply_assignment_group_weights]' : course_apply_assignment_group_weights,
        'offer' : offer,
        'course[syllabus_body]' : course_syllabus_body,
        'course[grading_standard_id]' : course_grading_standard_id,
        'course[course_format]' : course_course_format,
        'course[event]': course_event,
    }

    path = '/v1/courses/{id}'

    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_courses(request_ctx, account_id, course_ids, event, **request_kwargs):
    """
    Update multiple courses in an account.  Operates asynchronously; use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_
    to query the status of an operation.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param course_ids: (required) List of ids of courses to update. At most 500 courses may be updated in one call.
        :type course_ids: string
        :param event: (required) The action to take on each course. Must be one of 'offer', 'conclude', 'delete', or 'undelete'. * 'offer' makes a course visible to students. This action is also called "publish" on the web site. * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears in prior-enrollment lists. * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a future date. * 'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered.
        :type event: string
        :return: Update courses
        :rtype: requests.Response (with Progress data)

    """

    path = '/v1/accounts/{account_id}/courses'
    payload = {
        'course_ids[]' : course_ids,
        'event' : event,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_course_copy_status(request_ctx, course_id, id, **request_kwargs):
    """
    DEPRECATED: Please use the `ContentMigrationsController#create <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_

    Retrieve the status of a course copy

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get course copy status
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/course_copy/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def copy_course_content(request_ctx, course_id, source_course, var_except, only, **request_kwargs):
    """
    DEPRECATED: Please use the `ContentMigrationsController#create <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_migrations_controller.rb>`_

    Copies content from one course into another. The default is to copy all course
    content. You can control specific types to copy by using either the 'except' option
    or the 'only' option.

    The response is the same as the course copy status endpoint

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param source_course: (required) ID or SIS-ID of the course to copy the content from
        :type source_course: string
        :param var_except: (required) A list of the course content types to exclude, all areas not listed will be copied.
        :type var_except: string
        :param only: (required) A list of the course content types to copy, all areas not listed will not be copied.
        :type only: string
        :return: Copy course content
        :rtype: requests.Response (with void data)

    """

    var_except_types = ('course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes')
    only_types = ('course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes')
    utils.validate_attr_is_acceptable(var_except, var_except_types)
    utils.validate_attr_is_acceptable(only, only_types)
    path = '/v1/courses/{course_id}/course_copy'
    payload = {
        'source_course' : source_course,
        'except[]' : var_except,
        'only[]' : only,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response



def reset_content(request_ctx, course_id, **request_kwargs):
    """
    Deletes the current course, and creates a new equivalent course with no content, but all sections and users moved over.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/reset_content'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response
