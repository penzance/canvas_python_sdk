from __future__ import unicode_literals
from canvas_sdk import client, utils

def list_discussion_topics_courses(request_ctx, course_id, order_by=None, scope=None, only_announcements=None, search_term=None, **request_kwargs):
    """
    Returns the paginated list of discussion topics for this course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param order_by: (optional) Determines the order of the discussion topic list. Defaults to "position".
        :type order_by: string or None
        :param scope: (optional) Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string.
        :type scope: string or None
        :param only_announcements: (optional) Return announcements instead of discussion topics. Defaults to false
        :type only_announcements: boolean or None
        :param search_term: (optional) The partial title of the discussion topics to match and return.
        :type search_term: string or None
        :return: List discussion topics
        :rtype: requests.Response (with void data)

    """

    order_by_types = ('position', 'recent_activity')
    scope_types = ('locked', 'unlocked', 'pinned', 'unpinned')
    utils.validate_attr_is_acceptable(order_by, order_by_types)
    utils.validate_attr_is_acceptable(scope, scope_types)
    path = '/v1/courses/{course_id}/discussion_topics'
    payload = {
        'order_by' : order_by,
        'scope' : scope,
        'only_announcements' : only_announcements,
        'search_term' : search_term,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_discussion_topics_groups(request_ctx, group_id, order_by=None, scope=None, only_announcements=None, search_term=None, **request_kwargs):
    """
    Returns the paginated list of discussion topics for this course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param order_by: (optional) Determines the order of the discussion topic list. Defaults to "position".
        :type order_by: string or None
        :param scope: (optional) Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string.
        :type scope: string or None
        :param only_announcements: (optional) Return announcements instead of discussion topics. Defaults to false
        :type only_announcements: boolean or None
        :param search_term: (optional) The partial title of the discussion topics to match and return.
        :type search_term: string or None
        :return: List discussion topics
        :rtype: requests.Response (with void data)

    """

    order_by_types = ('position', 'recent_activity')
    scope_types = ('locked', 'unlocked', 'pinned', 'unpinned')
    utils.validate_attr_is_acceptable(order_by, order_by_types)
    utils.validate_attr_is_acceptable(scope, scope_types)
    path = '/v1/groups/{group_id}/discussion_topics'
    payload = {
        'order_by' : order_by,
        'scope' : scope,
        'only_announcements' : only_announcements,
        'search_term' : search_term,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_discussion_topic_courses(request_ctx, course_id, title, message, require_initial_post, discussion_type=None, published=None, delayed_post_at=None, lock_at=None, podcast_enabled=None, podcast_has_student_posts=None, assignment=None, is_announcement=None, position_after=None, group_category_id=None, **request_kwargs):
    """
    Create an new discussion topic for the course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param title: (required) no description
        :type title: string
        :param message: (required) no description
        :type message: string
        :param require_initial_post: (required) If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.
        :type require_initial_post: boolean
        :param discussion_type: (optional) The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions.
        :type discussion_type: string or None
        :param published: (optional) Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics.
        :type published: boolean or None
        :param delayed_post_at: (optional) If a timestamp is given, the topic will not be published until that time.
        :type delayed_post_at: datetime or None
        :param lock_at: (optional) If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked.
        :type lock_at: datetime or None
        :param podcast_enabled: (optional) If true, the topic will have an associated podcast feed.
        :type podcast_enabled: boolean or None
        :param podcast_has_student_posts: (optional) If true, the podcast will include posts from students as well. Implies podcast_enabled.
        :type podcast_has_student_posts: boolean or None
        :param assignment: (optional) To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object
        :type assignment: assignment or None
        :param is_announcement: (optional) If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions.
        :type is_announcement: boolean or None
        :param position_after: (optional) By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed.
        :type position_after: string or None
        :param group_category_id: (optional) If present, the topic will become a group discussion assigned to the group.
        :type group_category_id: integer or None
        :return: Create a new discussion topic
        :rtype: requests.Response (with void data)

    """

    discussion_type_types = ('side_comment', 'threaded')
    utils.validate_attr_is_acceptable(discussion_type, discussion_type_types)
    path = '/v1/courses/{course_id}/discussion_topics'
    payload = {
        'title' : title,
        'message' : message,
        'discussion_type' : discussion_type,
        'published' : published,
        'delayed_post_at' : delayed_post_at,
        'lock_at' : lock_at,
        'podcast_enabled' : podcast_enabled,
        'podcast_has_student_posts' : podcast_has_student_posts,
        'require_initial_post' : require_initial_post,
        'assignment' : assignment,
        'is_announcement' : is_announcement,
        'position_after' : position_after,
        'group_category_id' : group_category_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_discussion_topic_groups(request_ctx, group_id, title, message, require_initial_post, discussion_type=None, published=None, delayed_post_at=None, lock_at=None, podcast_enabled=None, podcast_has_student_posts=None, assignment=None, is_announcement=None, position_after=None, group_category_id=None, **request_kwargs):
    """
    Create an new discussion topic for the course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param title: (required) no description
        :type title: string
        :param message: (required) no description
        :type message: string
        :param require_initial_post: (required) If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.
        :type require_initial_post: boolean
        :param discussion_type: (optional) The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions.
        :type discussion_type: string or None
        :param published: (optional) Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics.
        :type published: boolean or None
        :param delayed_post_at: (optional) If a timestamp is given, the topic will not be published until that time.
        :type delayed_post_at: datetime or None
        :param lock_at: (optional) If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked.
        :type lock_at: datetime or None
        :param podcast_enabled: (optional) If true, the topic will have an associated podcast feed.
        :type podcast_enabled: boolean or None
        :param podcast_has_student_posts: (optional) If true, the podcast will include posts from students as well. Implies podcast_enabled.
        :type podcast_has_student_posts: boolean or None
        :param assignment: (optional) To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object
        :type assignment: assignment or None
        :param is_announcement: (optional) If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions.
        :type is_announcement: boolean or None
        :param position_after: (optional) By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed.
        :type position_after: string or None
        :param group_category_id: (optional) If present, the topic will become a group discussion assigned to the group.
        :type group_category_id: integer or None
        :return: Create a new discussion topic
        :rtype: requests.Response (with void data)

    """

    discussion_type_types = ('side_comment', 'threaded')
    utils.validate_attr_is_acceptable(discussion_type, discussion_type_types)
    path = '/v1/groups/{group_id}/discussion_topics'
    payload = {
        'title' : title,
        'message' : message,
        'discussion_type' : discussion_type,
        'published' : published,
        'delayed_post_at' : delayed_post_at,
        'lock_at' : lock_at,
        'podcast_enabled' : podcast_enabled,
        'podcast_has_student_posts' : podcast_has_student_posts,
        'require_initial_post' : require_initial_post,
        'assignment' : assignment,
        'is_announcement' : is_announcement,
        'position_after' : position_after,
        'group_category_id' : group_category_id,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_new_discussion_topic_collection_items(request_ctx, collection_item_id, title, message, require_initial_post, discussion_type=None, published=None, delayed_post_at=None, lock_at=None, podcast_enabled=None, podcast_has_student_posts=None, assignment=None, is_announcement=None, position_after=None, group_category_id=None, **request_kwargs):
    """
    Create an new discussion topic for the course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param title: (required) no description
        :type title: string
        :param message: (required) no description
        :type message: string
        :param require_initial_post: (required) If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false.
        :type require_initial_post: boolean
        :param discussion_type: (optional) The type of discussion. Defaults to side_comment if not value is given. Accepted values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions.
        :type discussion_type: string or None
        :param published: (optional) Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics.
        :type published: boolean or None
        :param delayed_post_at: (optional) If a timestamp is given, the topic will not be published until that time.
        :type delayed_post_at: datetime or None
        :param lock_at: (optional) If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked.
        :type lock_at: datetime or None
        :param podcast_enabled: (optional) If true, the topic will have an associated podcast feed.
        :type podcast_enabled: boolean or None
        :param podcast_has_student_posts: (optional) If true, the podcast will include posts from students as well. Implies podcast_enabled.
        :type podcast_has_student_posts: boolean or None
        :param assignment: (optional) To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object
        :type assignment: assignment or None
        :param is_announcement: (optional) If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions.
        :type is_announcement: boolean or None
        :param position_after: (optional) By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed.
        :type position_after: string or None
        :param group_category_id: (optional) If present, the topic will become a group discussion assigned to the group.
        :type group_category_id: integer or None
        :return: Create a new discussion topic
        :rtype: requests.Response (with void data)

    """

    discussion_type_types = ('side_comment', 'threaded')
    utils.validate_attr_is_acceptable(discussion_type, discussion_type_types)
    path = '/v1/collection_items/{collection_item_id}/discussion_topics'
    payload = {
        'title' : title,
        'message' : message,
        'discussion_type' : discussion_type,
        'published' : published,
        'delayed_post_at' : delayed_post_at,
        'lock_at' : lock_at,
        'podcast_enabled' : podcast_enabled,
        'podcast_has_student_posts' : podcast_has_student_posts,
        'require_initial_post' : require_initial_post,
        'assignment' : assignment,
        'is_announcement' : is_announcement,
        'position_after' : position_after,
        'group_category_id' : group_category_id,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Accepts the same parameters as create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Update a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Accepts the same parameters as create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Update a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Accepts the same parameters as create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Update a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def delete_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Deletes the discussion topic. This will also delete the assignment, if it's
    an assignment discussion.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Delete a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Deletes the discussion topic. This will also delete the assignment, if it's
    an assignment discussion.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Delete a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Deletes the discussion topic. This will also delete the assignment, if it's
    an assignment discussion.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Delete a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def reorder_pinned_topics_courses(request_ctx, course_id, order=None, **request_kwargs):
    """
    Puts the pinned discussion topics in the specified order.
    All pinned topics should be included.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param order: (optional) The ids of the pinned discussion topics in the desired order. (For example, "order=104,102,103".)
        :type order: integer or None
        :return: Reorder pinned topics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/reorder'
    payload = {
        'order' : order,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def reorder_pinned_topics_groups(request_ctx, group_id, order=None, **request_kwargs):
    """
    Puts the pinned discussion topics in the specified order.
    All pinned topics should be included.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param order: (optional) The ids of the pinned discussion topics in the desired order. (For example, "order=104,102,103".)
        :type order: integer or None
        :return: Reorder pinned topics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/reorder'
    payload = {
        'order' : order,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def reorder_pinned_topics_collection_items(request_ctx, collection_item_id, order=None, **request_kwargs):
    """
    Puts the pinned discussion topics in the specified order.
    All pinned topics should be included.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param order: (optional) The ids of the pinned discussion topics in the desired order. (For example, "order=104,102,103".)
        :type order: integer or None
        :return: Reorder pinned topics
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/reorder'
    payload = {
        'order' : order,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_entry_courses(request_ctx, course_id, topic_id, id, message, **request_kwargs):
    """
    Update an existing discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :param message: (required) The updated body of the entry.
        :type message: string
        :return: Update an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}'
    payload = {
        'message' : message,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_entry_groups(request_ctx, group_id, topic_id, id, message, **request_kwargs):
    """
    Update an existing discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :param message: (required) The updated body of the entry.
        :type message: string
        :return: Update an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}'
    payload = {
        'message' : message,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_entry_collection_items(request_ctx, collection_item_id, topic_id, id, message, **request_kwargs):
    """
    Update an existing discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :param message: (required) The updated body of the entry.
        :type message: string
        :return: Update an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{id}'
    payload = {
        'message' : message,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_entry_courses(request_ctx, course_id, topic_id, id, **request_kwargs):
    """
    Delete a discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.
    
    The discussion will be marked deleted, and the user_id and message will be cleared out.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_entry_groups(request_ctx, group_id, topic_id, id, **request_kwargs):
    """
    Delete a discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.
    
    The discussion will be marked deleted, and the user_id and message will be cleared out.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_entry_collection_items(request_ctx, collection_item_id, topic_id, id, **request_kwargs):
    """
    Delete a discussion entry.
    
    The entry must have been created by the current user, or the current user
    must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.
    
    The discussion will be marked deleted, and the user_id and message will be cleared out.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{id}'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def get_single_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Returns data on an individual discussion topic. See the List action for the response formatting.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get a single topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Returns data on an individual discussion topic. See the List action for the response formatting.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get a single topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Returns data on an individual discussion topic. See the List action for the response formatting.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get a single topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_full_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Return a cached structure of the discussion topic, containing all entries,
    their authors, and their message bodies.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    In some rare situations, this cached structure may not be available yet. In
    that case, the server will respond with a 503 error, and the caller should
    try again soon.
    
    The response is an object containing the following keys:
    * "participants": A list of summary information on users who have posted to
      the discussion. Each value is an object containing their id, display_name,
      and avatar_url.
    * "unread_entries": A list of entry ids that are unread by the current
      user. this implies that any entry not in this list is read.
    * "forced_entries": A list of entry ids that have forced_read_state set to
      true. This flag is meant to indicate the entry's read_state has been
      manually set to 'unread' by the user, so the entry should not be
      automatically marked as read.
    * "view": A threaded view of all the entries in the discussion, containing
      the id, user_id, and message.
    * "new_entries": Because this view is eventually consistent, it's possible
      that newly created or updated entries won't yet be reflected in the view.
      If the application wants to also get a flat list of all entries not yet
      reflected in the view, pass include_new_entries=1 to the request and this
      array of entries will be returned. These entries are returned in a flat
      array, in ascending created_at order.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get the full topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/view'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_full_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Return a cached structure of the discussion topic, containing all entries,
    their authors, and their message bodies.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    In some rare situations, this cached structure may not be available yet. In
    that case, the server will respond with a 503 error, and the caller should
    try again soon.
    
    The response is an object containing the following keys:
    * "participants": A list of summary information on users who have posted to
      the discussion. Each value is an object containing their id, display_name,
      and avatar_url.
    * "unread_entries": A list of entry ids that are unread by the current
      user. this implies that any entry not in this list is read.
    * "forced_entries": A list of entry ids that have forced_read_state set to
      true. This flag is meant to indicate the entry's read_state has been
      manually set to 'unread' by the user, so the entry should not be
      automatically marked as read.
    * "view": A threaded view of all the entries in the discussion, containing
      the id, user_id, and message.
    * "new_entries": Because this view is eventually consistent, it's possible
      that newly created or updated entries won't yet be reflected in the view.
      If the application wants to also get a flat list of all entries not yet
      reflected in the view, pass include_new_entries=1 to the request and this
      array of entries will be returned. These entries are returned in a flat
      array, in ascending created_at order.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get the full topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/view'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_full_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Return a cached structure of the discussion topic, containing all entries,
    their authors, and their message bodies.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    In some rare situations, this cached structure may not be available yet. In
    that case, the server will respond with a 503 error, and the caller should
    try again soon.
    
    The response is an object containing the following keys:
    * "participants": A list of summary information on users who have posted to
      the discussion. Each value is an object containing their id, display_name,
      and avatar_url.
    * "unread_entries": A list of entry ids that are unread by the current
      user. this implies that any entry not in this list is read.
    * "forced_entries": A list of entry ids that have forced_read_state set to
      true. This flag is meant to indicate the entry's read_state has been
      manually set to 'unread' by the user, so the entry should not be
      automatically marked as read.
    * "view": A threaded view of all the entries in the discussion, containing
      the id, user_id, and message.
    * "new_entries": Because this view is eventually consistent, it's possible
      that newly created or updated entries won't yet be reflected in the view.
      If the application wants to also get a flat list of all entries not yet
      reflected in the view, pass include_new_entries=1 to the request and this
      array of entries will be returned. These entries are returned in a flat
      array, in ascending created_at order.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Get the full topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/view'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def post_entry_courses(request_ctx, course_id, topic_id, message, attachment=None, **request_kwargs):
    """
    Create a new entry in a discussion topic. Returns a json representation of
    the created entry (see documentation for 'entries' method) on success.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def post_entry_groups(request_ctx, group_id, topic_id, message, attachment=None, **request_kwargs):
    """
    Create a new entry in a discussion topic. Returns a json representation of
    the created entry (see documentation for 'entries' method) on success.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def post_entry_collection_items(request_ctx, collection_item_id, topic_id, message, attachment=None, **request_kwargs):
    """
    Create a new entry in a discussion topic. Returns a json representation of
    the created entry (see documentation for 'entries' method) on success.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post an entry
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_topic_entries_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Retrieve the (paginated) top-level entries in a discussion topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Will include the 10 most recent replies, if any, for each entry returned.
    
    If the topic is a root topic with children corresponding to groups of a
    group assignment, entries from those subtopics for which the user belongs
    to the corresponding group will be returned.
    
    Ordering of returned entries is newest-first by posting timestamp (reply
    activity is ignored).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: List topic entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_topic_entries_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Retrieve the (paginated) top-level entries in a discussion topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Will include the 10 most recent replies, if any, for each entry returned.
    
    If the topic is a root topic with children corresponding to groups of a
    group assignment, entries from those subtopics for which the user belongs
    to the corresponding group will be returned.
    
    Ordering of returned entries is newest-first by posting timestamp (reply
    activity is ignored).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: List topic entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_topic_entries_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Retrieve the (paginated) top-level entries in a discussion topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Will include the 10 most recent replies, if any, for each entry returned.
    
    If the topic is a root topic with children corresponding to groups of a
    group assignment, entries from those subtopics for which the user belongs
    to the corresponding group will be returned.
    
    Ordering of returned entries is newest-first by posting timestamp (reply
    activity is ignored).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: List topic entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def post_reply_courses(request_ctx, course_id, topic_id, entry_id, message, attachment=None, **request_kwargs):
    """
    Add a reply to an entry in a discussion topic. Returns a json
    representation of the created reply (see documentation for 'replies'
    method) on success.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post a reply
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, entry_id=entry_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def post_reply_groups(request_ctx, group_id, topic_id, entry_id, message, attachment=None, **request_kwargs):
    """
    Add a reply to an entry in a discussion topic. Returns a json
    representation of the created reply (see documentation for 'replies'
    method) on success.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post a reply
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, entry_id=entry_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def post_reply_collection_items(request_ctx, collection_item_id, topic_id, entry_id, message, attachment=None, **request_kwargs):
    """
    Add a reply to an entry in a discussion topic. Returns a json
    representation of the created reply (see documentation for 'replies'
    method) on success.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param message: (required) The body of the entry.
        :type message: string
        :param attachment: (optional) a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions.
        :type attachment: string or None
        :return: Post a reply
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    payload = {
        'message' : message,
        'attachment' : attachment,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, entry_id=entry_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_entry_replies_courses(request_ctx, course_id, topic_id, entry_id, **request_kwargs):
    """
    Retrieve the (paginated) replies to a top-level entry in a discussion
    topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Ordering of returned entries is newest-first by creation timestamp.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :return: List entry replies
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, entry_id=entry_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_entry_replies_groups(request_ctx, group_id, topic_id, entry_id, **request_kwargs):
    """
    Retrieve the (paginated) replies to a top-level entry in a discussion
    topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Ordering of returned entries is newest-first by creation timestamp.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :return: List entry replies
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, entry_id=entry_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_entry_replies_collection_items(request_ctx, collection_item_id, topic_id, entry_id, **request_kwargs):
    """
    Retrieve the (paginated) replies to a top-level entry in a discussion
    topic.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.
    
    Ordering of returned entries is newest-first by creation timestamp.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :return: List entry replies
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, entry_id=entry_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_entries_courses(request_ctx, course_id, topic_id, ids, **request_kwargs):
    """
    Retrieve a paginated list of discussion entries, given a list of ids.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param ids: (required) A list of entry ids to retrieve. Entries will be returned in id order, smallest id first.
        :type ids: string
        :return: List entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list'
    payload = {
        'ids' : ids,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_entries_groups(request_ctx, group_id, topic_id, ids, **request_kwargs):
    """
    Retrieve a paginated list of discussion entries, given a list of ids.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param ids: (required) A list of entry ids to retrieve. Entries will be returned in id order, smallest id first.
        :type ids: string
        :return: List entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list'
    payload = {
        'ids' : ids,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_entries_collection_items(request_ctx, collection_item_id, topic_id, ids, **request_kwargs):
    """
    Retrieve a paginated list of discussion entries, given a list of ids.
    
    May require (depending on the topic) that the user has posted in the topic.
    If it is required, and the user has not posted, will respond with a 403
    Forbidden status and the body 'require_initial_post'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param ids: (required) A list of entry ids to retrieve. Entries will be returned in id order, smallest id first.
        :type ids: string
        :return: List entries
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entry_list'
    payload = {
        'ids' : ids,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_topic_as_read_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def mark_topic_as_read_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def mark_topic_as_read_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def mark_topic_as_unread_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def mark_topic_as_unread_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def mark_topic_as_unread_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Mark the initial text of the discussion topic as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Mark topic as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/read'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def mark_all_entries_as_read_courses(request_ctx, course_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_entries_as_read_groups(request_ctx, group_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_entries_as_read_collection_items(request_ctx, collection_item_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_entries_as_unread_courses(request_ctx, course_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_entries_as_unread_groups(request_ctx, group_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_all_entries_as_unread_collection_items(request_ctx, collection_item_id, topic_id, forced_read_state=None, **request_kwargs):
    """
    Mark the discussion topic and all its entries as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param forced_read_state: (optional) A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark all entries as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/read_all'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_read_courses(request_ctx, course_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, entry_id=entry_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_read_groups(request_ctx, group_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, entry_id=entry_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_read_collection_items(request_ctx, collection_item_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as read.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as read
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, entry_id=entry_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_unread_courses(request_ctx, course_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id, entry_id=entry_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_unread_groups(request_ctx, group_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id, entry_id=entry_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def mark_entry_as_unread_collection_items(request_ctx, collection_item_id, topic_id, entry_id, forced_read_state=None, **request_kwargs):
    """
    Mark a discussion entry as unread.
    
    No request fields are necessary.
    
    On success, the response will be 204 No Content with an empty body.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :param entry_id: (required) ID
        :type entry_id: string
        :param forced_read_state: (optional) A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified.
        :type forced_read_state: boolean or None
        :return: Mark entry as unread
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'
    payload = {
        'forced_read_state' : forced_read_state,
    }
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id, entry_id=entry_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def subscribe_to_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Subscribe to a topic to receive notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Subscribe to a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def subscribe_to_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Subscribe to a topic to receive notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Subscribe to a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def subscribe_to_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Subscribe to a topic to receive notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Subscribe to a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def unsubscribe_from_topic_courses(request_ctx, course_id, topic_id, **request_kwargs):
    """
    Unsubscribe from a topic to stop receiving notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Unsubscribe from a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(course_id=course_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def unsubscribe_from_topic_groups(request_ctx, group_id, topic_id, **request_kwargs):
    """
    Unsubscribe from a topic to stop receiving notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Unsubscribe from a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(group_id=group_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def unsubscribe_from_topic_collection_items(request_ctx, collection_item_id, topic_id, **request_kwargs):
    """
    Unsubscribe from a topic to stop receiving notifications about new entries
    
    On success, the response will be 204 No Content with an empty body

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param collection_item_id: (required) ID
        :type collection_item_id: string
        :param topic_id: (required) ID
        :type topic_id: string
        :return: Unsubscribe from a topic
        :rtype: requests.Response (with void data)

    """

    path = '/v1/collection_items/{collection_item_id}/discussion_topics/{topic_id}/subscribed'
    url = request_ctx.base_api_url + path.format(collection_item_id=collection_item_id, topic_id=topic_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


