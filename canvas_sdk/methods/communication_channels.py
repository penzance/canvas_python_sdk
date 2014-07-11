from canvas_sdk import client, utils

def list_user_communication_channels(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Returns a list of communication channels for the specified user, sorted by
    position.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List user communication channels
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/communication_channels'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_communication_channel(request_ctx, user_id, communication_channel_address, communication_channel_type, skip_confirmation=None, **request_kwargs):
    """
    Creates a new communication channel for the specified user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param communication_channel_address: (required) An email address or SMS number.
        :type communication_channel_address: string
        :param communication_channel_type: (required) The type of communication channel. In order to enable push notification support, the server must be properly configured (via sns.yml) to communicate with Amazon Simple Notification Services, and the developer key used to create the access token from this request must have an SNS ARN configured on it.
        :type communication_channel_type: string
        :param skip_confirmation: (optional) Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.
        :type skip_confirmation: boolean or None
        :return: Create a communication channel
        :rtype: requests.Response (with CommunicationChannel data)

    """

    communication_channel_type_types = ('email', 'sms', 'push')
    utils.validate_attr_is_acceptable(communication_channel_type, communication_channel_type_types)
    path = '/v1/users/{user_id}/communication_channels'
    payload = {
        'communication_channel[address]' : communication_channel_address,
        'communication_channel[type]' : communication_channel_type,
        'skip_confirmation' : skip_confirmation,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_communication_channel_id(request_ctx, user_id, id, **request_kwargs):
    """
    Delete an existing communication channel.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a communication channel
        :rtype: requests.Response (with CommunicationChannel data)

    """

    path = '/v1/users/{user_id}/communication_channels/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_communication_channel_type(request_ctx, user_id, type, address, **request_kwargs):
    """
    Delete an existing communication channel.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param type: (required) ID
        :type type: string
        :param address: (required) ID
        :type address: string
        :return: Delete a communication channel
        :rtype: requests.Response (with CommunicationChannel data)

    """

    path = '/v1/users/{user_id}/communication_channels/{type}/{address}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, type=type, address=address)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


