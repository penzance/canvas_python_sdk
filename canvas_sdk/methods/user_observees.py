from canvas_sdk import client, utils

def list_observees(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    List the users that the given user is observing.
    
    *Note:* all users are allowed to list their own observees. Administrators can list
    other users' observees.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List observees
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/observees'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def add_observee_with_credentials(request_ctx, user_id, observee_unique_id=None, observee_password=None, **request_kwargs):
    """
    Register the given user to observe another user, given the observee's credentials.
    
    *Note:* all users are allowed to add their own observees, given the observee's
    credentials are provided. Administrators can add observees given credentials or
    the `UserObserveesController#update <https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb>`_.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param observee_unique_id: (optional) The login id for the user to observe.
        :type observee_unique_id: string or None
        :param observee_password: (optional) The password for the user to observe.
        :type observee_password: string or None
        :return: Add an observee with credentials
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{user_id}/observees'
    payload = {
        'observee[unique_id]' : observee_unique_id,
        'observee[password]' : observee_password,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_observee(request_ctx, user_id, observee_id, **request_kwargs):
    """
    Gets information about an observed user.
    
    *Note:* all users are allowed to view their own observees.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param observee_id: (required) ID
        :type observee_id: string
        :return: Show an observee
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{user_id}/observees/{observee_id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, observee_id=observee_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def add_observee(request_ctx, user_id, observee_id, **request_kwargs):
    """
    Registers a user as being observed by the given user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param observee_id: (required) ID
        :type observee_id: string
        :return: Add an observee
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{user_id}/observees/{observee_id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, observee_id=observee_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def remove_observee(request_ctx, user_id, observee_id, **request_kwargs):
    """
    Unregisters a user as being observed by the given user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param observee_id: (required) ID
        :type observee_id: string
        :return: Remove an observee
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{user_id}/observees/{observee_id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, observee_id=observee_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


