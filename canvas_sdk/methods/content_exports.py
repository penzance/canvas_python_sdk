from canvas_sdk import client, utils

def list_content_exports_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    List the past and pending content export jobs for a course, group, or user.
    Exports are returned newest first.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content exports
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/content_exports'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_exports_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    List the past and pending content export jobs for a course, group, or user.
    Exports are returned newest first.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content exports
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/content_exports'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_content_exports_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    List the past and pending content export jobs for a course, group, or user.
    Exports are returned newest first.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List content exports
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/content_exports'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_content_export_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Get information about a single content export.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Show content export
        :rtype: requests.Response (with ContentExport data)

    """

    path = '/v1/courses/{course_id}/content_exports/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_content_export_groups(request_ctx, group_id, id, **request_kwargs):
    """
    Get information about a single content export.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param id: (required) ID
        :type id: string
        :return: Show content export
        :rtype: requests.Response (with ContentExport data)

    """

    path = '/v1/groups/{group_id}/content_exports/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_content_export_users(request_ctx, user_id, id, **request_kwargs):
    """
    Get information about a single content export.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Show content export
        :rtype: requests.Response (with ContentExport data)

    """

    path = '/v1/users/{user_id}/content_exports/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def export_content_courses(request_ctx, course_id, export_type, skip_notifications=None, **request_kwargs):
    """
    Begin a content export job for a course, group, or user.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the export. The migration's progress is linked to with the
    _progress_url_ value.
    
    When the export completes, use the `ContentExportsApiController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb>`_ endpoint
    to retrieve a download URL for the exported content.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param export_type: (required) "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
"qti":: Export quizzes from a course in the QTI format
"zip":: Export files from a course, group, or user in a zip file
        :type export_type: string
        :param skip_notifications: (optional) Don't send the notifications about the export to the user. Default: false
        :type skip_notifications: boolean or None
        :return: Export content
        :rtype: requests.Response (with ContentExport data)

    """

    export_type_types = ('common_cartridge', 'qti', 'zip')
    utils.validate_attr_is_acceptable(export_type, export_type_types)
    path = '/v1/courses/{course_id}/content_exports'
    payload = {
        'export_type' : export_type,
        'skip_notifications' : skip_notifications,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def export_content_groups(request_ctx, group_id, export_type, skip_notifications=None, **request_kwargs):
    """
    Begin a content export job for a course, group, or user.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the export. The migration's progress is linked to with the
    _progress_url_ value.
    
    When the export completes, use the `ContentExportsApiController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb>`_ endpoint
    to retrieve a download URL for the exported content.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param export_type: (required) "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
"qti":: Export quizzes from a course in the QTI format
"zip":: Export files from a course, group, or user in a zip file
        :type export_type: string
        :param skip_notifications: (optional) Don't send the notifications about the export to the user. Default: false
        :type skip_notifications: boolean or None
        :return: Export content
        :rtype: requests.Response (with ContentExport data)

    """

    export_type_types = ('common_cartridge', 'qti', 'zip')
    utils.validate_attr_is_acceptable(export_type, export_type_types)
    path = '/v1/groups/{group_id}/content_exports'
    payload = {
        'export_type' : export_type,
        'skip_notifications' : skip_notifications,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def export_content_users(request_ctx, user_id, export_type, skip_notifications=None, **request_kwargs):
    """
    Begin a content export job for a course, group, or user.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the export. The migration's progress is linked to with the
    _progress_url_ value.
    
    When the export completes, use the `ContentExportsApiController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb>`_ endpoint
    to retrieve a download URL for the exported content.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param export_type: (required) "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
"qti":: Export quizzes from a course in the QTI format
"zip":: Export files from a course, group, or user in a zip file
        :type export_type: string
        :param skip_notifications: (optional) Don't send the notifications about the export to the user. Default: false
        :type skip_notifications: boolean or None
        :return: Export content
        :rtype: requests.Response (with ContentExport data)

    """

    export_type_types = ('common_cartridge', 'qti', 'zip')
    utils.validate_attr_is_acceptable(export_type, export_type_types)
    path = '/v1/users/{user_id}/content_exports'
    payload = {
        'export_type' : export_type,
        'skip_notifications' : skip_notifications,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


