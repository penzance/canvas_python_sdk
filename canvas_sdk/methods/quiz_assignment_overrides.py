from __future__ import unicode_literals
from canvas_sdk import client, utils

def retrieve_assignment_overridden_dates_for_quizzes(request_ctx, course_id, quiz_assignment_overrides_0_quiz_ids=None, per_page=None, **request_kwargs):
    """
    Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
    based on the assignment overrides active for the current API user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_assignment_overrides_0_quiz_ids: (optional) An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned.
        :type quiz_assignment_overrides_0_quiz_ids: integer or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Retrieve assignment-overridden dates for quizzes
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/quizzes/assignment_overrides'
    payload = {
        'quiz_assignment_overrides[0][quiz_ids]' : quiz_assignment_overrides_0_quiz_ids,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


