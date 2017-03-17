from canvas_sdk import client, utils


def submit_captured_events(request_ctx, course_id, quiz_id, id, quiz_submission_events, **request_kwargs):
    """
    Store a set of events which were captured during a quiz taking session.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param quiz_submission_events: (required) The submission events to be recorded
        :type quiz_submission_events: array
        :return: Submit captured events
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events'
    payload = {
        'quiz_submission_events[]': quiz_submission_events,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def retrieve_captured_events(request_ctx, course_id, quiz_id, id, attempt=None, **request_kwargs):
    """
    Retrieve the set of events captured during a specific submission attempt.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param attempt: (optional) The specific submission attempt to look up the events for. If unspecified,
the latest attempt will be used.
        :type attempt: integer or None
        :return: Retrieve captured events
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events'
    payload = {
        'attempt': attempt,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


