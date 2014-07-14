from canvas_sdk import client, utils

def list_external_feeds_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the list of External Feeds this course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List external feeds
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/external_feeds'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_external_feeds_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Returns the list of External Feeds this course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List external feeds
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/external_feeds'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_external_feed_courses(request_ctx, course_id, url, verbosity, header_match=None, **request_kwargs):
    """
    Create a new external feed for the course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) The url to the external rss or atom feed
        :type url: string
        :param verbosity: (required) no description
        :type verbosity: string
        :param header_match: (optional) If given, only feed entries that contain this string in their title will be imported
        :type header_match: boolean or None
        :return: Create an external feed
        :rtype: requests.Response (with ExternalFeed data)

    """

    verbosity_types = ('full', 'truncate', 'link_only')
    utils.validate_attr_is_acceptable(verbosity, verbosity_types)
    path = '/v1/courses/{course_id}/external_feeds'
    payload = {
        'url' : url,
        'header_match' : header_match,
        'verbosity' : verbosity,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_external_feed_groups(request_ctx, group_id, url, verbosity, header_match=None, **request_kwargs):
    """
    Create a new external feed for the course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) The url to the external rss or atom feed
        :type url: string
        :param verbosity: (required) no description
        :type verbosity: string
        :param header_match: (optional) If given, only feed entries that contain this string in their title will be imported
        :type header_match: boolean or None
        :return: Create an external feed
        :rtype: requests.Response (with ExternalFeed data)

    """

    verbosity_types = ('full', 'truncate', 'link_only')
    utils.validate_attr_is_acceptable(verbosity, verbosity_types)
    path = '/v1/groups/{group_id}/external_feeds'
    payload = {
        'url' : url,
        'header_match' : header_match,
        'verbosity' : verbosity,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_external_feed_courses(request_ctx, course_id, external_feed_id, **request_kwargs):
    """
    Deletes the external feed.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param external_feed_id: (required) ID
        :type external_feed_id: string
        :return: Delete an external feed
        :rtype: requests.Response (with ExternalFeed data)

    """

    path = '/v1/courses/{course_id}/external_feeds/{external_feed_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, external_feed_id=external_feed_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_external_feed_groups(request_ctx, group_id, external_feed_id, **request_kwargs):
    """
    Deletes the external feed.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param external_feed_id: (required) ID
        :type external_feed_id: string
        :return: Delete an external feed
        :rtype: requests.Response (with ExternalFeed data)

    """

    path = '/v1/groups/{group_id}/external_feeds/{external_feed_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, external_feed_id=external_feed_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


