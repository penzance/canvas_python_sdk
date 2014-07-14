from canvas_sdk import client, utils

def set_extensions_for_student_quiz_submissions(request_ctx, course_id, quiz_id, user_id, extra_attempts=None, extra_time=None, manually_unlocked=None, extend_from_now=None, extend_from_end_at=None, **request_kwargs):
    """
    <b>Responses</b>
    
    * <b>200 OK</b> if the request was successful
    * <b>403 Forbidden</b> if you are not allowed to extend quizzes for this course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param user_id: (required) The ID of the user we want to add quiz extensions for.
        :type user_id: integer
        :param extra_attempts: (optional) Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less.
        :type extra_attempts: integer or None
        :param extra_time: (optional) The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week)
        :type extra_time: integer or None
        :param manually_unlocked: (optional) Allow the student to take the quiz even if it's locked for everyone else.
        :type manually_unlocked: boolean or None
        :param extend_from_now: (optional) The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend_from_end_at. This is limited to 1440 minutes (24 hours)
        :type extend_from_now: integer or None
        :param extend_from_end_at: (optional) The number of minutes to extend the quiz beyond the quiz's current ending time. This is mutually exclusive to extend_from_now. This is limited to 1440 minutes (24 hours)
        :type extend_from_end_at: integer or None
        :return: Set extensions for student quiz submissions
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/extensions'
    payload = {
        'user_id' : user_id,
        'extra_attempts' : extra_attempts,
        'extra_time' : extra_time,
        'manually_unlocked' : manually_unlocked,
        'extend_from_now' : extend_from_now,
        'extend_from_end_at' : extend_from_end_at,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


