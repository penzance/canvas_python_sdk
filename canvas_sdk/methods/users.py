from canvas_sdk import client, utils

def list_users_in_account(request_ctx, account_id, search_term=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of users associated with this account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.
        :type search_term: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/users'
    payload = {
        'search_term' : search_term,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_activity_stream_self(request_ctx, **request_kwargs):
    """
    Returns the current user's global activity stream, paginated.
    
    There are many types of objects that can be returned in the activity
    stream. All object types have the same basic set of shared attributes:
      !!!javascript
      {
        'created_at': '2011-07-13T09:12:00Z',
        'updated_at': '2011-07-25T08:52:41Z',
        'id': 1234,
        'title': 'Stream Item Subject',
        'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
        'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|...',
        'read_state': false,
        'context_type': 'course', // course|group
        'course_id': 1,
        'group_id': null,
        'html_url': "http://..." // URL to the Canvas web UI for this stream item
      }
    
    In addition, each item type has its own set of attributes available.
    
    DiscussionTopic:
    
      !!!javascript
      {
        'type': 'DiscussionTopic',
        'discussion_topic_id': 1234,
        'total_root_discussion_entries': 5,
        'require_initial_post': true,
        'user_has_posted': true,
        'root_discussion_entries': {
          ...
        }
      }
    
    For DiscussionTopic, the message is truncated at 4kb.
    
    Announcement:
    
      !!!javascript
      {
        'type': 'Announcement',
        'announcement_id': 1234,
        'total_root_discussion_entries': 5,
        'require_initial_post': true,
        'user_has_posted': null,
        'root_discussion_entries': {
          ...
        }
      }
    
    For Announcement, the message is truncated at 4kb.
    
    Conversation:
    
      !!!javascript
      {
        'type': 'Conversation',
        'conversation_id': 1234,
        'private': false,
        'participant_count': 3,
      }
    
    Message:
    
      !!!javascript
      {
        'type': 'Message',
        'message_id': 1234,
        'notification_category': 'Assignment Graded'
      }
    
    Submission:
    
    Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.
    
    Conference:
    
      !!!javascript
      {
        'type': 'Conference',
        'web_conference_id': 1234
      }
    
    Collaboration:
    
      !!!javascript
      {
        'type': 'Collaboration',
        'collaboration_id': 1234
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List the activity stream
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/activity_stream'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_activity_stream_activity_stream(request_ctx, **request_kwargs):
    """
    Returns the current user's global activity stream, paginated.
    
    There are many types of objects that can be returned in the activity
    stream. All object types have the same basic set of shared attributes:
      !!!javascript
      {
        'created_at': '2011-07-13T09:12:00Z',
        'updated_at': '2011-07-25T08:52:41Z',
        'id': 1234,
        'title': 'Stream Item Subject',
        'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
        'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|...',
        'read_state': false,
        'context_type': 'course', // course|group
        'course_id': 1,
        'group_id': null,
        'html_url': "http://..." // URL to the Canvas web UI for this stream item
      }
    
    In addition, each item type has its own set of attributes available.
    
    DiscussionTopic:
    
      !!!javascript
      {
        'type': 'DiscussionTopic',
        'discussion_topic_id': 1234,
        'total_root_discussion_entries': 5,
        'require_initial_post': true,
        'user_has_posted': true,
        'root_discussion_entries': {
          ...
        }
      }
    
    For DiscussionTopic, the message is truncated at 4kb.
    
    Announcement:
    
      !!!javascript
      {
        'type': 'Announcement',
        'announcement_id': 1234,
        'total_root_discussion_entries': 5,
        'require_initial_post': true,
        'user_has_posted': null,
        'root_discussion_entries': {
          ...
        }
      }
    
    For Announcement, the message is truncated at 4kb.
    
    Conversation:
    
      !!!javascript
      {
        'type': 'Conversation',
        'conversation_id': 1234,
        'private': false,
        'participant_count': 3,
      }
    
    Message:
    
      !!!javascript
      {
        'type': 'Message',
        'message_id': 1234,
        'notification_category': 'Assignment Graded'
      }
    
    Submission:
    
    Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.
    
    Conference:
    
      !!!javascript
      {
        'type': 'Conference',
        'web_conference_id': 1234
      }
    
    Collaboration:
    
      !!!javascript
      {
        'type': 'Collaboration',
        'collaboration_id': 1234
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List the activity stream
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/activity_stream'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def activity_stream_summary(request_ctx, **request_kwargs):
    """
    Returns a summary of the current user's global activity stream.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Activity stream summary
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/activity_stream/summary'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_todo_items(request_ctx, **request_kwargs):
    """
    Returns the current user's list of todo items, as seen on the user dashboard.
    
    There is a limit to the number of items returned.
    
    The `ignore` and `ignore_permanently` URLs can be used to update the user's
    preferences on what items will be displayed.
    Performing a DELETE request against the `ignore` URL will hide that item
    from future todo item requests, until the item changes.
    Performing a DELETE request against the `ignore_permanently` URL will hide
    that item forever.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List the TODO items
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/todo'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_upcoming_assignments_calendar_events(request_ctx, **request_kwargs):
    """
    Returns the current user's upcoming events, i.e. the same things shown
    in the dashboard 'Coming Up' sidebar.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: List upcoming assignments, calendar events
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/upcoming_events'
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def hide_stream_item(request_ctx, id, **request_kwargs):
    """
    Hide the given stream item.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Hide a stream item
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/activity_stream/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def hide_all_stream_items(request_ctx, **request_kwargs):
    """
    Hide all stream items for the user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Hide all stream items
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/activity_stream'
    url = request_ctx.base_api_url + path.format()
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def upload_file(request_ctx, user_id, **request_kwargs):
    """
    Upload a file to the user's personal files section.
    
    This API endpoint is the first step in uploading a file to a user's files.
    See the {file:file_uploads.html File Upload Documentation} for details on
    the file upload workflow.
    
    Note that typically users will only be able to upload files to their
    own files section. Passing a user_id of +self+ is an easy shortcut
    to specify the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/files'
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def create_user(request_ctx, account_id, pseudonym_unique_id, user_name=None, user_short_name=None, user_sortable_name=None, user_time_zone=None, user_locale=None, user_birthdate=None, user_terms_of_use=None, pseudonym_password=None, pseudonym_sis_user_id=None, pseudonym_send_confirmation=None, communication_channel_type=None, communication_channel_address=None, communication_channel_skip_confirmation=None, **request_kwargs):
    """
    Create and return a new user and pseudonym for an account.
    
    If you don't have the "Modify login details for users" permission, but
    self-registration is enabled on the account, you can still use this
    endpoint to register new users. Certain fields will be required, and
    others will be ignored (see below).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param pseudonym_unique_id: (required) User's login ID. If this is a self-registration, it must be a valid email address.
        :type pseudonym_unique_id: string
        :param user_name: (optional) The full name of the user. This name will be used by teacher for grading. Required if this is a self-registration.
        :type user_name: string or None
        :param user_short_name: (optional) User's name as it will be displayed in discussions, messages, and comments.
        :type user_short_name: string or None
        :param user_sortable_name: (optional) User's name as used to sort alphabetically in lists.
        :type user_sortable_name: string or None
        :param user_time_zone: (optional) The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type user_time_zone: string or None
        :param user_locale: (optional) The user's preferred language as a two-letter ISO 639-1 code.
        :type user_locale: string or None
        :param user_birthdate: (optional) The user's birth date.
        :type user_birthdate: date or None
        :param user_terms_of_use: (optional) Whether the user accepts the terms of use. Required if this is a self-registration and this canvas instance requires users to accept the terms (on by default).
        :type user_terms_of_use: boolean or None
        :param pseudonym_password: (optional) User's password. Cannot be set during self-registration.
        :type pseudonym_password: string or None
        :param pseudonym_sis_user_id: (optional) SIS ID for the user's account. To set this parameter, the caller must be able to manage SIS permissions.
        :type pseudonym_sis_user_id: string or None
        :param pseudonym_send_confirmation: (optional) Send user notification of account creation if true. Automatically set to true during self-registration.
        :type pseudonym_send_confirmation: boolean or None
        :param communication_channel_type: (optional) The communication channel type, e.g. 'email' or 'sms'.
        :type communication_channel_type: string or None
        :param communication_channel_address: (optional) The communication channel address, e.g. the user's email address.
        :type communication_channel_address: string or None
        :param communication_channel_skip_confirmation: (optional) Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.
        :type communication_channel_skip_confirmation: boolean or None
        :return: Create a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/accounts/{account_id}/users'
    payload = {
        'user[name]' : user_name,
        'user[short_name]' : user_short_name,
        'user[sortable_name]' : user_sortable_name,
        'user[time_zone]' : user_time_zone,
        'user[locale]' : user_locale,
        'user[birthdate]' : user_birthdate,
        'user[terms_of_use]' : user_terms_of_use,
        'pseudonym[unique_id]' : pseudonym_unique_id,
        'pseudonym[password]' : pseudonym_password,
        'pseudonym[sis_user_id]' : pseudonym_sis_user_id,
        'pseudonym[send_confirmation]' : pseudonym_send_confirmation,
        'communication_channel[type]' : communication_channel_type,
        'communication_channel[address]' : communication_channel_address,
        'communication_channel[skip_confirmation]' : communication_channel_skip_confirmation,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_user_settings(request_ctx, id, manual_mark_as_read, **request_kwargs):
    """
    Update an existing user's settings.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param manual_mark_as_read: (required) If true, require user to manually mark discussion posts as read (don't auto-mark as read).
        :type manual_mark_as_read: boolean
        :return: Update user settings.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/settings'
    payload = {
        'manual_mark_as_read' : manual_mark_as_read,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_user(request_ctx, id, user_name=None, user_short_name=None, user_sortable_name=None, user_time_zone=None, user_locale=None, user_avatar_token=None, user_avatar_url=None, **request_kwargs):
    """
    Modify an existing user. To modify a user's login, see the documentation for logins.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param user_name: (optional) The full name of the user. This name will be used by teacher for grading.
        :type user_name: string or None
        :param user_short_name: (optional) User's name as it will be displayed in discussions, messages, and comments.
        :type user_short_name: string or None
        :param user_sortable_name: (optional) User's name as used to sort alphabetically in lists.
        :type user_sortable_name: string or None
        :param user_time_zone: (optional) The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type user_time_zone: string or None
        :param user_locale: (optional) The user's preferred language as a two-letter ISO 639-1 code.
        :type user_locale: string or None
        :param user_avatar_token: (optional) A unique representation of the avatar record to assign as the user's current avatar. This token can be obtained from the user avatars endpoint. This supersedes the user[avatar][url] argument, and if both are included the url will be ignored. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
        :type user_avatar_token: string or None
        :param user_avatar_url: (optional) To set the user's avatar to point to an external url, do not include a token and instead pass the url here. Warning: For maximum compatibility, please use 128 px square images.
        :type user_avatar_url: string or None
        :return: Edit a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{id}'
    payload = {
        'user[name]' : user_name,
        'user[short_name]' : user_short_name,
        'user[sortable_name]' : user_sortable_name,
        'user[time_zone]' : user_time_zone,
        'user[locale]' : user_locale,
        'user[avatar][token]' : user_avatar_token,
        'user[avatar][url]' : user_avatar_url,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_user(request_ctx, account_id, id, **request_kwargs):
    """
    Delete a user record from Canvas.
    
    WARNING: This API will allow a user to delete themselves. If you do this,
    you won't be able to make API calls or log into Canvas.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/accounts/{account_id}/users/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def merge_user_into_another_user_destination_user_id(request_ctx, id, destination_user_id, **request_kwargs):
    """
    Merge a user into another user.
    To merge users, the caller must have permissions to manage both users.
    
    When finding users by SIS ids in different accounts the
    destination_account_id is required.
    
    The account can also be identified by passing the domain in destination_account_id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param destination_user_id: (required) ID
        :type destination_user_id: string
        :return: Merge user into another user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{id}/merge_into/{destination_user_id}'
    url = request_ctx.base_api_url + path.format(id=id, destination_user_id=destination_user_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def merge_user_into_another_user_accounts(request_ctx, id, destination_account_id, destination_user_id, **request_kwargs):
    """
    Merge a user into another user.
    To merge users, the caller must have permissions to manage both users.
    
    When finding users by SIS ids in different accounts the
    destination_account_id is required.
    
    The account can also be identified by passing the domain in destination_account_id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param destination_account_id: (required) ID
        :type destination_account_id: string
        :param destination_user_id: (required) ID
        :type destination_user_id: string
        :return: Merge user into another user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id}'
    url = request_ctx.base_api_url + path.format(id=id, destination_account_id=destination_account_id, destination_user_id=destination_user_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def get_user_profile(request_ctx, user_id, **request_kwargs):
    """
    Returns user profile data, including user id, name, and profile pic.
    
    When requesting the profile for the user accessing the API, the user's
    calendar feed URL will be returned as well.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :return: Get user profile
        :rtype: requests.Response (with Profile data)

    """

    path = '/v1/users/{user_id}/profile'
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_avatar_options(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Retrieve the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field. The following explains each field in more detail
    type:: ["gravatar"|"attachment"|"no_pic"] The type of avatar record, for categorization purposes.
    url:: The url of the avatar
    token:: A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
    display_name:: A textual description of the avatar record
    id:: ['attachment' type only] the internal id of the attachment
    content-type:: ['attachment' type only] the content-type of the attachment
    filename:: ['attachment' type only] the filename of the attachment
    size:: ['attachment' type only] the size of the attachment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List avatar options
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/avatars'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_user_page_views(request_ctx, user_id, start_time=None, end_time=None, per_page=None, **request_kwargs):
    """
    Return the user's page view history in json format, similar to the
    available CSV download. Pagination is used as described in API basics
    section. Page views are returned in descending order, newest to oldest.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param start_time: (optional) The beginning of the time range from which you want page views.
        :type start_time: datetime or None
        :param end_time: (optional) The end of the time range from which you want page views.
        :type end_time: datetime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List user page views
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/page_views'
    payload = {
        'start_time' : start_time,
        'end_time' : end_time,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def store_custom_data(request_ctx, user_id, scope, ns, data, **request_kwargs):
    """
    Store arbitrary user data as JSON.
    
    Arbitrary JSON data can be stored for a User.
    A typical scenario would be an external site/service that registers users in Canvas
    and wants to capture additional info about them.  The part of the URL that follows
    +/custom_data/+ defines the scope of the request, and it reflects the structure of
    the JSON data to be stored or retrieved.
    
    A namespace parameter, +ns+, is used to prevent custom_data collisions between
    different apps.  This parameter is required for all custom_data requests.
    
    A request with Content-Type multipart/form-data or Content-Type
    application/x-www-form-urlencoded can only be used to store strings.
    
    Example PUT with multipart/form-data data:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
        -X PUT \
        -F 'ns=com.my-organization.canvas-app' \
        -F 'data=555-1234' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": "555-1234"
      }
    
    Subscopes (or, generated scopes) can also be specified by passing values to
    data[<subscope>].
    
    Example PUT specifying subscopes:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
        -X PUT \
        -F 'ns=com.my-organization.canvas-app' \
        -F 'data[waist]=32in' \
        -F 'data[inseam]=34in' \
        -F 'data[chest]=40in' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": {
          "chest": "40in",
          "waist": "32in",
          "inseam": "34in"
        }
      }
    
    Following such a request, subsets of the stored data to be retrieved directly from a subscope.
    
    Example `UsersController#get_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ from a generated scope
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
        -X GET \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": "40in"
      }
    
    If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false,
    and/or null), you must make a request with Content-Type application/json as in the following
    example.
    
    Example PUT with JSON data:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
        -H 'Content-Type: application/json' \
        -X PUT \
        -d '{
              "ns": "com.my-organization.canvas-app",
              "data": {
                "a-number": 6.02e23,
                "a-bool": true,
                "a-string": "true",
                "a-hash": {"a": {"b": "ohai"}},
                "an-array": [1, "two", null, false]
              }
            }' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": {
          "a-number": 6.02e+23,
          "a-bool": true,
          "a-string": "true",
          "a-hash": {
            "a": {
              "b": "ohai"
            }
          },
          "an-array": [1, "two", null, false]
        }
      }
    
    If the data is an Object (as it is in the above example), then subsets of the data can
    be accessed by including the object's (possibly nested) keys in the scope of a GET request.
    
    Example `UsersController#get_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ with a generated scope:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
        -X GET \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": "ohai"
      }
    
    
    On success, this endpoint returns an object containing the data that was stored.
    
    Responds with status code 200 if the scope already contained data, and it was overwritten
    by the data specified in the request.
    
    Responds with status code 201 if the scope was previously empty, and the data specified
    in the request was successfully stored there.
    
    Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid, or if
    the +data+ parameter is missing.
    
    Responds with status code 409 if the requested scope caused a conflict and data was not stored.
    This happens when storing data at the requested scope would cause data at an outer scope
    to be lost.  e.g., if +/custom_data+ was +{"fashion_app": {"hair": "blonde"}}+, but
    you tried to +`PUT /custom_data/fashion_app/hair/style -F data=buzz`+, then for the request
    to succeed,the value of +/custom_data/fashion_app/hair+ would have to become a hash, and its
    old string value would be lost.  In this situation, an error object is returned with the
    following format:
    
      !!!javascript
      {
        "message": "write conflict for custom_data hash",
        "conflict_scope": "fashion_app/hair",
        "type_at_conflict": "String",
        "value_at_conflict": "blonde"
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param scope: (required) ID
        :type scope: string
        :param ns: (required) The namespace under which to store the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :param data: (required) The data you want to store for the user, at the specified scope. If the data is composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples).
        :type data: json
        :return: Store custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data/{scope}'
    payload = {
        'ns' : ns,
        'data' : data,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, scope=scope)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def load_custom_data(request_ctx, user_id, scope, ns, **request_kwargs):
    """
    Load custom user data.
    
    Arbitrary JSON data can be stored for a User.  This API call
    retrieves that data for a (optional) given scope.
    See `UsersController#set_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ for details and
    examples.
    
    On success, this endpoint returns an object containing the data that was requested.
    
    Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
    or if the specified scope does not contain any data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param scope: (required) ID
        :type scope: string
        :param ns: (required) The namespace from which to retrieve the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :return: Load custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data/{scope}'
    payload = {
        'ns' : ns,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, scope=scope)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_custom_data(request_ctx, user_id, scope, ns, **request_kwargs):
    """
    Delete custom user data.
    
    Arbitrary JSON data can be stored for a User.  This API call
    deletes that data for a given scope.  Without a scope, all custom_data is deleted.
    See `UsersController#set_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ for details and
    examples of storage and retrieval.
    
    As an example, we'll store some data, then delete a subset of it.
    
    Example `UsersController#set_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ with valid JSON data:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
        -X PUT \
        -F 'ns=com.my-organization.canvas-app' \
        -F 'data[fruit][apple]=so tasty' \
        -F 'data[fruit][kiwi]=a bit sour' \
        -F 'data[veggies][root][onion]=tear-jerking' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": {
          "fruit": {
            "apple": "so tasty",
            "kiwi": "a bit sour"
          },
          "veggies": {
            "root": {
              "onion": "tear-jerking"
            }
          }
        }
      }
    
    Example DELETE:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
        -X DELETE \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": "a bit sour"
      }
    
    Example `UsersController#get_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ following the above DELETE:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
        -X GET \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": {
          "fruit": {
            "apple": "so tasty"
          },
          "veggies": {
            "root": {
              "onion": "tear-jerking"
            }
          }
        }
      }
    
    Note that hashes left empty after a DELETE will get removed from the custom_data store.
    For example, following the previous commands, if we delete /custom_data/veggies/root/onion,
    then the entire /custom_data/veggies scope will be removed.
    
    Example DELETE that empties a parent scope:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
        -X DELETE \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": "tear-jerking"
      }
    
    Example `UsersController#get_custom_data <https://github.com/instructure/canvas-lms/blob/master/app/controllers/users_controller.rb>`_ following the above DELETE:
      curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
        -X GET \
        -F 'ns=com.my-organization.canvas-app' \
        -H 'Authorization: Bearer <token>'
    
    Response:
      !!!javascript
      {
        "data": {
          "fruit": {
            "apple": "so tasty"
          }
        }
      }
    
    On success, this endpoint returns an object containing the data that was deleted.
    
    Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
    or if the specified scope does not contain any data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param scope: (required) ID
        :type scope: string
        :param ns: (required) The namespace from which to delete the data. This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :return: Delete custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data/{scope}'
    payload = {
        'ns' : ns,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, scope=scope)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


