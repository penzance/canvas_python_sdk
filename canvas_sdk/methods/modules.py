from canvas_sdk import client, utils


def list_modules(request_ctx, course_id, include=None, search_term=None, student_id=None, per_page=None, **request_kwargs):
    """
    List the modules in a course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) - "items": Return module items inline if possible.
  This parameter suggests that Canvas return module items directly
  in the Module object JSON, to avoid having to make separate API
  requests for each module when enumerating modules and items. Canvas
  is free to omit 'items' for any particular module if it deems them
  too numerous to return inline. Callers must be prepared to use the
  {api:ContextModuleItemsApiController#index List Module Items API}
  if items are not returned.
- "content_details": Requires include['items']. Returns additional
  details with module items specific to their associated content items.
  Includes standard lock information for each item.
        :type include: array or None
        :param search_term: (optional) The partial name of the modules (and module items, if include['items'] is
specified) to match and return.
        :type search_term: string or None
        :param student_id: (optional) Returns module completion information for the student with this id.
        :type student_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List modules
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('items', 'content_details')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/modules'
    payload = {
        'include': include,
        'search_term': search_term,
        'student_id': student_id,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_module(request_ctx, course_id, id, include=None, student_id=None, **request_kwargs):
    """
    Get information about a single module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) - "items": Return module items inline if possible.
  This parameter suggests that Canvas return module items directly
  in the Module object JSON, to avoid having to make separate API
  requests for each module when enumerating modules and items. Canvas
  is free to omit 'items' for any particular module if it deems them
  too numerous to return inline. Callers must be prepared to use the
  {api:ContextModuleItemsApiController#index List Module Items API}
  if items are not returned.
- "content_details": Requires include['items']. Returns additional
  details with module items specific to their associated content items.
  Includes standard lock information for each item.
        :type include: array or None
        :param student_id: (optional) Returns module completion information for the student with this id.
        :type student_id: string or None
        :return: Show module
        :rtype: requests.Response (with Module data)

    """

    include_types = ('items', 'content_details')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/modules/{id}'
    payload = {
        'include': include,
        'student_id': student_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_module(request_ctx, course_id, module_name, module_unlock_at=None, module_position=None, module_require_sequential_progress=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, **request_kwargs):
    """
    Create and return a new module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_name: (required) The name of the module
        :type module_name: string
        :param module_unlock_at: (optional) The date the module will unlock
        :type module_unlock_at: DateTime or None
        :param module_position: (optional) The position of this module in the course (1-based)
        :type module_position: integer or None
        :param module_require_sequential_progress: (optional) Whether module items must be unlocked in order
        :type module_require_sequential_progress: boolean or None
        :param module_prerequisite_module_ids: (optional) IDs of Modules that must be completed before this one is unlocked.
Prerequisite modules must precede this module (i.e. have a lower position
value), otherwise they will be ignored
        :type module_prerequisite_module_ids: array or None
        :param module_publish_final_grade: (optional) Whether to publish the student's final grade for the course upon
completion of this module.
        :type module_publish_final_grade: boolean or None
        :return: Create a module
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules'
    payload = {
        'module[name]': module_name,
        'module[unlock_at]': module_unlock_at,
        'module[position]': module_position,
        'module[require_sequential_progress]': module_require_sequential_progress,
        'module[prerequisite_module_ids]': module_prerequisite_module_ids,
        'module[publish_final_grade]': module_publish_final_grade,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_module(request_ctx, course_id, id, module_name=None, module_unlock_at=None, module_position=None, module_require_sequential_progress=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, module_published=None, **request_kwargs):
    """
    Update and return an existing module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param module_name: (optional) The name of the module
        :type module_name: string or None
        :param module_unlock_at: (optional) The date the module will unlock
        :type module_unlock_at: DateTime or None
        :param module_position: (optional) The position of the module in the course (1-based)
        :type module_position: integer or None
        :param module_require_sequential_progress: (optional) Whether module items must be unlocked in order
        :type module_require_sequential_progress: boolean or None
        :param module_prerequisite_module_ids: (optional) IDs of Modules that must be completed before this one is unlocked
Prerequisite modules must precede this module (i.e. have a lower position
value), otherwise they will be ignored
        :type module_prerequisite_module_ids: array or None
        :param module_publish_final_grade: (optional) Whether to publish the student's final grade for the course upon
completion of this module.
        :type module_publish_final_grade: boolean or None
        :param module_published: (optional) Whether the module is published and visible to students
        :type module_published: boolean or None
        :return: Update a module
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules/{id}'
    payload = {
        'module[name]': module_name,
        'module[unlock_at]': module_unlock_at,
        'module[position]': module_position,
        'module[require_sequential_progress]': module_require_sequential_progress,
        'module[prerequisite_module_ids]': module_prerequisite_module_ids,
        'module[publish_final_grade]': module_publish_final_grade,
        'module[published]': module_published,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_module(request_ctx, course_id, id, **request_kwargs):
    """
    Delete a module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete module
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def re_lock_module_progressions(request_ctx, course_id, id, **request_kwargs):
    """
    Resets module progressions to their default locked state and
    recalculates them based on the current requirements.
    
    Adding progression requirements to an active course will not lock students
    out of modules they have already unlocked unless this action is called.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Re-lock module progressions
        :rtype: requests.Response (with Module data)

    """

    path = '/v1/courses/{course_id}/modules/{id}/relock'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def list_module_items(request_ctx, course_id, module_id, include=None, search_term=None, student_id=None, per_page=None, **request_kwargs):
    """
    List the items in a module

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param include: (optional) If included, will return additional details specific to the content
associated with each item. Refer to the {api:Modules:Module%20Item Module
Item specification} for more details.
Includes standard lock information for each item.
        :type include: array or None
        :param search_term: (optional) The partial title of the items to match and return.
        :type search_term: string or None
        :param student_id: (optional) Returns module completion information for the student with this id.
        :type student_id: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List module items
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('content_details')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/modules/{module_id}/items'
    payload = {
        'include': include,
        'search_term': search_term,
        'student_id': student_id,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_module_item(request_ctx, course_id, module_id, id, include=None, student_id=None, **request_kwargs):
    """
    Get information about a single module item

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) If included, will return additional details specific to the content
associated with this item. Refer to the {api:Modules:Module%20Item Module
Item specification} for more details.
Includes standard lock information for each item.
        :type include: array or None
        :param student_id: (optional) Returns module completion information for the student with this id.
        :type student_id: string or None
        :return: Show module item
        :rtype: requests.Response (with ModuleItem data)

    """

    include_types = ('content_details')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}'
    payload = {
        'include': include,
        'student_id': student_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_module_item(request_ctx, course_id, module_id, module_item_type, module_item_content_id, module_item_title=None, module_item_position=None, module_item_indent=None, module_item_page_url=None, module_item_external_url=None, module_item_new_tab=None, module_item_completion_requirement_type=None, module_item_completion_requirement_min_score=None, **request_kwargs):
    """
    Create and return a new module item

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param module_item_type: (required) The type of content linked to the item
        :type module_item_type: string
        :param module_item_content_id: (required) The id of the content to link to the module item. Required, except for
'ExternalUrl', 'Page', and 'SubHeader' types.
        :type module_item_content_id: string
        :param module_item_title: (optional) The name of the module item and associated content
        :type module_item_title: string or None
        :param module_item_position: (optional) The position of this item in the module (1-based).
        :type module_item_position: integer or None
        :param module_item_indent: (optional) 0-based indent level; module items may be indented to show a hierarchy
        :type module_item_indent: integer or None
        :param module_item_page_url: (optional) Suffix for the linked wiki page (e.g. 'front-page'). Required for 'Page'
type.
        :type module_item_page_url: string or None
        :param module_item_external_url: (optional) External url that the item points to. [Required for 'ExternalUrl' and
'ExternalTool' types.
        :type module_item_external_url: string or None
        :param module_item_new_tab: (optional) Whether the external tool opens in a new tab. Only applies to
'ExternalTool' type.
        :type module_item_new_tab: boolean or None
        :param module_item_completion_requirement_type: (optional) Completion requirement for this module item.
"must_view": Applies to all item types
"must_contribute": Only applies to "Assignment", "Discussion", and "Page" types
"must_submit", "min_score": Only apply to "Assignment" and "Quiz" types
Inapplicable types will be ignored
        :type module_item_completion_requirement_type: string or None
        :param module_item_completion_requirement_min_score: (optional) Minimum score required to complete. Required for completion_requirement
type 'min_score'.
        :type module_item_completion_requirement_min_score: integer or None
        :return: Create a module item
        :rtype: requests.Response (with ModuleItem data)

    """

    module_item_type_types = ('File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool')
    module_item_completion_requirement_type_types = ('must_view', 'must_contribute', 'must_submit')
    utils.validate_attr_is_acceptable(module_item_type, module_item_type_types)
    utils.validate_attr_is_acceptable(module_item_completion_requirement_type, module_item_completion_requirement_type_types)
    path = '/v1/courses/{course_id}/modules/{module_id}/items'
    payload = {
        'module_item[title]': module_item_title,
        'module_item[type]': module_item_type,
        'module_item[content_id]': module_item_content_id,
        'module_item[position]': module_item_position,
        'module_item[indent]': module_item_indent,
        'module_item[page_url]': module_item_page_url,
        'module_item[external_url]': module_item_external_url,
        'module_item[new_tab]': module_item_new_tab,
        'module_item[completion_requirement][type]': module_item_completion_requirement_type,
        'module_item[completion_requirement][min_score]': module_item_completion_requirement_min_score,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_module_item(request_ctx, course_id, module_id, id, module_item_title=None, module_item_position=None, module_item_indent=None, module_item_external_url=None, module_item_new_tab=None, module_item_completion_requirement_type=None, module_item_completion_requirement_min_score=None, module_item_published=None, module_item_module_id=None, **request_kwargs):
    """
    Update and return an existing module item

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :param module_item_title: (optional) The name of the module item
        :type module_item_title: string or None
        :param module_item_position: (optional) The position of this item in the module (1-based)
        :type module_item_position: integer or None
        :param module_item_indent: (optional) 0-based indent level; module items may be indented to show a hierarchy
        :type module_item_indent: integer or None
        :param module_item_external_url: (optional) External url that the item points to. Only applies to 'ExternalUrl' type.
        :type module_item_external_url: string or None
        :param module_item_new_tab: (optional) Whether the external tool opens in a new tab. Only applies to
'ExternalTool' type.
        :type module_item_new_tab: boolean or None
        :param module_item_completion_requirement_type: (optional) Completion requirement for this module item.
"must_view": Applies to all item types
"must_contribute": Only applies to "Assignment", "Discussion", and "Page" types
"must_submit", "min_score": Only apply to "Assignment" and "Quiz" types
Inapplicable types will be ignored
        :type module_item_completion_requirement_type: string or None
        :param module_item_completion_requirement_min_score: (optional) Minimum score required to complete, Required for completion_requirement
type 'min_score'.
        :type module_item_completion_requirement_min_score: integer or None
        :param module_item_published: (optional) Whether the module item is published and visible to students.
        :type module_item_published: boolean or None
        :param module_item_module_id: (optional) Move this item to another module by specifying the target module id here.
The target module must be in the same course.
        :type module_item_module_id: string or None
        :return: Update a module item
        :rtype: requests.Response (with ModuleItem data)

    """

    module_item_completion_requirement_type_types = ('must_view', 'must_contribute', 'must_submit')
    utils.validate_attr_is_acceptable(module_item_completion_requirement_type, module_item_completion_requirement_type_types)
    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}'
    payload = {
        'module_item[title]': module_item_title,
        'module_item[position]': module_item_position,
        'module_item[indent]': module_item_indent,
        'module_item[external_url]': module_item_external_url,
        'module_item[new_tab]': module_item_new_tab,
        'module_item[completion_requirement][type]': module_item_completion_requirement_type,
        'module_item[completion_requirement][min_score]': module_item_completion_requirement_min_score,
        'module_item[published]': module_item_published,
        'module_item[module_id]': module_item_module_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def select_mastery_path(request_ctx, course_id, module_id, id, assignment_set_id=None, student_id=None, **request_kwargs):
    """
    Select a mastery path when module item includes several possible paths.
    Requires Mastery Paths feature to be enabled.  Returns a compound document
    with the assignments included in the given path and any module items
    related to those assignments

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :param assignment_set_id: (optional) Assignment set chosen, as specified in the mastery_paths portion of the
context module item response
        :type assignment_set_id: string or None
        :param student_id: (optional) Which student the selection applies to.  If not specified, current user is
implied.
        :type student_id: string or None
        :return: Select a mastery path
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path'
    payload = {
        'assignment_set_id': assignment_set_id,
        'student_id': student_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_module_item(request_ctx, course_id, module_id, id, **request_kwargs):
    """
    Delete a module item

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete module item
        :rtype: requests.Response (with ModuleItem data)

    """

    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def mark_module_item_as_done_not_done(request_ctx, course_id, module_id, id, **request_kwargs):
    """
    Mark a module item as done/not done. Use HTTP method PUT to mark as done,
    and DELETE to mark as not done.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :return: Mark module item as done/not done
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}/done'
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def get_module_item_sequence(request_ctx, course_id, asset_type=None, asset_id=None, **request_kwargs):
    """
    Given an asset in a course, find the ModuleItem it belongs to, and also the previous and next Module Items
    in the course sequence.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param asset_type: (optional) The type of asset to find module sequence information for. Use the ModuleItem if it is known
(e.g., the user navigated from a module item), since this will avoid ambiguity if the asset
appears more than once in the module sequence.
        :type asset_type: string or None
        :param asset_id: (optional) The id of the asset (or the url in the case of a Page)
        :type asset_id: integer or None
        :return: Get module item sequence
        :rtype: requests.Response (with ModuleItemSequence data)

    """

    asset_type_types = ('ModuleItem', 'File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'ExternalTool')
    utils.validate_attr_is_acceptable(asset_type, asset_type_types)
    path = '/v1/courses/{course_id}/module_item_sequence'
    payload = {
        'asset_type': asset_type,
        'asset_id': asset_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_module_item_read(request_ctx, course_id, module_id, id, **request_kwargs):
    """
    Fulfills "must view" requirement for a module item. It is generally not necessary to do this explicitly,
    but it is provided for applications that need to access external content directly (bypassing the html_url
    redirect that normally allows Canvas to fulfill "must view" requirements).
    
    This endpoint cannot be used to complete requirements on locked or unpublished module items.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param module_id: (required) ID
        :type module_id: string
        :param id: (required) ID
        :type id: string
        :return: Mark module item read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read'
    url = request_ctx.base_api_url + path.format(course_id=course_id, module_id=module_id, id=id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


