def list_enrollments_courses(request_ctx, course_id, type=None, role=None, role_id=None, state=None, user_id=None, per_page=None, **request_kwargs):
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
        :param role_id: (optional) A list of enrollment role IDs to return. Accepted values include course-level the numeric IDs of the roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role_id: integer or None
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
        'role_id[]' : role_id,
        'state[]' : state,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enrollments_sections(request_ctx, section_id, type=None, role=None, role_id=None, state=None, user_id=None, per_page=None, **request_kwargs):
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
        :param role_id: (optional) A list of enrollment role IDs to return. Accepted values include course-level the numeric IDs of the roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role_id: integer or None
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
        'role_id[]' : role_id,
        'state[]' : state,
        'user_id' : user_id,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enrollments_users(request_ctx, user_id, type=None, role=None, role_id=None, state=None, per_page=None, **request_kwargs):
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
        :param role_id: (optional) A list of enrollment role IDs to return. Accepted values include course-level the numeric IDs of the roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above.
        :type role_id: integer or None
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
        'role_id[]' : role_id,
        'state[]' : state,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response
