from canvas_sdk import client, utils


def list_collaborations_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    List collaborations the current user has access to in the context of the course
    provided in the url. NOTE: this only returns ExternalToolCollaboration type
    collaborations.
    
      curl https://<canvas>/api/v1/courses/1/collaborations/

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List collaborations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/collaborations'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_collaborations_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    List collaborations the current user has access to in the context of the course
    provided in the url. NOTE: this only returns ExternalToolCollaboration type
    collaborations.
    
      curl https://<canvas>/api/v1/courses/1/collaborations/

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List collaborations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/collaborations'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_members_of_collaboration(request_ctx, id, include=None, per_page=None, **request_kwargs):
    """
    List the collaborators of a given collaboration

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param include: (optional) - "collaborator_lti_id": Optional information to include with each member.
  Represents an identifier to be used for the member in an LTI context.
- "avatar_image_url": Optional information to include with each member.
  The url for the avatar of a collaborator with type 'user'.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List members of a collaboration.
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('collaborator_lti_id', 'avatar_image_url')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/collaborations/{id}/members'
    payload = {
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_potential_members_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    List the users who can potentially be added to a collaboration in the given context.
    
    For courses, this consists of all enrolled users.  For groups, it is comprised of the
    group members plus the admins of the course containing the group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List potential members
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/potential_collaborators'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_potential_members_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    List the users who can potentially be added to a collaboration in the given context.
    
    For courses, this consists of all enrolled users.  For groups, it is comprised of the
    group members plus the admins of the course containing the group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List potential members
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/potential_collaborators'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


