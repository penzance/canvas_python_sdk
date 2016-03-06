from canvas_sdk import client, utils

def list_your_groups(request_ctx, context_type=None, per_page=None, **request_kwargs):
    """
    Returns a list of active groups for the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param context_type: (optional) Only include groups that are in this type of context.
        :type context_type: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List your groups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    context_type_types = ('Account', 'Course')
    utils.validate_attr_is_acceptable(context_type, context_type_types)
    path = '/v1/users/self/groups'
    payload = {
        'context_type' : context_type,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_groups_available_in_context_accounts(request_ctx, account_id, only_own_groups=None, per_page=None, **request_kwargs):
    """
    Returns the list of active groups in the given context that are visible to user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param only_own_groups: (optional) Will only include groups that the user belongs to if this is set
        :type only_own_groups: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the groups available in a context.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/groups'
    payload = {
        'only_own_groups' : only_own_groups,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_groups_available_in_context_courses(request_ctx, course_id, only_own_groups=None, per_page=None, **request_kwargs):
    """
    Returns the list of active groups in the given context that are visible to user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param only_own_groups: (optional) Will only include groups that the user belongs to if this is set
        :type only_own_groups: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the groups available in a context.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/groups'
    payload = {
        'only_own_groups' : only_own_groups,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_group(request_ctx, group_id, include=None, **request_kwargs):
    """
    Returns the data for a single group, or a 401 if the caller doesn't have
    the rights to see it.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param include: (optional) - "permissions": Include permissions the current user has
  for the group.
        :type include: array or None
        :return: Get a single group
        :rtype: requests.Response (with Group data)

    """

    include_types = ('permissions')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/groups/{group_id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_group_groups(request_ctx, name=None, description=None, is_public=None, join_level=None, storage_quota_mb=None, **request_kwargs):
    """
    Creates a new group. Groups created using the "/api/v1/groups/"
    endpoint will be community groups.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param name: (optional) The name of the group
        :type name: string or None
        :param description: (optional) A description of the group
        :type description: string or None
        :param is_public: (optional) whether the group is public (applies only to community groups)
        :type is_public: boolean or None
        :param join_level: (optional) no description
        :type join_level: string or None
        :param storage_quota_mb: (optional) The allowed file storage for the group, in megabytes. This parameter is
ignored if the caller does not have the manage_storage_quotas permission.
        :type storage_quota_mb: integer or None
        :return: Create a group
        :rtype: requests.Response (with Group data)

    """

    join_level_types = ('parent_context_auto_join', 'parent_context_request', 'invitation_only')
    utils.validate_attr_is_acceptable(join_level, join_level_types)
    path = '/v1/groups'
    payload = {
        'name' : name,
        'description' : description,
        'is_public' : is_public,
        'join_level' : join_level,
        'storage_quota_mb' : storage_quota_mb,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_group_group_categories(request_ctx, group_category_id, name=None, description=None, is_public=None, join_level=None, storage_quota_mb=None, **request_kwargs):
    """
    Creates a new group. Groups created using the "/api/v1/groups/"
    endpoint will be community groups.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_category_id: (required) ID
        :type group_category_id: string
        :param name: (optional) The name of the group
        :type name: string or None
        :param description: (optional) A description of the group
        :type description: string or None
        :param is_public: (optional) whether the group is public (applies only to community groups)
        :type is_public: boolean or None
        :param join_level: (optional) no description
        :type join_level: string or None
        :param storage_quota_mb: (optional) The allowed file storage for the group, in megabytes. This parameter is
ignored if the caller does not have the manage_storage_quotas permission.
        :type storage_quota_mb: integer or None
        :return: Create a group
        :rtype: requests.Response (with Group data)

    """

    join_level_types = ('parent_context_auto_join', 'parent_context_request', 'invitation_only')
    utils.validate_attr_is_acceptable(join_level, join_level_types)
    path = '/v1/group_categories/{group_category_id}/groups'
    payload = {
        'name' : name,
        'description' : description,
        'is_public' : is_public,
        'join_level' : join_level,
        'storage_quota_mb' : storage_quota_mb,
    }
    url = request_ctx.base_api_url + path.format(group_category_id=group_category_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_group(request_ctx, group_id, name=None, description=None, is_public=None, join_level=None, avatar_id=None, storage_quota_mb=None, members=None, **request_kwargs):
    """
    Modifies an existing group.  Note that to set an avatar image for the
    group, you must first upload the image file to the group, and the use the
    id in the response as the argument to this function.  See the
    {file:file_uploads.html File Upload Documentation} for details on the file
    upload workflow.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param name: (optional) The name of the group
        :type name: string or None
        :param description: (optional) A description of the group
        :type description: string or None
        :param is_public: (optional) Whether the group is public (applies only to community groups). Currently
you cannot set a group back to private once it has been made public.
        :type is_public: boolean or None
        :param join_level: (optional) no description
        :type join_level: string or None
        :param avatar_id: (optional) The id of the attachment previously uploaded to the group that you would
like to use as the avatar image for this group.
        :type avatar_id: integer or None
        :param storage_quota_mb: (optional) The allowed file storage for the group, in megabytes. This parameter is
ignored if the caller does not have the manage_storage_quotas permission.
        :type storage_quota_mb: integer or None
        :param members: (optional) An array of user ids for users you would like in the group.
Users not in the group will be sent invitations. Existing group
members who aren't in the list will be removed from the group.
        :type members: array or None
        :return: Edit a group
        :rtype: requests.Response (with Group data)

    """

    join_level_types = ('parent_context_auto_join', 'parent_context_request', 'invitation_only')
    utils.validate_attr_is_acceptable(join_level, join_level_types)
    path = '/v1/groups/{group_id}'
    payload = {
        'name' : name,
        'description' : description,
        'is_public' : is_public,
        'join_level' : join_level,
        'avatar_id' : avatar_id,
        'storage_quota_mb' : storage_quota_mb,
        'members' : members,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_group(request_ctx, group_id, **request_kwargs):
    """
    Deletes a group and removes all members.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Delete a group
        :rtype: requests.Response (with Group data)

    """

    path = '/v1/groups/{group_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def invite_others_to_group(request_ctx, group_id, invitees, **request_kwargs):
    """
    Sends an invitation to all supplied email addresses which will allow the
    receivers to join the group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param invitees: (required) An array of email addresses to be sent invitations.
        :type invitees: array
        :return: Invite others to a group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/invite'
    payload = {
        'invitees' : invitees,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_group_s_users(request_ctx, group_id, search_term=None, include=None, per_page=None, **request_kwargs):
    """
    Returns a list of users in the group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the
results list. Must be at least 3 characters.
        :type search_term: string or None
        :param include: (optional) - "avatar_url": Include users' avatar_urls.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List group's users
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('avatar_url')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/groups/{group_id}/users'
    payload = {
        'search_term' : search_term,
        'include' : include,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def upload_file(request_ctx, group_id, **request_kwargs):
    """
    Upload a file to the group.
    
    This API endpoint is the first step in uploading a file to a group.
    See the {file:file_uploads.html File Upload Documentation} for details on
    the file upload workflow.
    
    Only those with the "Manage Files" permission on a group can upload files
    to the group. By default, this is anybody participating in the
    group, or any admin over the group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/files'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def preview_processed_html(request_ctx, group_id, html=None, **request_kwargs):
    """
    Preview html content processed for this group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param html: (optional) The html content to process
        :type html: string or None
        :return: Preview processed html
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/preview_html'
    payload = {
        'html' : html,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def group_activity_stream(request_ctx, group_id, **request_kwargs):
    """
    Returns the current user's group-specific activity stream, paginated.
    
    For full documentation, see the API documentation for the user activity
    stream, in the user api.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Group activity stream
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/activity_stream'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def group_activity_stream_summary(request_ctx, group_id, **request_kwargs):
    """
    Returns a summary of the current user's group-specific activity stream.
    
    For full documentation, see the API documentation for the user activity
    stream summary, in the user api.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Group activity stream summary
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/activity_stream/summary'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_group_memberships(request_ctx, group_id, filter_states=None, per_page=None, **request_kwargs):
    """
    List the members of a group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param filter_states: (optional) Only list memberships with the given workflow_states. By default it will
return all memberships.
        :type filter_states: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List group memberships
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    filter_states_types = ('accepted', 'invited', 'requested')
    utils.validate_attr_is_acceptable(filter_states, filter_states_types)
    path = '/v1/groups/{group_id}/memberships'
    payload = {
        'filter_states' : filter_states,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_group_membership_memberships(request_ctx, group_id, membership_id, **request_kwargs):
    """
    Returns the group membership with the given membership id or user id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param membership_id: (required) ID
        :type membership_id: string
        :return: Get a single group membership
        :rtype: requests.Response (with GroupMembership data)

    """

    path = '/v1/groups/{group_id}/memberships/{membership_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, membership_id=membership_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_group_membership_users(request_ctx, group_id, user_id, **request_kwargs):
    """
    Returns the group membership with the given membership id or user id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Get a single group membership
        :rtype: requests.Response (with GroupMembership data)

    """

    path = '/v1/groups/{group_id}/users/{user_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, user_id=user_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_membership(request_ctx, group_id, user_id=None, **request_kwargs):
    """
    Join, or request to join, a group, depending on the join_level of the
    group.  If the membership or join request already exists, then it is simply
    returned

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param user_id: (optional) no description
        :type user_id: string or None
        :return: Create a membership
        :rtype: requests.Response (with GroupMembership data)

    """

    path = '/v1/groups/{group_id}/memberships'
    payload = {
        'user_id' : user_id,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_membership_memberships(request_ctx, group_id, membership_id, workflow_state=None, moderator=None, **request_kwargs):
    """
    Accept a membership request, or add/remove moderator rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param membership_id: (required) ID
        :type membership_id: string
        :param workflow_state: (optional) Currently, the only allowed value is "accepted"
        :type workflow_state: string or None
        :param moderator: (optional) no description
        :type moderator: string or None
        :return: Update a membership
        :rtype: requests.Response (with GroupMembership data)

    """

    workflow_state_types = ('accepted')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/groups/{group_id}/memberships/{membership_id}'
    payload = {
        'workflow_state' : workflow_state,
        'moderator' : moderator,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, membership_id=membership_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_membership_users(request_ctx, group_id, user_id, workflow_state=None, moderator=None, **request_kwargs):
    """
    Accept a membership request, or add/remove moderator rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param workflow_state: (optional) Currently, the only allowed value is "accepted"
        :type workflow_state: string or None
        :param moderator: (optional) no description
        :type moderator: string or None
        :return: Update a membership
        :rtype: requests.Response (with GroupMembership data)

    """

    workflow_state_types = ('accepted')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    path = '/v1/groups/{group_id}/users/{user_id}'
    payload = {
        'workflow_state' : workflow_state,
        'moderator' : moderator,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def leave_group_memberships(request_ctx, group_id, membership_id, **request_kwargs):
    """
    Leave a group if you are allowed to leave (some groups, such as sets of
    course groups created by teachers, cannot be left). You may also use 'self'
    in place of a membership_id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param membership_id: (required) ID
        :type membership_id: string
        :return: Leave a group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/memberships/{membership_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, membership_id=membership_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def leave_group_users(request_ctx, group_id, user_id, **request_kwargs):
    """
    Leave a group if you are allowed to leave (some groups, such as sets of
    course groups created by teachers, cannot be left). You may also use 'self'
    in place of a membership_id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Leave a group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/users/{user_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, user_id=user_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


