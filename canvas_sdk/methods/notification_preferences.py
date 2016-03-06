from canvas_sdk import client, utils

def list_preferences_communication_channel_id(request_ctx, user_id, communication_channel_id, per_page=None, **request_kwargs):
    """
    Fetch all preferences for the given communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List preferences
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, communication_channel_id=communication_channel_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_preferences_type(request_ctx, user_id, type, address, per_page=None, **request_kwargs):
    """
    Fetch all preferences for the given communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param type: (required) ID
        :type type: string
        :param address: (required) ID
        :type address: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List preferences
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, type=type, address=address)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_of_preference_categories(request_ctx, user_id, communication_channel_id, per_page=None, **request_kwargs):
    """
    Fetch all notification preference categories for the given communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List of preference categories
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, communication_channel_id=communication_channel_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_preference_communication_channel_id(request_ctx, user_id, communication_channel_id, notification, **request_kwargs):
    """
    Fetch the preference for the given notification for the given communicaiton channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param notification: (required) ID
        :type notification: string
        :return: Get a preference
        :rtype: requests.Response (with NotificationPreference data)

    """

    path = '/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, communication_channel_id=communication_channel_id, notification=notification)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_preference_type(request_ctx, user_id, type, address, notification, **request_kwargs):
    """
    Fetch the preference for the given notification for the given communicaiton channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param type: (required) ID
        :type type: string
        :param address: (required) ID
        :type address: string
        :param notification: (required) ID
        :type notification: string
        :return: Get a preference
        :rtype: requests.Response (with NotificationPreference data)

    """

    path = '/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, type=type, address=address, notification=notification)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_preference_communication_channel_id(request_ctx, communication_channel_id, notification, notification_preferences_frequency, **request_kwargs):
    """
    Change the preference for a single notification for a single communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param notification: (required) ID
        :type notification: string
        :param notification_preferences_frequency: (required) The desired frequency for this notification
        :type notification_preferences_frequency: string
        :return: Update a preference
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification}'
    payload = {
        'notification_preferences[frequency]' : notification_preferences_frequency,
    }
    url = request_ctx.base_api_url + path.format(communication_channel_id=communication_channel_id, notification=notification)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_preference_type(request_ctx, type, address, notification, notification_preferences_frequency, **request_kwargs):
    """
    Change the preference for a single notification for a single communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param type: (required) ID
        :type type: string
        :param address: (required) ID
        :type address: string
        :param notification: (required) ID
        :type notification: string
        :param notification_preferences_frequency: (required) The desired frequency for this notification
        :type notification_preferences_frequency: string
        :return: Update a preference
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification}'
    payload = {
        'notification_preferences[frequency]' : notification_preferences_frequency,
    }
    url = request_ctx.base_api_url + path.format(type=type, address=address, notification=notification)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_preferences_by_category(request_ctx, communication_channel_id, category, notification_preferences_frequency, **request_kwargs):
    """
    Change the preferences for multiple notifications based on the category for a single communication channel

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param category: (required) The name of the category. Must be parameterized (e.g. The category "Course Content" should be "course_content")
        :type category: string
        :param notification_preferences_frequency: (required) The desired frequency for each notification in the category
        :type notification_preferences_frequency: string
        :return: Update preferences by category
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category}'
    payload = {
        'notification_preferences[frequency]' : notification_preferences_frequency,
    }
    url = request_ctx.base_api_url + path.format(communication_channel_id=communication_channel_id, category=category)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_multiple_preferences_communication_channel_id(request_ctx, communication_channel_id, notification_preferences_X_frequency, **request_kwargs):
    """
    Change the preferences for multiple notifications for a single communication channel at once

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param communication_channel_id: (required) ID
        :type communication_channel_id: string
        :param notification_preferences_X_frequency: (required) The desired frequency for <X> notification
        :type notification_preferences_X_frequency: string
        :return: Update multiple preferences
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences'
    payload = {
        'notification_preferences[X][frequency]' : notification_preferences_X_frequency,
    }
    url = request_ctx.base_api_url + path.format(communication_channel_id=communication_channel_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_multiple_preferences_type(request_ctx, type, address, notification_preferences_X_frequency, **request_kwargs):
    """
    Change the preferences for multiple notifications for a single communication channel at once

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param type: (required) ID
        :type type: string
        :param address: (required) ID
        :type address: string
        :param notification_preferences_X_frequency: (required) The desired frequency for <X> notification
        :type notification_preferences_X_frequency: string
        :return: Update multiple preferences
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/communication_channels/{type}/{address}/notification_preferences'
    payload = {
        'notification_preferences[X][frequency]' : notification_preferences_X_frequency,
    }
    url = request_ctx.base_api_url + path.format(type=type, address=address)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


