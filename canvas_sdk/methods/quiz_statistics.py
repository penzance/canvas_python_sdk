from canvas_sdk import client, utils

def fetching_latest_quiz_statistics(request_ctx, course_id, quiz_id, all_versions=None, **request_kwargs):
    """
    This endpoint provides statistics for all quiz versions, or for a specific
    quiz version, in which case the output is guaranteed to represent the
    _latest_ and most current version of the quiz.
    
    <b>200 OK</b> response code is returned if the request was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param all_versions: (optional) Whether the statistics report should include all submissions attempts.
        :type all_versions: boolean or None
        :return: Fetching the latest quiz statistics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/statistics'
    payload = {
        'all_versions' : all_versions,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


