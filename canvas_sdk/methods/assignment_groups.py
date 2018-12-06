from __future__ import unicode_literals
from canvas_sdk import client, utils

def list_assignment_groups(request_ctx, course_id, include, override_assignment_dates=None, per_page=None, **request_kwargs):
    """
    Returns the list of assignment groups for the current context. The returned
    groups are sorted by their position field.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (required) Associations to include with the group. both "discussion_topic" and "all_dates" is only valid are only valid if "assignments" is also included.
        :type include: string
        :param override_assignment_dates: (optional) Apply assignment overrides for each assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List assignment groups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('assignments', 'discussion_topic', 'all_dates')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignment_groups'
    payload = {
        'include' : include,
        'override_assignment_dates' : override_assignment_dates,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_assignment_group(request_ctx, course_id, assignment_group_id, include, override_assignment_dates=None, **request_kwargs):
    """
    Returns the assignment group with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_group_id: (required) ID
        :type assignment_group_id: string
        :param include: (required) Associations to include with the group. "discussion_topic" is only valid if "assignments" is also included.
        :type include: string
        :param override_assignment_dates: (optional) Apply assignment overrides for each assignment, defaults to true.
        :type override_assignment_dates: boolean or None
        :return: Get an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    include_types = ('assignments', 'discussion_topic')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'
    payload = {
        'include' : include,
        'override_assignment_dates' : override_assignment_dates,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_group_id=assignment_group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_assignment_group(request_ctx, course_id, name=None, position=None, group_weight=None, rules=None, **request_kwargs):
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
        :type group_weight: float or None
        :param rules: (optional) The grading rules that are applied within this assignment group See the Assignment Group object definition for format
        :type rules: string or None
        :return: Create an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    path = '/v1/courses/{course_id}/assignment_groups'
    payload = {
        'name' : name,
        'position' : position,
        'group_weight' : group_weight,
        'rules' : rules,
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


def destroy_assignment_group(request_ctx, course_id, assignment_group_id, move_assignment_to, **request_kwargs):
    """
    Deletes the assignment group with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_group_id: (required) ID
        :type assignment_group_id: string
        :param move_assignment_to: (required) The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted.
        :type move_assignment_to: string
        :return: Destroy an Assignment Group
        :rtype: requests.Response (with AssignmentGroup data)

    """

    path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'
    payload = {
        'move_assignment_to' : move_assignment_to,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_group_id=assignment_group_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


