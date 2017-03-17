from canvas_sdk import client, utils


def list_courses_with_their_latest_epub_export(request_ctx, per_page=None, **request_kwargs):
    """
    Lists all courses a user is actively participating in,
    and the latest ePub export associated with the user & course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List courses with their latest ePub export
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/epub_exports'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_epub_export(request_ctx, course_id, **request_kwargs):
    """
    Begin an ePub export for a course.
    
    You can use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_ to track the
    progress of the export. The export's progress is linked to with the
    _progress_url_ value.
    
    When the export completes, use the `EpubExportsController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/epub_exports_controller.rb>`_ endpoint
    to retrieve a download URL for the exported content.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Create ePub Export
        :rtype: requests.Response (with EpubExport data)

    """

    path = '/v1/courses/{course_id}/epub_exports'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def show_epub_export(request_ctx, course_id, id, **request_kwargs):
    """
    Get information about a single ePub export.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Show ePub export
        :rtype: requests.Response (with EpubExport data)

    """

    path = '/v1/courses/{course_id}/epub_exports/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


