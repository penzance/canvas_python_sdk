from __future__ import unicode_literals
from canvas_sdk import client, utils

def find_recipients_conversations(request_ctx, search, context, exclude, type, user_id, from_conversation_id, permissions, **request_kwargs):
    """
    Find valid recipients (users, courses and groups) that the current user
    can send messages to. The /api/v1/search/recipients path is the preferred
    endpoint, /api/v1/conversations/find_recipients is deprecated.
    
    Pagination is supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param search: (required) Search terms used for matching users/courses/groups (e.g. "bob smith"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned.
        :type search: string
        :param context: (required) Limit the search to a particular course/group (e.g. "course_3" or "group_4").
        :type context: string
        :param exclude: (required) Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3
        :type exclude: string
        :param type: (required) Limit the search just to users or contexts (groups/courses).
        :type type: string
        :param user_id: (required) Search for a specific user id. This ignores the other above parameters, and will never return more than one result.
        :type user_id: integer
        :param from_conversation_id: (required) When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations.
        :type from_conversation_id: integer
        :param permissions: (required) Array of permission strings to be checked for each matched context (e.g. "send_messages"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s).
        :type permissions: string
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


def find_recipients_search(request_ctx, search, context, exclude, type, user_id, from_conversation_id, permissions, **request_kwargs):
    """
    Find valid recipients (users, courses and groups) that the current user
    can send messages to. The /api/v1/search/recipients path is the preferred
    endpoint, /api/v1/conversations/find_recipients is deprecated.
    
    Pagination is supported.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param search: (required) Search terms used for matching users/courses/groups (e.g. "bob smith"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned.
        :type search: string
        :param context: (required) Limit the search to a particular course/group (e.g. "course_3" or "group_4").
        :type context: string
        :param exclude: (required) Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3
        :type exclude: string
        :param type: (required) Limit the search just to users or contexts (groups/courses).
        :type type: string
        :param user_id: (required) Search for a specific user id. This ignores the other above parameters, and will never return more than one result.
        :type user_id: integer
        :param from_conversation_id: (required) When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations.
        :type from_conversation_id: integer
        :param permissions: (required) Array of permission strings to be checked for each matched context (e.g. "send_messages"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s).
        :type permissions: string
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


