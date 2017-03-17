from canvas_sdk import client, utils


def list_announcements(request_ctx, context_codes, start_date=None, end_date=None, active_only=None, per_page=None, **request_kwargs):
    """
    Returns the paginated list of announcements for the given courses and date range.  Note that
    a +context_code+ field is added to the responses so you can tell which course each announcement
    belongs to.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param context_codes: (required) List of context_codes to retrieve announcements for (for example, +course_123+). Only courses
are presently supported. The call will fail unless the caller has View Announcements permission
in all listed courses.
        :type context_codes: array
        :param start_date: (optional) Only return announcements posted since the start_date (inclusive).
Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        :type start_date: Date or None
        :param end_date: (optional) Only return announcements posted before the end_date (inclusive).
Defaults to 28 days from start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
Announcements scheduled for future posting will only be returned to course administrators.
        :type end_date: Date or None
        :param active_only: (optional) Only return active announcements that have been published.
Applies only to requesting users that have permission to view
unpublished items.
Defaults to false for users with access to view unpublished items,
otherwise true and unmodifiable.
        :type active_only: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List announcements
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/announcements'
    payload = {
        'context_codes': context_codes,
        'start_date': start_date,
        'end_date': end_date,
        'active_only': active_only,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


