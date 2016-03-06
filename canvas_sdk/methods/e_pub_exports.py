from canvas_sdk import client, utils

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


