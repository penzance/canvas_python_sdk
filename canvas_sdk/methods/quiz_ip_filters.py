from canvas_sdk import client, utils


def get_available_quiz_ip_filters(request_ctx, course_id, quiz_id, **request_kwargs):
    """
    Get a list of available IP filters for this Quiz.
    
    <b>200 OK</b> response code is returned if the request was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :return: Get available quiz IP filters.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters'
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


