from canvas_sdk import client, utils


def list_assignment_groups(request_ctx, course_id, include=None, exclude_assignment_submission_types=None, override_assignment_dates=None, grading_period_id=None, scope_assignments_to_student=None, per_page=None, **request_kwargs):
    """
    Returns the list of assignment groups for the current context. The returned
    groups are sorted by their position field.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) Associations to include with the group. "discussion_topic", "all_dates"
"assignment_visibility" & "submission" are only valid are only valid if "assignments" is also included.
The "assignment_visibility" option additionally requires that the Differentiated Assignments course feature be turned on.
        :type include: array or None
        :param exclude_assignment_submission_types: (optional) If "assignments" are included, those with the specified submission types
will be excluded from the assignment groups.
        :type exclude_assignment_submission_types: array or None
        :param override_assignment_dates: (optional) Apply assignment overrides for each assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :param grading_period_id: (optional) The id of the grading period in which assignment groups are being requested
(Requires the Multiple Grading Periods feature turned on.)
        :type grading_period_id: integer or None
        :param scope_assignments_to_student: (optional) If true, all assignments returned will apply to the current user in the
specified grading period. If assignments apply to other students in the
specified grading period, but not the current user, they will not be
returned. (Requires the grading_period_id argument and the Multiple Grading
Periods feature turned on. In addition, the current user must be a student.)
        :type scope_assignments_to_student: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignment groups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('assignments', 'discussion_topic', 'all_dates', 'assignment_visibility', 'overrides', 'submission')
    exclude_assignment_submission_types_types = ('online_quiz', 'discussion_topic', 'wiki_page', 'external_tool')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(exclude_assignment_submission_types, exclude_assignment_submission_types_types)
    path = '/v1/courses/{course_id}/assignment_groups'
    payload = {
        'include[]': include,
        'exclude_assignment_submission_types[]': exclude_assignment_submission_types,
        'override_assignment_dates': override_assignment_dates,
        'grading_period_id': grading_period_id,
        'scope_assignments_to_student': scope_assignments_to_student,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_assignment_group(request_ctx, course_id, assignment_group_id, include=None, override_assignment_dates=None, grading_period_id=None, **request_kwargs):
    """
    Returns the assignment group with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_group_id: (required) ID
        :type assignment_group_id: string
        :param include: (optional) Associations to include with the group. "discussion_topic" and "assignment_visibility" and "submission"
are only valid if "assignments" is also included. The "assignment_visibility" option additionally
requires that the Differentiated Assignments course feature be turned on.
        :type include: array or None
        :param override_assignment_dates: (optional) Apply assignment overrides for each assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :param grading_period_id: (optional) The id of the grading period in which assignment groups are being requested
(Requires the Multiple Grading Periods account feature turned on)
        :type grading_period_id: integer or None
        :return: Get an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    include_types = ('assignments', 'discussion_topic', 'assignment_visibility', 'submission')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'
    payload = {
        'include[]': include,
        'override_assignment_dates': override_assignment_dates,
        'grading_period_id': grading_period_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_group_id=assignment_group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_assignment_group(request_ctx, course_id, name=None, position=None, group_weight=None, sis_source_id=None, integration_data=None, rules=None, **request_kwargs):
    """
    Create a new assignment group for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param name: (optional) The assignment group's name
        :type name: string or None
        :param position: (optional) The position of this assignment group in relation to the other assignment groups
        :type position: integer or None
        :param group_weight: (optional) The percent of the total grade that this assignment group represents
        :type group_weight: Float or None
        :param sis_source_id: (optional) The sis source id of the Assignment Group
        :type sis_source_id: string or None
        :param integration_data: (optional) The integration data of the Assignment Group
        :type integration_data: Object or None
        :param rules: (optional) The grading rules that are applied within this assignment group
See the Assignment Group object definition for format
        :type rules: string or None
        :return: Create an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    path = '/v1/courses/{course_id}/assignment_groups'
    payload = {
        'name': name,
        'position': position,
        'group_weight': group_weight,
        'sis_source_id': sis_source_id,
        'integration_data': integration_data,
        'rules': rules,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_assignment_group(request_ctx, course_id, assignment_group_id, **request_kwargs):
    """
    Modify an existing Assignment Group.
    Accepts the same parameters as Assignment Group creation

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_group_id: (required) ID
        :type assignment_group_id: string
        :return: Edit an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_group_id=assignment_group_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def destroy_assignment_group(request_ctx, course_id, assignment_group_id, move_assignments_to=None, **request_kwargs):
    """
    Deletes the assignment group with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_group_id: (required) ID
        :type assignment_group_id: string
        :param move_assignments_to: (optional) The ID of an active Assignment Group to which the assignments that are
currently assigned to the destroyed Assignment Group will be assigned.
NOTE: If this argument is not provided, any assignments in this Assignment
Group will be deleted.
        :type move_assignments_to: integer or None
        :return: Destroy an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'
    payload = {
        'move_assignments_to': move_assignments_to,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_group_id=assignment_group_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


