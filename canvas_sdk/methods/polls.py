from canvas_sdk import client, utils


def list_polls(request_ctx, per_page=None, **request_kwargs):
    """
    Returns the list of polls for the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List polls
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/polls'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_poll(request_ctx, id, **request_kwargs):
    """
    Returns the poll with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get a single poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_poll(request_ctx, polls_question, polls_description=None, **request_kwargs):
    """
    Create a new poll for the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param polls_question: (required) The title of the poll.
        :type polls_question: array
        :param polls_description: (optional) A brief description or instructions for the poll.
        :type polls_description: array or None
        :return: Create a single poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls'
    payload = {
        'polls[question][]': polls_question,
        'polls[description][]': polls_description,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_single_poll(request_ctx, id, polls_question, polls_description=None, **request_kwargs):
    """
    Update an existing poll belonging to the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param polls_question: (required) The title of the poll.
        :type polls_question: array
        :param polls_description: (optional) A brief description or instructions for the poll.
        :type polls_description: array or None
        :return: Update a single poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{id}'
    payload = {
        'polls[question][]': polls_question,
        'polls[description][]': polls_description,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_poll(request_ctx, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete a poll
        :rtype: requests.Response (with void data)

    """

    path = '/v1/polls/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


