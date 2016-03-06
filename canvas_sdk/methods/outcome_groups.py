from canvas_sdk import client, utils


def redirect_to_root_outcome_group_for_context_global(request_ctx, **request_kwargs):
    """
    Convenience redirect to find the root outcome group for a particular
    context. Will redirect to the appropriate outcome group's URL.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Redirect to root outcome group for context
        :rtype: requests.Response (with void data)

    """

    path = '/v1/global/root_outcome_group'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def redirect_to_root_outcome_group_for_context_accounts(request_ctx, account_id, **request_kwargs):
    """
    Convenience redirect to find the root outcome group for a particular
    context. Will redirect to the appropriate outcome group's URL.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Redirect to root outcome group for context
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/root_outcome_group'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def redirect_to_root_outcome_group_for_context_courses(request_ctx, course_id, **request_kwargs):
    """
    Convenience redirect to find the root outcome group for a particular
    context. Will redirect to the appropriate outcome group's URL.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Redirect to root outcome group for context
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/root_outcome_group'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_all_outcome_groups_for_context_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all outcome groups for context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/outcome_groups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_outcome_groups_for_context_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all outcome groups for context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/outcome_groups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_outcome_links_for_context_accounts(request_ctx, account_id, outcome_style=None, outcome_group_style=None, per_page=None, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param outcome_style: (optional) The detail level of the outcomes. Defaults to "abbrev".
Specify "full" for more information.
        :type outcome_style: string or None
        :param outcome_group_style: (optional) The detail level of the outcome groups. Defaults to "abbrev".
Specify "full" for more information.
        :type outcome_group_style: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all outcome links for context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/outcome_group_links'
    payload = {
        'outcome_style': outcome_style,
        'outcome_group_style': outcome_group_style,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_outcome_links_for_context_courses(request_ctx, course_id, outcome_style=None, outcome_group_style=None, per_page=None, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param outcome_style: (optional) The detail level of the outcomes. Defaults to "abbrev".
Specify "full" for more information.
        :type outcome_style: string or None
        :param outcome_group_style: (optional) The detail level of the outcome groups. Defaults to "abbrev".
Specify "full" for more information.
        :type outcome_group_style: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all outcome links for context
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/outcome_group_links'
    payload = {
        'outcome_style': outcome_style,
        'outcome_group_style': outcome_group_style,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_outcome_group_global(request_ctx, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Show an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/global/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_outcome_group_accounts(request_ctx, account_id, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Show an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_outcome_group_courses(request_ctx, course_id, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Show an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_outcome_group_global(request_ctx, id, title=None, description=None, vendor_guid=None, parent_outcome_group_id=None, **request_kwargs):
    """
    Modify an existing outcome group. Fields not provided are left as is;
    unrecognized fields are ignored.
    
    When changing the parent outcome group, the new parent group must belong to
    the same context as this outcome group, and must not be a descendant of
    this outcome group (i.e. no cycles allowed).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param title: (optional) The new outcome group title.
        :type title: string or None
        :param description: (optional) The new outcome group description.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param parent_outcome_group_id: (optional) The id of the new parent outcome group.
        :type parent_outcome_group_id: integer or None
        :return: Update an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/global/outcome_groups/{id}'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
        'parent_outcome_group_id': parent_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_outcome_group_accounts(request_ctx, account_id, id, title=None, description=None, vendor_guid=None, parent_outcome_group_id=None, **request_kwargs):
    """
    Modify an existing outcome group. Fields not provided are left as is;
    unrecognized fields are ignored.
    
    When changing the parent outcome group, the new parent group must belong to
    the same context as this outcome group, and must not be a descendant of
    this outcome group (i.e. no cycles allowed).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param title: (optional) The new outcome group title.
        :type title: string or None
        :param description: (optional) The new outcome group description.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param parent_outcome_group_id: (optional) The id of the new parent outcome group.
        :type parent_outcome_group_id: integer or None
        :return: Update an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
        'parent_outcome_group_id': parent_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_outcome_group_courses(request_ctx, course_id, id, title=None, description=None, vendor_guid=None, parent_outcome_group_id=None, **request_kwargs):
    """
    Modify an existing outcome group. Fields not provided are left as is;
    unrecognized fields are ignored.
    
    When changing the parent outcome group, the new parent group must belong to
    the same context as this outcome group, and must not be a descendant of
    this outcome group (i.e. no cycles allowed).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param title: (optional) The new outcome group title.
        :type title: string or None
        :param description: (optional) The new outcome group description.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param parent_outcome_group_id: (optional) The id of the new parent outcome group.
        :type parent_outcome_group_id: integer or None
        :return: Update an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
        'parent_outcome_group_id': parent_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_outcome_group_global(request_ctx, id, **request_kwargs):
    """
    Deleting an outcome group deletes descendant outcome groups and outcome
    links. The linked outcomes themselves are only deleted if all links to the
    outcome were deleted.
    
    Aligned outcomes cannot be deleted; as such, if all remaining links to an
    aligned outcome are included in this group's descendants, the group
    deletion will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/global/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_outcome_group_accounts(request_ctx, account_id, id, **request_kwargs):
    """
    Deleting an outcome group deletes descendant outcome groups and outcome
    links. The linked outcomes themselves are only deleted if all links to the
    outcome were deleted.
    
    Aligned outcomes cannot be deleted; as such, if all remaining links to an
    aligned outcome are included in this group's descendants, the group
    deletion will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_outcome_group_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Deleting an outcome group deletes descendant outcome groups and outcome
    links. The linked outcomes themselves are only deleted if all links to the
    outcome were deleted.
    
    Aligned outcomes cannot be deleted; as such, if all remaining links to an
    aligned outcome are included in this group's descendants, the group
    deletion will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_linked_outcomes_global(request_ctx, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeLink children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List linked outcomes
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/global/outcome_groups/{id}/outcomes'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_linked_outcomes_accounts(request_ctx, account_id, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeLink children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List linked outcomes
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/outcome_groups/{id}/outcomes'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_linked_outcomes_courses(request_ctx, course_id, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeLink children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List linked outcomes
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/outcome_groups/{id}/outcomes'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_global(request_ctx, id, outcome_id=None, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param outcome_id: (optional) The ID of the existing outcome to link.
        :type outcome_id: integer or None
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/global/outcome_groups/{id}/outcomes'
    payload = {
        'outcome_id': outcome_id,
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_global_outcome_id(request_ctx, id, outcome_id, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) The ID of the existing outcome to link.
        :type outcome_id: integer
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/global/outcome_groups/{id}/outcomes/{outcome_id}'
    payload = {
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(id=id, outcome_id=outcome_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_accounts(request_ctx, account_id, id, outcome_id=None, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (optional) The ID of the existing outcome to link.
        :type outcome_id: integer or None
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/accounts/{account_id}/outcome_groups/{id}/outcomes'
    payload = {
        'outcome_id': outcome_id,
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_accounts_outcome_id(request_ctx, account_id, id, outcome_id, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) The ID of the existing outcome to link.
        :type outcome_id: integer
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}'
    payload = {
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id, outcome_id=outcome_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_courses(request_ctx, course_id, id, outcome_id=None, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (optional) The ID of the existing outcome to link.
        :type outcome_id: integer or None
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/courses/{course_id}/outcome_groups/{id}/outcomes'
    payload = {
        'outcome_id': outcome_id,
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_link_outcome_courses_outcome_id(request_ctx, course_id, id, outcome_id, title=None, display_name=None, description=None, vendor_guid=None, mastery_points=None, ratings_description=None, ratings_points=None, calculation_method=None, calculation_int=None, **request_kwargs):
    """
    Link an outcome into the outcome group. The outcome to link can either be
    specified by a PUT to the link URL for a specific outcome (the outcome_id
    in the PUT URLs) or by supplying the information for a new outcome (title,
    description, ratings, mastery_points) in a POST to the collection.
    
    If linking an existing outcome, the outcome_id must identify an outcome
    available to this context; i.e. an outcome owned by this group's context,
    an outcome owned by an associated account, or a global outcome. With
    outcome_id present, any other parameters are ignored.
    
    If defining a new outcome, the outcome is created in the outcome group's
    context using the provided title, description, ratings, and mastery points;
    the title is required but all other fields are optional. The new outcome
    is then linked into the outcome group.
    
    If ratings are provided when creating a new outcome, an embedded rubric
    criterion is included in the new outcome. This criterion's mastery_points
    default to the maximum points in the highest rating if not specified in the
    mastery_points parameter. Any ratings lacking a description are given a
    default of "No description". Any ratings lacking a point value are given a
    default of 0. If no ratings are provided, the mastery_points parameter is
    ignored.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) The ID of the existing outcome to link.
        :type outcome_id: integer
        :param title: (optional) The title of the new outcome. Required if outcome_id is absent.
        :type title: string or None
        :param display_name: (optional) A friendly name shown in reports for outcomes with cryptic titles,
such as common core standards names.
        :type display_name: string or None
        :param description: (optional) The description of the new outcome.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard.
        :type vendor_guid: string or None
        :param mastery_points: (optional) The mastery threshold for the embedded rubric criterion.
        :type mastery_points: integer or None
        :param ratings_description: (optional) The description of a rating level for the embedded rubric criterion.
        :type ratings_description: array or None
        :param ratings_points: (optional) The points corresponding to a rating level for the embedded rubric criterion.
        :type ratings_points: array or None
        :param calculation_method: (optional) The new calculation method.  Defaults to "highest"
        :type calculation_method: string or None
        :param calculation_int: (optional) The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery"
        :type calculation_int: integer or None
        :return: Create/link an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    calculation_method_types = ('decaying_average', 'n_mastery', 'latest', 'highest')
    utils.validate_attr_is_acceptable(calculation_method, calculation_method_types)
    path = '/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}'
    payload = {
        'title': title,
        'display_name': display_name,
        'description': description,
        'vendor_guid': vendor_guid,
        'mastery_points': mastery_points,
        'ratings[description]': ratings_description,
        'ratings[points]': ratings_points,
        'calculation_method': calculation_method,
        'calculation_int': calculation_int,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id, outcome_id=outcome_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def unlink_outcome_global(request_ctx, id, outcome_id, **request_kwargs):
    """
    Unlinking an outcome only deletes the outcome itself if this was the last
    link to the outcome in any group in any context. Aligned outcomes cannot be
    deleted; as such, if this is the last link to an aligned outcome, the
    unlinking will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) ID
        :type outcome_id: string
        :return: Unlink an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    path = '/v1/global/outcome_groups/{id}/outcomes/{outcome_id}'
    url = request_ctx.base_api_url + path.format(id=id, outcome_id=outcome_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def unlink_outcome_accounts(request_ctx, account_id, id, outcome_id, **request_kwargs):
    """
    Unlinking an outcome only deletes the outcome itself if this was the last
    link to the outcome in any group in any context. Aligned outcomes cannot be
    deleted; as such, if this is the last link to an aligned outcome, the
    unlinking will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) ID
        :type outcome_id: string
        :return: Unlink an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id, outcome_id=outcome_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def unlink_outcome_courses(request_ctx, course_id, id, outcome_id, **request_kwargs):
    """
    Unlinking an outcome only deletes the outcome itself if this was the last
    link to the outcome in any group in any context. Aligned outcomes cannot be
    deleted; as such, if this is the last link to an aligned outcome, the
    unlinking will fail.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param outcome_id: (required) ID
        :type outcome_id: string
        :return: Unlink an outcome
        :rtype: requests.Response (with OutcomeLink data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id, outcome_id=outcome_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_subgroups_global(request_ctx, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeGroup children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List subgroups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/global/outcome_groups/{id}/subgroups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_subgroups_accounts(request_ctx, account_id, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeGroup children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List subgroups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/outcome_groups/{id}/subgroups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_subgroups_courses(request_ctx, course_id, id, per_page=None, **request_kwargs):
    """
    List the immediate OutcomeGroup children of the outcome group. Paginated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List subgroups
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/outcome_groups/{id}/subgroups'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_subgroup_global(request_ctx, id, title, description=None, vendor_guid=None, **request_kwargs):
    """
    Creates a new empty subgroup under the outcome group with the given title
    and description.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param title: (required) The title of the new outcome group.
        :type title: string
        :param description: (optional) The description of the new outcome group.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard
        :type vendor_guid: string or None
        :return: Create a subgroup
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/global/outcome_groups/{id}/subgroups'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_subgroup_accounts(request_ctx, account_id, id, title, description=None, vendor_guid=None, **request_kwargs):
    """
    Creates a new empty subgroup under the outcome group with the given title
    and description.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param title: (required) The title of the new outcome group.
        :type title: string
        :param description: (optional) The description of the new outcome group.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard
        :type vendor_guid: string or None
        :return: Create a subgroup
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}/subgroups'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_subgroup_courses(request_ctx, course_id, id, title, description=None, vendor_guid=None, **request_kwargs):
    """
    Creates a new empty subgroup under the outcome group with the given title
    and description.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param title: (required) The title of the new outcome group.
        :type title: string
        :param description: (optional) The description of the new outcome group.
        :type description: string or None
        :param vendor_guid: (optional) A custom GUID for the learning standard
        :type vendor_guid: string or None
        :return: Create a subgroup
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}/subgroups'
    payload = {
        'title': title,
        'description': description,
        'vendor_guid': vendor_guid,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def import_outcome_group_global(request_ctx, id, source_outcome_group_id, **request_kwargs):
    """
    Creates a new subgroup of the outcome group with the same title and
    description as the source group, then creates links in that new subgroup to
    the same outcomes that are linked in the source group. Recurses on the
    subgroups of the source group, importing them each in turn into the new
    subgroup.
    
    Allows you to copy organizational structure, but does not create copies of
    the outcomes themselves, only new links.
    
    The source group must be either global, from the same context as this
    outcome group, or from an associated account. The source group cannot be
    the root outcome group of its context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param source_outcome_group_id: (required) The ID of the source outcome group.
        :type source_outcome_group_id: integer
        :return: Import an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/global/outcome_groups/{id}/import'
    payload = {
        'source_outcome_group_id': source_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def import_outcome_group_accounts(request_ctx, account_id, id, source_outcome_group_id, **request_kwargs):
    """
    Creates a new subgroup of the outcome group with the same title and
    description as the source group, then creates links in that new subgroup to
    the same outcomes that are linked in the source group. Recurses on the
    subgroups of the source group, importing them each in turn into the new
    subgroup.
    
    Allows you to copy organizational structure, but does not create copies of
    the outcomes themselves, only new links.
    
    The source group must be either global, from the same context as this
    outcome group, or from an associated account. The source group cannot be
    the root outcome group of its context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :param source_outcome_group_id: (required) The ID of the source outcome group.
        :type source_outcome_group_id: integer
        :return: Import an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/accounts/{account_id}/outcome_groups/{id}/import'
    payload = {
        'source_outcome_group_id': source_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def import_outcome_group_courses(request_ctx, course_id, id, source_outcome_group_id, **request_kwargs):
    """
    Creates a new subgroup of the outcome group with the same title and
    description as the source group, then creates links in that new subgroup to
    the same outcomes that are linked in the source group. Recurses on the
    subgroups of the source group, importing them each in turn into the new
    subgroup.
    
    Allows you to copy organizational structure, but does not create copies of
    the outcomes themselves, only new links.
    
    The source group must be either global, from the same context as this
    outcome group, or from an associated account. The source group cannot be
    the root outcome group of its context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param source_outcome_group_id: (required) The ID of the source outcome group.
        :type source_outcome_group_id: integer
        :return: Import an outcome group
        :rtype: requests.Response (with OutcomeGroup data)

    """

    path = '/v1/courses/{course_id}/outcome_groups/{id}/import'
    payload = {
        'source_outcome_group_id': source_outcome_group_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


