from canvas_sdk import client, utils

def index_of_active_global_notification_for_user(request_ctx, account_id, user_id, per_page=None, **request_kwargs):
    """
    Returns a list of all global notifications in the account for this user
    Any notifications that have been closed by the user will not be returned

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Index of active global notification for the user
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/users/{user_id}/account_notifications'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def close_notification_for_user(request_ctx, account_id, user_id, id, **request_kwargs):
    """
    If the user no long wants to see this notification it can be excused with this call

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Close notification for user
        :rtype: requests.Response (with AccountNotification data)

    """

    path = '/v1/accounts/{account_id}/users/{user_id}/account_notifications/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, user_id=user_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def create_global_notification(request_ctx, account_id, account_notification_subject, account_notification_message, account_notification_start_at, account_notification_end_at, account_notification_icon=None, account_notification_roles=None, **request_kwargs):
    """
    Create and return a new global notification for an account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param account_notification_subject: (required) The subject of the notification.
        :type account_notification_subject: string
        :param account_notification_message: (required) The message body of the notification.
        :type account_notification_message: string
        :param account_notification_start_at: (required) The start date and time of the notification in ISO8601 format.
e.g. 2014-01-01T01:00Z
        :type account_notification_start_at: DateTime
        :param account_notification_end_at: (required) The end date and time of the notification in ISO8601 format.
e.g. 2014-01-01T01:00Z
        :type account_notification_end_at: DateTime
        :param account_notification_icon: (optional) The icon to display with the notification.
Note: Defaults to warning.
        :type account_notification_icon: string or None
        :param account_notification_roles: (optional) The role(s) to send global notification to.  Note:  ommitting this field will send to everyone
Example:
  account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"]
        :type account_notification_roles: array or None
        :return: Create a global notification
        :rtype: requests.Response (with void data)

    """

    account_notification_icon_types = ('warning', 'information', 'question', 'error', 'calendar')
    utils.validate_attr_is_acceptable(account_notification_icon, account_notification_icon_types)
    path = '/v1/accounts/{account_id}/account_notifications'
    payload = {
        'account_notification[subject]' : account_notification_subject,
        'account_notification[message]' : account_notification_message,
        'account_notification[start_at]' : account_notification_start_at,
        'account_notification[end_at]' : account_notification_end_at,
        'account_notification[icon]' : account_notification_icon,
        'account_notification_roles' : account_notification_roles,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


