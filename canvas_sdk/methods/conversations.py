from canvas_sdk import client, utils

def list_conversations(request_ctx, interleave_submissions, include_all_conversation_ids, scope=None, filter=None, filter_mode=None, per_page=None, **request_kwargs):
    """
    Returns the list of conversations for the current user, most recent ones first.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param interleave_submissions: (required) (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored.
        :type interleave_submissions: boolean
        :param include_all_conversation_ids: (required) Default is false. If true, the top-level element of the response will be an object rather than an array, and will have the keys "conversations" which will contain the paged conversation data, and "conversation_ids" which will contain the ids of all conversations under this scope/filter in the same order.
        :type include_all_conversation_ids: boolean
        :param scope: (optional) When set, only return conversations of the specified type. For example, set to "unread" to return only conversations that haven't been read. The default behavior is to return all non-archived conversations (i.e. read and unread).
        :type scope: string or None
        :param filter: (optional) When set, only return conversations for the specified courses, groups or users. The id should be prefixed with its type, e.g. "user_123" or "course_456". Can be an array (by setting "filter[]") or single value (by setting "filter")
        :type filter: string or None
        :param filter_mode: (optional) no description
        :type filter_mode: combine them with this mode or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List conversations
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    scope_types = ('unread', 'starred', 'archived')
    filter_mode_types = ('and', 'or', 'default or] When filter[] contains multiple filters', 'filtering conversations that at have at least all of the contexts (and) or at least one of the contexts (or)')
    utils.validate_attr_is_acceptable(scope, scope_types)
    utils.validate_attr_is_acceptable(filter_mode, filter_mode_types)
    path = '/v1/conversations'
    payload = {
        'scope' : scope,
        'filter' : filter,
        'filter_mode' : filter_mode,
        'interleave_submissions' : interleave_submissions,
        'include_all_conversation_ids' : include_all_conversation_ids,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_conversation(request_ctx, recipients, body, group_conversation, attachment_ids, media_comment_id, media_comment_type, mode, subject=None, user_note=None, scope=None, filter=None, filter_mode=None, context_code=None, **request_kwargs):
    """
    Create a new conversation with one or more recipients. If there is already
    an existing private conversation with the given recipients, it will be
    reused.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param recipients: (required) An array of recipient ids. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. recipients[]=1&recipients[]=2&recipients[]=course_3
        :type recipients: string
        :param body: (required) The message to be sent
        :type body: string
        :param group_conversation: (required) Defaults to false. If true, this will be a group conversation (i.e. all recipients may see all messages and replies). If false, individual private conversations will be started with each recipient.
        :type group_conversation: boolean
        :param attachment_ids: (required) An array of attachments ids. These must be files that have been previously uploaded to the sender's "conversation attachments" folder.
        :type attachment_ids: string
        :param media_comment_id: (required) Media comment id of an audio of video file to be associated with this message.
        :type media_comment_id: string
        :param media_comment_type: (required) Type of the associated media file
        :type media_comment_type: string
        :param mode: (required) Determines whether the messages will be created/sent synchronously or asynchronously. Defaults to sync, and this option is ignored if this is a group conversation or there is just one recipient (i.e. it must be a bulk private message). When sent async, the response will be an empty array (batch status can be queried via the {api:ConversationsController#batches batches API})
        :type mode: string
        :param subject: (optional) The subject of the conversation. This is ignored when reusing a conversation. Maximum length is 255 characters.
        :type subject: string or None
        :param user_note: (optional) Will add a faculty journal entry for each recipient as long as the user making the api call has permission, the recipient is a student and faculty journals are enabled in the account.
        :type user_note: boolean or None
        :param scope: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type scope: string or None
        :param filter: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type filter: string or None
        :param filter_mode: (optional) no description
        :type filter_mode: string or None
        :param context_code: (optional) The course or group that is the context for this conversation. Same format as courses or groups in the recipients argument.
        :type context_code: string or None
        :return: Create a conversation
        :rtype: requests.Response (with void data)

    """

    media_comment_type_types = ('audio', 'video')
    mode_types = ('sync', 'async')
    scope_types = ('unread', 'starred', 'archived')
    filter_mode_types = ('and', 'or', 'default or] Used when generating visible in the API response. See the explanation under the {api:ConversationsController#index index API action}')
    utils.validate_attr_is_acceptable(media_comment_type, media_comment_type_types)
    utils.validate_attr_is_acceptable(mode, mode_types)
    utils.validate_attr_is_acceptable(scope, scope_types)
    utils.validate_attr_is_acceptable(filter_mode, filter_mode_types)
    path = '/v1/conversations'
    payload = {
        'recipients' : recipients,
        'subject' : subject,
        'body' : body,
        'group_conversation' : group_conversation,
        'attachment_ids' : attachment_ids,
        'media_comment_id' : media_comment_id,
        'media_comment_type' : media_comment_type,
        'user_note' : user_note,
        'mode' : mode,
        'scope' : scope,
        'filter' : filter,
        'filter_mode' : filter_mode,
        'context_code' : context_code,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_running_batches(request_ctx, **request_kwargs):
    """
    Returns any currently running conversation batches for the current user.
    Conversation batches are created when a bulk private message is sent
    asynchronously (see the mode argument to the `ConversationsController#create <https://github.com/instructure/canvas-lms/blob/master/app/controllers/conversations_controller.rb>`_).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Get running batches
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/batches'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_conversation(request_ctx, id, interleave_submissions, auto_mark_as_read, scope=None, filter=None, filter_mode=None, **request_kwargs):
    """
    Returns information for a single conversation. Response includes all
    fields that are present in the list/index action as well as messages
    and extended participant information.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param interleave_submissions: (required) (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored.
        :type interleave_submissions: boolean
        :param auto_mark_as_read: (required) Default true. If true, unread conversations will be automatically marked as read. This will default to false in a future API release, so clients should explicitly send true if that is the desired behavior.
        :type auto_mark_as_read: boolean
        :param scope: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type scope: string or None
        :param filter: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type filter: string or None
        :param filter_mode: (optional) no description
        :type filter_mode: string or None
        :return: Get a single conversation
        :rtype: requests.Response (with void data)

    """

    scope_types = ('unread', 'starred', 'archived')
    filter_mode_types = ('and', 'or', 'default or] Used when generating visible in the API response. See the explanation under the {api:ConversationsController#index index API action}')
    utils.validate_attr_is_acceptable(scope, scope_types)
    utils.validate_attr_is_acceptable(filter_mode, filter_mode_types)
    path = '/v1/conversations/{id}'
    payload = {
        'interleave_submissions' : interleave_submissions,
        'scope' : scope,
        'filter' : filter,
        'filter_mode' : filter_mode,
        'auto_mark_as_read' : auto_mark_as_read,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_conversation(request_ctx, id, conversation_subject, conversation_workflow_state, conversation_subscribed, conversation_starred, scope=None, filter=None, filter_mode=None, **request_kwargs):
    """
    Updates attributes for a single conversation.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param conversation_subject: (required) Change the subject of this conversation
        :type conversation_subject: string
        :param conversation_workflow_state: (required) Change the state of this conversation
        :type conversation_workflow_state: string
        :param conversation_subscribed: (required) Toggle the current user's subscription to the conversation (only valid for group conversations). If unsubscribed, the user will still have access to the latest messages, but the conversation won't be automatically flagged as unread, nor will it jump to the top of the inbox.
        :type conversation_subscribed: boolean
        :param conversation_starred: (required) Toggle the starred state of the current user's view of the conversation.
        :type conversation_starred: boolean
        :param scope: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type scope: string or None
        :param filter: (optional) Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action}
        :type filter: string or None
        :param filter_mode: (optional) no description
        :type filter_mode: string or None
        :return: Edit a conversation
        :rtype: requests.Response (with void data)

    """

    workflow_state_types = ('read', 'unread', 'archived')
    scope_types = ('unread', 'starred', 'archived')
    filter_mode_types = ('and', 'or', 'default or] Used when generating visible in the API response. See the explanation under the {api:ConversationsController#index index API action}')
    utils.validate_attr_is_acceptable(workflow_state, workflow_state_types)
    utils.validate_attr_is_acceptable(scope, scope_types)
    utils.validate_attr_is_acceptable(filter_mode, filter_mode_types)
    path = '/v1/conversations/{id}'
    payload = {
        'conversation[subject]' : conversation_subject,
        'conversation[workflow_state]' : conversation_workflow_state,
        'conversation[subscribed]' : conversation_subscribed,
        'conversation[starred]' : conversation_starred,
        'scope' : scope,
        'filter' : filter,
        'filter_mode' : filter_mode,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_as_read(request_ctx, **request_kwargs):
    """
    Mark all conversations as read.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Mark all as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/mark_all_as_read'
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def delete_conversation(request_ctx, id, **request_kwargs):
    """
    Delete this conversation and its messages. Note that this only deletes
    this user's view of the conversation.
    
    Response includes same fields as UPDATE action

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete a conversation
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def add_recipients(request_ctx, id, recipients, **request_kwargs):
    """
    Add recipients to an existing group conversation. Response is similar to
    the GET/show action, except that only includes the
    latest message (e.g. "joe was added to the conversation by bob")

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param recipients: (required) An array of recipient ids. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. recipients[]=1&recipients[]=2&recipients[]=course_3
        :type recipients: string
        :return: Add recipients
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/{id}/add_recipients'
    payload = {
        'recipients' : recipients,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def add_message(request_ctx, id, body, attachment_ids, media_comment_id, media_comment_type, recipients=None, included_messages=None, user_note=None, **request_kwargs):
    """
    Add a message to an existing conversation. Response is similar to the
    GET/show action, except that only includes the
    latest message (i.e. what we just sent)
    
    An array of user ids. Defaults to all of the current conversation
    recipients. To explicitly send a message to no other recipients,
    this array should consist of the logged-in user id.
    
    An array of message ids from this conversation to send to recipients
    of the new message. Recipients who already had a copy of included
    messages will not be affected.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param body: (required) The message to be sent.
        :type body: string
        :param attachment_ids: (required) An array of attachments ids. These must be files that have been previously uploaded to the sender's "conversation attachments" folder.
        :type attachment_ids: string
        :param media_comment_id: (required) Media comment id of an audio of video file to be associated with this message.
        :type media_comment_id: string
        :param media_comment_type: (required) Type of the associated media file.
        :type media_comment_type: string
        :param recipients: (optional) no description
        :type recipients: string or None
        :param included_messages: (optional) no description
        :type included_messages: string or None
        :param user_note: (optional) Will add a faculty journal entry for each recipient as long as the user making the api call has permission, the recipient is a student and faculty journals are enabled in the account.
        :type user_note: boolean or None
        :return: Add a message
        :rtype: requests.Response (with void data)

    """

    media_comment_type_types = ('audio', 'video')
    utils.validate_attr_is_acceptable(media_comment_type, media_comment_type_types)
    path = '/v1/conversations/{id}/add_message'
    payload = {
        'body' : body,
        'attachment_ids' : attachment_ids,
        'media_comment_id' : media_comment_id,
        'media_comment_type' : media_comment_type,
        'recipients' : recipients,
        'included_messages' : included_messages,
        'user_note' : user_note,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_message(request_ctx, id, remove, **request_kwargs):
    """
    Delete messages from this conversation. Note that this only affects this
    user's view of the conversation. If all messages are deleted, the
    conversation will be as well (equivalent to DELETE)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param remove: (required) Array of message ids to be deleted
        :type remove: string
        :return: Delete a message
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/{id}/remove_messages'
    payload = {
        'remove' : remove,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def batch_update_conversations(request_ctx, conversation_ids, event, **request_kwargs):
    """
    Perform a change on a set of conversations. Operates asynchronously; use the `ProgressController#show <https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb>`_
    to query the status of an operation.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param conversation_ids: (required) List of conversations to update. Limited to 500 conversations.
        :type conversation_ids: string
        :param event: (required) The action to take on each conversation.
        :type event: string
        :return: Batch update conversations
        :rtype: requests.Response (with Progress data)

    """

    event_types = ('mark_as_read', 'mark_as_unread', 'star', 'unstar', 'archive', 'destroy')
    utils.validate_attr_is_acceptable(event, event_types)
    path = '/v1/conversations'
    payload = {
        'conversation_ids' : conversation_ids,
        'event' : event,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def find_recipients(request_ctx, **request_kwargs):
    """
    Deprecated, see the `SearchController#recipients <https://github.com/instructure/canvas-lms/blob/master/app/controllers/search_controller.rb>`_ in the Search API

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Find recipients
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/find_recipients'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def unread_count(request_ctx, **request_kwargs):
    """
    Get the number of unread conversations for the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Unread count
        :rtype: requests.Response (with void data)

    """

    path = '/v1/conversations/unread_count'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


