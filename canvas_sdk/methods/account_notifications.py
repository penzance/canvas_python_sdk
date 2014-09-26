from canvas_sdk import client, utils

def create_global_notification(request_ctx, account_id, account_notification_subject=None, account_notification_message=None, account_notification_start_at=None, account_notification_end_at=None, account_notification_icon=None, account_notification_roles=None, **request_kwargs):
    """
    Create and return a new global notification for an account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param account_notification_subject: (optional) The subject of the notification.
        :type account_notification_subject: string or None
        :param account_notification_message: (optional) The message body of the notification.
        :type account_notification_message: string or None
        :param account_notification_start_at: (optional) The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z
        :type account_notification_start_at: datetime or None
        :param account_notification_end_at: (optional) The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z
        :type account_notification_end_at: datetime or None
        :param account_notification_icon: (optional) The icon to display with the notification. Note: Defaults to warning.
        :type account_notification_icon: string or None
        :param account_notification_roles: (optional) The role(s) to send global notification to. Note: ommitting this field will send to everyone Example: account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"]
        :type account_notification_roles: string or None
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


