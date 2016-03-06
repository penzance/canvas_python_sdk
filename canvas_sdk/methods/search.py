from canvas_sdk import client, utils

def find_recipients_conversations(request_ctx, search=None, context=None, exclude=None, type=None, user_id=None, from_conversation_id=None, permissions=None, **request_kwargs):
    """
    Find valid recipients (users, courses and groups) that the current user
    can send messages to. The /api/v1/search/recipients path is the preferred
    endpoint, /api/v1/conversations/find_recipients is deprecated.
    
    Pagination is supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param search: (optional) Search terms used for matching users/courses/groups (e.g. "bob smith"). If
multiple terms are given (separated via whitespace), only results matching
all terms will be returned.
        :type search: string or None
        :param context: (optional) Limit the search to a particular course/group (e.g. "course_3" or "group_4").
        :type context: string or None
        :param exclude: (optional) Array of ids to exclude from the search. These may be user ids or
course/group ids prefixed with "course_" or "group_" respectively,
e.g. exclude[]=1&exclude[]=2&exclude[]=course_3
        :type exclude: array or None
        :param type: (optional) Limit the search just to users or contexts (groups/courses).
        :type type: string or None
        :param user_id: (optional) Search for a specific user id. This ignores the other above parameters,
and will never return more than one result.
        :type user_id: integer or None
        :param from_conversation_id: (optional) When searching by user_id, only users that could be normally messaged by
this user will be returned. This parameter allows you to specify a
conversation that will be referenced for a shared context -- if both the
current user and the searched user are in the conversation, the user will
be returned. This is used to start new side conversations.
        :type from_conversation_id: integer or None
        :param permissions: (optional) Array of permission strings to be checked for each matched context (e.g.
"send_messages"). This argument determines which permissions may be
returned in the response; it won't prevent contexts from being returned if
they don't grant the permission(s).
        :type permissions: array or None
        :return: Find recipients
        :rtype: requests.Response (with void data)

    """

    type_types = ('user', 'context')
    utils.validate_attr_is_acceptable(type, type_types)
    path = '/v1/conversations/find_recipients'
    payload = {
        'search' : search,
        'context' : context,
        'exclude' : exclude,
        'type' : type,
        'user_id' : user_id,
        'from_conversation_id' : from_conversation_id,
        'permissions' : permissions,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def find_recipients_search(request_ctx, search=None, context=None, exclude=None, type=None, user_id=None, from_conversation_id=None, permissions=None, **request_kwargs):
    """
    Find valid recipients (users, courses and groups) that the current user
    can send messages to. The /api/v1/search/recipients path is the preferred
    endpoint, /api/v1/conversations/find_recipients is deprecated.
    
    Pagination is supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param search: (optional) Search terms used for matching users/courses/groups (e.g. "bob smith"). If
multiple terms are given (separated via whitespace), only results matching
all terms will be returned.
        :type search: string or None
        :param context: (optional) Limit the search to a particular course/group (e.g. "course_3" or "group_4").
        :type context: string or None
        :param exclude: (optional) Array of ids to exclude from the search. These may be user ids or
course/group ids prefixed with "course_" or "group_" respectively,
e.g. exclude[]=1&exclude[]=2&exclude[]=course_3
        :type exclude: array or None
        :param type: (optional) Limit the search just to users or contexts (groups/courses).
        :type type: string or None
        :param user_id: (optional) Search for a specific user id. This ignores the other above parameters,
and will never return more than one result.
        :type user_id: integer or None
        :param from_conversation_id: (optional) When searching by user_id, only users that could be normally messaged by
this user will be returned. This parameter allows you to specify a
conversation that will be referenced for a shared context -- if both the
current user and the searched user are in the conversation, the user will
be returned. This is used to start new side conversations.
        :type from_conversation_id: integer or None
        :param permissions: (optional) Array of permission strings to be checked for each matched context (e.g.
"send_messages"). This argument determines which permissions may be
returned in the response; it won't prevent contexts from being returned if
they don't grant the permission(s).
        :type permissions: array or None
        :return: Find recipients
        :rtype: requests.Response (with void data)

    """

    type_types = ('user', 'context')
    utils.validate_attr_is_acceptable(type, type_types)
    path = '/v1/search/recipients'
    payload = {
        'search' : search,
        'context' : context,
        'exclude' : exclude,
        'type' : type,
        'user_id' : user_id,
        'from_conversation_id' : from_conversation_id,
        'permissions' : permissions,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_all_courses(request_ctx, search=None, public_only=None, open_enrollment_only=None, per_page=None, **request_kwargs):
    """
    List all courses visible in the public index

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param search: (optional) Search terms used for matching users/courses/groups (e.g. "bob smith"). If
multiple terms are given (separated via whitespace), only results matching
all terms will be returned.
        :type search: string or None
        :param public_only: (optional) Only return courses with public content. Defaults to false.
        :type public_only: boolean or None
        :param open_enrollment_only: (optional) Only return courses that allow self enrollment. Defaults to false.
        :type open_enrollment_only: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List all courses
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/search/all_courses'
    payload = {
        'search' : search,
        'public_only' : public_only,
        'open_enrollment_only' : open_enrollment_only,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


