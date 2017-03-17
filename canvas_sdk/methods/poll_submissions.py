from canvas_sdk import client, utils


def get_single_poll_submission(request_ctx, poll_id, poll_session_id, id, **request_kwargs):
    """
    Returns the poll submission with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param poll_session_id: (required) ID
        :type poll_session_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single poll submission
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id}'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, poll_session_id=poll_session_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_poll_submission(request_ctx, poll_id, poll_session_id, poll_submissions_poll_choice_id, **request_kwargs):
    """
    Create a new poll submission for this poll session

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param poll_session_id: (required) ID
        :type poll_session_id: string
        :param poll_submissions_poll_choice_id: (required) The chosen poll choice for this submission.
        :type poll_submissions_poll_choice_id: array
        :return: Create a single poll submission
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions'
    payload = {
        'poll_submissions[poll_choice_id][]': poll_submissions_poll_choice_id,
    }
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, poll_session_id=poll_session_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


