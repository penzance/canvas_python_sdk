from __future__ import unicode_literals
from canvas_sdk import client, utils

def list_poll_sessions_for_poll(request_ctx, poll_id, **request_kwargs):
    """
    Returns the list of PollSessions in this poll.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :return: List poll sessions for a poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_results_for_single_poll_session(request_ctx, poll_id, id, **request_kwargs):
    """
    Returns the poll session with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Get the results for a single poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{id}'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_poll_session(request_ctx, poll_id, poll_sessions_course_id, poll_sessions_course_section_id=None, poll_sessions_has_public_results=None, **request_kwargs):
    """
    Create a new poll session for this poll

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param poll_sessions_course_id: (required) The id of the course this session is associated with.
        :type poll_sessions_course_id: integer
        :param poll_sessions_course_section_id: (optional) The id of the course section this session is associated with.
        :type poll_sessions_course_section_id: integer or None
        :param poll_sessions_has_public_results: (optional) Whether or not results are viewable by students.
        :type poll_sessions_has_public_results: boolean or None
        :return: Create a single poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions'
    payload = {
        'poll_sessions[course_id]' : poll_sessions_course_id,
        'poll_sessions[course_section_id]' : poll_sessions_course_section_id,
        'poll_sessions[has_public_results]' : poll_sessions_has_public_results,
    }
    url = request_ctx.base_api_url + path.format(poll_id=poll_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_single_poll_session(request_ctx, poll_id, id, poll_sessions_course_id, poll_sessions_course_section_id, poll_sessions_has_public_results=None, **request_kwargs):
    """
    Update an existing poll session for this poll

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :param poll_sessions_course_id: (required) The id of the course this session is associated with.
        :type poll_sessions_course_id: integer
        :param poll_sessions_course_section_id: (required) The id of the course section this session is associated with.
        :type poll_sessions_course_section_id: integer
        :param poll_sessions_has_public_results: (optional) Whether or not results are viewable by students.
        :type poll_sessions_has_public_results: boolean or None
        :return: Update a single poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{id}'
    payload = {
        'poll_sessions[course_id]' : poll_sessions_course_id,
        'poll_sessions[course_section_id]' : poll_sessions_course_section_id,
        'poll_sessions[has_public_results]' : poll_sessions_has_public_results,
    }
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_poll_session(request_ctx, poll_id, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{id}'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def open_poll_session(request_ctx, poll_id, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Open a poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{id}/open'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def close_opened_poll_session(request_ctx, poll_id, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Close an opened poll session
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_sessions/{id}/close'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_opened_poll_sessions(request_ctx, **request_kwargs):
    """
    Lists all opened poll sessions available to the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List opened poll sessions
        :rtype: requests.Response (with void data)

    """

    path = '/v1/poll_sessions/opened'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_closed_poll_sessions(request_ctx, **request_kwargs):
    """
    Lists all closed poll sessions available to the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List closed poll sessions
        :rtype: requests.Response (with void data)

    """

    path = '/v1/poll_sessions/closed'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


