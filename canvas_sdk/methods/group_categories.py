from canvas_sdk import client, utils


def list_group_categories_for_context_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns a list of group categories in a context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List group categories for a context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/group_categories'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_group_categories_for_context_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns a list of group categories in a context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List group categories for a context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/group_categories'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_group_category(request_ctx, group_category_id, **request_kwargs):
    """
    Returns the data for a single group category, or a 401 if the caller doesn't have
    the rights to see it.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :return: Get a single group category
        :rtype: requests.Response (with GroupCategory data)

    """

    path = '/v1/group_categories/{group_category_id}'
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_group_category_accounts(request_ctx, account_id, name, self_signup=None, auto_leader=None, group_limit=None, create_group_count=None, split_group_count=None, **request_kwargs):
    """
    Create a new group category

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param name: (required) Name of the group category
        :type name: string
        :param self_signup: (optional) Allow students to sign up for a group themselves (Course Only).
valid values are:
"enabled":: allows students to self sign up for any group in course
"restricted":: allows students to self sign up only for groups in the
               same section null disallows self sign up
        :type self_signup: string or None
        :param auto_leader: (optional) Assigns group leaders automatically when generating and allocating students to groups
Valid values are:
"first":: the first student to be allocated to a group is the leader
"random":: a random student from all members is chosen as the leader
        :type auto_leader: string or None
        :param group_limit: (optional) Limit the maximum number of users in each group (Course Only). Requires
self signup.
        :type group_limit: integer or None
        :param create_group_count: (optional) Create this number of groups (Course Only).
        :type create_group_count: integer or None
        :param split_group_count: (optional) (Deprecated)
Create this number of groups, and evenly distribute students
among them. not allowed with "enable_self_signup". because
the group assignment happens synchronously, it's recommended
that you instead use the assign_unassigned_members endpoint.
(Course Only)
        :type split_group_count: string or None
        :return: Create a Group Category
        :rtype: requests.Response (with GroupCategory data)

    """

    self_signup_types = ('enabled', 'restricted')
    auto_leader_types = ('first', 'random')
    utils.validate_attr_is_acceptable(self_signup, self_signup_types)
    utils.validate_attr_is_acceptable(auto_leader, auto_leader_types)
    path = '/v1/accounts/{account_id}/group_categories'
    payload = {
        'name': name,
        'self_signup': self_signup,
        'auto_leader': auto_leader,
        'group_limit': group_limit,
        'create_group_count': create_group_count,
        'split_group_count': split_group_count,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_group_category_courses(request_ctx, course_id, name, self_signup=None, auto_leader=None, group_limit=None, create_group_count=None, split_group_count=None, **request_kwargs):
    """
    Create a new group category

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param name: (required) Name of the group category
        :type name: string
        :param self_signup: (optional) Allow students to sign up for a group themselves (Course Only).
valid values are:
"enabled":: allows students to self sign up for any group in course
"restricted":: allows students to self sign up only for groups in the
               same section null disallows self sign up
        :type self_signup: string or None
        :param auto_leader: (optional) Assigns group leaders automatically when generating and allocating students to groups
Valid values are:
"first":: the first student to be allocated to a group is the leader
"random":: a random student from all members is chosen as the leader
        :type auto_leader: string or None
        :param group_limit: (optional) Limit the maximum number of users in each group (Course Only). Requires
self signup.
        :type group_limit: integer or None
        :param create_group_count: (optional) Create this number of groups (Course Only).
        :type create_group_count: integer or None
        :param split_group_count: (optional) (Deprecated)
Create this number of groups, and evenly distribute students
among them. not allowed with "enable_self_signup". because
the group assignment happens synchronously, it's recommended
that you instead use the assign_unassigned_members endpoint.
(Course Only)
        :type split_group_count: string or None
        :return: Create a Group Category
        :rtype: requests.Response (with GroupCategory data)

    """

    self_signup_types = ('enabled', 'restricted')
    auto_leader_types = ('first', 'random')
    utils.validate_attr_is_acceptable(self_signup, self_signup_types)
    utils.validate_attr_is_acceptable(auto_leader, auto_leader_types)
    path = '/v1/courses/{course_id}/group_categories'
    payload = {
        'name': name,
        'self_signup': self_signup,
        'auto_leader': auto_leader,
        'group_limit': group_limit,
        'create_group_count': create_group_count,
        'split_group_count': split_group_count,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_group_category(request_ctx, group_category_id, name=None, self_signup=None, auto_leader=None, group_limit=None, create_group_count=None, split_group_count=None, **request_kwargs):
    """
    Modifies an existing group category.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :param name: (optional) Name of the group category
        :type name: string or None
        :param self_signup: (optional) Allow students to sign up for a group themselves (Course Only).
Valid values are:
"enabled":: allows students to self sign up for any group in course
"restricted":: allows students to self sign up only for groups in the
               same section null disallows self sign up
        :type self_signup: string or None
        :param auto_leader: (optional) Assigns group leaders automatically when generating and allocating students to groups
Valid values are:
"first":: the first student to be allocated to a group is the leader
"random":: a random student from all members is chosen as the leader
        :type auto_leader: string or None
        :param group_limit: (optional) Limit the maximum number of users in each group (Course Only). Requires
self signup.
        :type group_limit: integer or None
        :param create_group_count: (optional) Create this number of groups (Course Only).
        :type create_group_count: integer or None
        :param split_group_count: (optional) (Deprecated)
Create this number of groups, and evenly distribute students
among them. not allowed with "enable_self_signup". because
the group assignment happens synchronously, it's recommended
that you instead use the assign_unassigned_members endpoint.
(Course Only)
        :type split_group_count: string or None
        :return: Update a Group Category
        :rtype: requests.Response (with GroupCategory data)

    """

    self_signup_types = ('enabled', 'restricted')
    auto_leader_types = ('first', 'random')
    utils.validate_attr_is_acceptable(self_signup, self_signup_types)
    utils.validate_attr_is_acceptable(auto_leader, auto_leader_types)
    path = '/v1/group_categories/{group_category_id}'
    payload = {
        'name': name,
        'self_signup': self_signup,
        'auto_leader': auto_leader,
        'group_limit': group_limit,
        'create_group_count': create_group_count,
        'split_group_count': split_group_count,
    }
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_group_category(request_ctx, group_category_id, **request_kwargs):
    """
    Deletes a group category and all groups under it. Protected group
    categories can not be deleted, i.e. "communities" and "student_organized".

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :return: Delete a Group Category
        :rtype: requests.Response (with void data)

    """

    path = '/v1/group_categories/{group_category_id}'
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_groups_in_group_category(request_ctx, group_category_id, per_page=None, **request_kwargs):
    """
    Returns a list of groups in a group category

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List groups in group category
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/group_categories/{group_category_id}/groups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_users_in_group_category(request_ctx, group_category_id, search_term=None, unassigned=None, per_page=None, **request_kwargs):
    """
    Returns a list of users in the group category.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the results
list. Must be at least 3 characters.
        :type search_term: string or None
        :param unassigned: (optional) Set this value to true if you wish only to search unassigned users in the
group category.
        :type unassigned: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in group category
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/group_categories/{group_category_id}/users'
    payload = {
        'search_term': search_term,
        'unassigned': unassigned,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def assign_unassigned_members(request_ctx, group_category_id, sync=None, **request_kwargs):
    """
    Assign all unassigned members as evenly as possible among the existing
    student groups.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :param sync: (optional) The assigning is done asynchronously by default. If you would like to
override this and have the assigning done synchronously, set this value
to true.
        :type sync: boolean or None
        :return: Assign unassigned members
        :rtype: requests.Response (with GroupMembership | Progress data)

    """

    path = '/v1/group_categories/{group_category_id}/assign_unassigned_members'
    payload = {
        'sync': sync,
    }
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


