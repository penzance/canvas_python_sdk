from canvas_sdk import client, utils

def list_enrollments_courses(request_ctx, course_id, type=None, role=None, state=None, user_id=None, per_page=None, **request_kwargs):
    """
    Depending on the URL given, return either (1) all of the enrollments in
    a course, (2) all of the enrollments in a section or (3) all of a user's
    enrollments. This includes student, teacher, TA, and observer enrollments.
    
    If a user has multiple enrollments in a context (e.g. as a teacher
    and a student or in multiple course sections), each enrollment will be
    listed separately.
    
    note: Currently, only an admin user can return other users' enrollments. A
    user can, however, return his/her own enrollments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param type: (optional) A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given.
        :type type: string or None
        :param role: (optional) A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role: string or None
        :param state: (optional) Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. When querying a user's enrollments (either via user_id argument or via user enrollments endpoint), the following additional synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded"
        :type state: string or None
        :param user_id: (optional) Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster.
        :type user_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enrollments
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('active', 'invited', 'creation_pending', 'deleted', 'rejected', 'completed', 'inactive')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/courses/{course_id}/enrollments'
    payload = {
        'type[]' : type,
        'role[]' : role,
        'state[]' : state,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enrollments_sections(request_ctx, section_id, type=None, role=None, state=None, user_id=None, per_page=None, **request_kwargs):
    """
    Depending on the URL given, return either (1) all of the enrollments in
    a course, (2) all of the enrollments in a section or (3) all of a user's
    enrollments. This includes student, teacher, TA, and observer enrollments.
    
    If a user has multiple enrollments in a context (e.g. as a teacher
    and a student or in multiple course sections), each enrollment will be
    listed separately.
    
    note: Currently, only an admin user can return other users' enrollments. A
    user can, however, return his/her own enrollments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param type: (optional) A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given.
        :type type: string or None
        :param role: (optional) A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role: string or None
        :param state: (optional) Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. When querying a user's enrollments (either via user_id argument or via user enrollments endpoint), the following additional synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded"
        :type state: string or None
        :param user_id: (optional) Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster.
        :type user_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enrollments
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('active', 'invited', 'creation_pending', 'deleted', 'rejected', 'completed', 'inactive')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/sections/{section_id}/enrollments'
    payload = {
        'type[]' : type,
        'role[]' : role,
        'state[]' : state,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enrollments_users(request_ctx, user_id, type=None, role=None, state=None, per_page=None, **request_kwargs):
    """
    Depending on the URL given, return either (1) all of the enrollments in
    a course, (2) all of the enrollments in a section or (3) all of a user's
    enrollments. This includes student, teacher, TA, and observer enrollments.
    
    If a user has multiple enrollments in a context (e.g. as a teacher
    and a student or in multiple course sections), each enrollment will be
    listed separately.
    
    note: Currently, only an admin user can return other users' enrollments. A
    user can, however, return his/her own enrollments.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster.
        :type user_id: string
        :param type: (optional) A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given.
        :type type: string or None
        :param role: (optional) A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role: string or None
        :param state: (optional) Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. When querying a user's enrollments (either via user_id argument or via user enrollments endpoint), the following additional synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded"
        :type state: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enrollments
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('active', 'invited', 'creation_pending', 'deleted', 'rejected', 'completed', 'inactive')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/users/{user_id}/enrollments'
    payload = {
        'type[]' : type,
        'role[]' : role,
        'state[]' : state,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def enrollment_by_id(request_ctx, account_id, id, **request_kwargs):
    """
    Get an Enrollment object by Enrollment ID

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) The ID of the enrollment object
        :type id: integer
        :return: Enrollment by ID
        :rtype: requests.Response (with Enrollment data)

    """

    path = '/v1/accounts/{account_id}/enrollments/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def enroll_user_courses(request_ctx, course_id, enrollment_user_id, enrollment_type=None, enrollment_role=None, enrollment_role_id=None, enrollment_enrollment_state=None, enrollment_course_section_id=None, enrollment_limit_privileges_to_course_section=None, enrollment_notify=None, enrollment_self_enrollment_code=None, enrollment_self_enrolled=None, **request_kwargs):
    """
    Create a new user enrollment for a course or section.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param enrollment_user_id: (required) The ID of the user to be enrolled in the course.
        :type enrollment_user_id: string
        :param enrollment_type: (required) Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by enrollment[role] if supplied, otherwise 'StudentEnrollment' will be used.
        :type enrollment_type: string
        :param enrollment_role: (optional) Deprecated. Assigns a custom course-level role to the user.
        :type enrollment_role: string or None
        :param enrollment_role_id: (optional) Assigns a custom course-level role to the user.
        :type enrollment_role_id: string or None
        :param enrollment_enrollment_state: (optional) If set to 'active,' student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is 'invited.'
        :type enrollment_enrollment_state: string or None
        :param enrollment_course_section_id: (optional) The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored.
        :type enrollment_course_section_id: integer or None
        :param enrollment_limit_privileges_to_course_section: (optional) If a teacher or TA enrollment, teacher/TA will be restricted to the section given by course_section_id.
        :type enrollment_limit_privileges_to_course_section: boolean or None
        :param enrollment_notify: (optional) If true, a notification will be sent to the enrolled user. Notifications are not sent by default.
        :type enrollment_notify: boolean or None
        :param enrollment_self_enrollment_code: (optional) If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user_id must be 'self'. The enrollment_state will be set to 'active' and all other arguments will be ignored.
        :type enrollment_self_enrollment_code: string or None
        :param enrollment_self_enrolled: (optional) If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false.
        :type enrollment_self_enrolled: Boolean
        :return: Enroll a user
        :rtype: requests.Response (with Enrollment data)

    """

    enrollment_type_types = ('StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', 'DesignerEnrollment')
    enrollment_enrollment_state_types = ('active', 'invited')
    enrollment_role_type_choices = ('enrollment_role', 'enrollment_role_id', 'enrollment_type')
    utils.validate_attr_is_acceptable(enrollment_type, enrollment_type_types)
    utils.validate_attr_is_acceptable(enrollment_enrollment_state, enrollment_enrollment_state_types)
    utils.validate_any(enrollment_role_type_choices,
                       enrollment_role, enrollment_role_id, enrollment_type)
    path = '/v1/courses/{course_id}/enrollments'
    payload = {
        'enrollment[user_id]': enrollment_user_id,
        'enrollment[type]': enrollment_type,
        'enrollment[role]': enrollment_role,
        'enrollment[role_id]': enrollment_role_id,
        'enrollment[enrollment_state]': enrollment_enrollment_state,
        'enrollment[course_section_id]': enrollment_course_section_id,
        'enrollment[limit_privileges_to_course_section]': enrollment_limit_privileges_to_course_section,
        'enrollment[notify]': enrollment_notify,
        'enrollment[self_enrollment_code]': enrollment_self_enrollment_code,
        'enrollment[self_enrolled]': enrollment_self_enrolled,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def enroll_user_sections(request_ctx, section_id, enrollment_user_id, enrollment_type=None, enrollment_role=None, enrollment_role_id=None, enrollment_enrollment_state=None, enrollment_course_section_id=None, enrollment_limit_privileges_to_course_section=None, enrollment_notify=None, enrollment_self_enrollment_code=None, enrollment_self_enrolled=None, **request_kwargs):
    """
    Create a new user enrollment for a course or section.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param enrollment_user_id: (required) The ID of the user to be enrolled in the course.
        :type enrollment_user_id: string
        :param enrollment_type: (required) Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by enrollment[role] if supplied, otherwise 'StudentEnrollment' will be used.
        :type enrollment_type: string
        :param enrollment_role: (optional) Deprecated. Assigns a custom course-level role to the user.
        :type enrollment_role: string or None
        :param enrollment_role_id: (optional) Assigns a custom course-level role to the user.
        :type enrollment_role_id: string or None
        :param enrollment_enrollment_state: (optional) If set to 'active,' student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is 'invited.'
        :type enrollment_enrollment_state: string or None
        :param enrollment_course_section_id: (optional) The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored.
        :type enrollment_course_section_id: integer or None
        :param enrollment_limit_privileges_to_course_section: (optional) If a teacher or TA enrollment, teacher/TA will be restricted to the section given by course_section_id.
        :type enrollment_limit_privileges_to_course_section: boolean or None
        :param enrollment_notify: (optional) If true, a notification will be sent to the enrolled user. Notifications are not sent by default.
        :type enrollment_notify: boolean or None
        :param enrollment_self_enrollment_code: (optional) If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user_id must be 'self'. The enrollment_state will be set to 'active' and all other arguments will be ignored.
        :type enrollment_self_enrollment_code: string or None
        :param enrollment_self_enrolled: (optional) If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false.
        :type enrollment_self_enrolled: Boolean
        :return: Enroll a user
        :rtype: requests.Response (with Enrollment data)

    """

    enrollment_type_types = ('StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', 'DesignerEnrollment')
    enrollment_enrollment_state_types = ('active', 'invited')
    enrollment_role_type_choices = ('enrollment_role', 'enrollment_role_id', 'enrollment_type')
    utils.validate_attr_is_acceptable(enrollment_type, enrollment_type_types)
    utils.validate_attr_is_acceptable(enrollment_enrollment_state, enrollment_enrollment_state_types)
    utils.validate_any(enrollment_role_type_choices,
                       enrollment_role, enrollment_role_id, enrollment_type)
    path = '/v1/sections/{section_id}/enrollments'
    payload = {
        'enrollment[user_id]': enrollment_user_id,
        'enrollment[type]': enrollment_type,
        'enrollment[role]': enrollment_role,
        'enrollment[role_id]': enrollment_role_id,
        'enrollment[enrollment_state]': enrollment_enrollment_state,
        'enrollment[course_section_id]': enrollment_course_section_id,
        'enrollment[limit_privileges_to_course_section]': enrollment_limit_privileges_to_course_section,
        'enrollment[notify]': enrollment_notify,
        'enrollment[self_enrollment_code]': enrollment_self_enrollment_code,
        'enrollment[self_enrolled]': enrollment_self_enrolled,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def conclude_enrollment(request_ctx, course_id, id, task=None, **request_kwargs):
    """
    Delete or conclude an enrollment.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param task: (optional) The action to take on the enrollment.
        :type task: string or None
        :return: Conclude an enrollment
        :rtype: requests.Response (with Enrollment data)

    """

    task_types = ('conclude', 'delete')
    utils.validate_attr_is_acceptable(task, task_types)
    path = '/v1/courses/{course_id}/enrollments/{id}'
    payload = {
        'task' : task,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


