from canvas_sdk import client, utils

def list_poll_choices_in_poll(request_ctx, poll_id, **request_kwargs):
    """
    Returns the list of PollChoices in this poll.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :return: List poll choices in a poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_choices'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_poll_choice(request_ctx, poll_id, id, **request_kwargs):
    """
    Returns the poll choice with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single poll choice
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_choices/{id}'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_poll_choice(request_ctx, poll_id, poll_choices_text, poll_choices_is_correct=None, poll_choices_position=None, **request_kwargs):
    """
    Create a new poll choice for this poll

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param poll_choices_text: (required) The descriptive text of the poll choice.
        :type poll_choices_text: string
        :param poll_choices_is_correct: (optional) Whether this poll choice is considered correct or not. Defaults to false.
        :type poll_choices_is_correct: boolean or None
        :param poll_choices_position: (optional) The order this poll choice should be returned in the context it's sibling poll choices.
        :type poll_choices_position: integer or None
        :return: Create a single poll choice
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_choices'
    payload = {
        'poll_choices[text]' : poll_choices_text,
        'poll_choices[is_correct]' : poll_choices_is_correct,
        'poll_choices[position]' : poll_choices_position,
    }
    url = request_ctx.base_api_url + path.format(poll_id=poll_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_single_poll_choice(request_ctx, poll_id, id, poll_choices_text, poll_choices_is_correct=None, poll_choices_position=None, **request_kwargs):
    """
    Update an existing poll choice for this poll

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :param poll_choices_text: (required) The descriptive text of the poll choice.
        :type poll_choices_text: string
        :param poll_choices_is_correct: (optional) Whether this poll choice is considered correct or not. Defaults to false.
        :type poll_choices_is_correct: boolean or None
        :param poll_choices_position: (optional) The order this poll choice should be returned in the context it's sibling poll choices.
        :type poll_choices_position: integer or None
        :return: Update a single poll choice
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_choices/{id}'
    payload = {
        'poll_choices[text]' : poll_choices_text,
        'poll_choices[is_correct]' : poll_choices_is_correct,
        'poll_choices[position]' : poll_choices_position,
    }
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_poll_choice(request_ctx, poll_id, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param poll_id: (required) ID
        :type poll_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a poll choice
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{poll_id}/poll_choices/{id}'
    url = request_ctx.base_api_url + path.format(poll_id=poll_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


