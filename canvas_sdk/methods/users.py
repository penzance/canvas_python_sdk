from canvas_sdk import client, utils


def list_users_in_account(request_ctx, account_id, search_term=None,
                          include=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of users associated with this account.
    
     @example_request
       curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
          -X GET \
          -H 'Authorization: Bearer <token>'

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the
results list. Must be at least 3 characters.

Note that the API will prefer matching on canonical user ID if the ID has
a numeric form. It will only search against other fields if non-numeric
in form, or if the numeric value doesn't yield any matches. Queries by
administrative users will search on SIS ID, name, or email address; non-
administrative queries will only be compared against name.
        :type search_term: string or None
        :param include: (optional) One of (avatar_url, email, last_login, time_zone)
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('avatar_url', 'email', 'last_login', 'time_zone')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/accounts/{account_id}/users'
    payload = {
        'include[]': include,
        'search_term': search_term,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_activity_stream_self(request_ctx, per_page=None, **request_kwargs):
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
        'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
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
    
    AssessmentRequest:
    
      !!!javascript
      {
        'type': 'AssessmentRequest',
        'assessment_request_id': 1234
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the activity stream
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/self/activity_stream'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_activity_stream_activity_stream(request_ctx, per_page=None, **request_kwargs):
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
        'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
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
    
    AssessmentRequest:
    
      !!!javascript
      {
        'type': 'AssessmentRequest',
        'assessment_request_id': 1234
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the activity stream
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/activity_stream'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

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


def list_todo_items(request_ctx, include=None, per_page=None, **request_kwargs):
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
        :param include: (optional) "ungraded_quizzes":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.
                     These will be returned under a +quiz+ key instead of an +assignment+ key in response elements.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List the TODO items
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('ungraded_quizzes')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/users/self/todo'
    payload = {
        'include': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_upcoming_assignments_calendar_events(request_ctx, per_page=None, **request_kwargs):
    """
    Returns the current user's upcoming events, i.e. the same things shown
    in the dashboard 'Coming Up' sidebar.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List upcoming assignments, calendar events
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/self/upcoming_events'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_missing_submissions(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    returns past-due assignments for which the student does not have a submission.
    The user sending the request must either be an admin or a parent observer using the parent app

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) the student's ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Missing Submissions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/missing_submissions'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

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


def show_user_details(request_ctx, id, **request_kwargs):
    """
    Shows details for user.
    
    Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.
    Example:
      !!!javascript
      "permissions": {
       "can_update_name": true, // Whether the user can update their name.
       "can_update_avatar": false // Whether the user can update their avatar.
      }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Show user details
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_user(request_ctx, account_id, pseudonym_unique_id, user_name=None, user_short_name=None, user_sortable_name=None, user_time_zone=None, user_locale=None, user_birthdate=None, user_terms_of_use=None, user_skip_registration=None, pseudonym_password=None, pseudonym_sis_user_id=None, pseudonym_integration_id=None, pseudonym_send_confirmation=None, pseudonym_force_self_registration=None, pseudonym_authentication_provider_id=None, communication_channel_type=None, communication_channel_address=None, communication_channel_confirmation_url=None, communication_channel_skip_confirmation=None, force_validations=None, enable_sis_reactivation=None, **request_kwargs):
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
        :param pseudonym_unique_id: (required) User's login ID. If this is a self-registration, it must be a valid
email address.
        :type pseudonym_unique_id: string
        :param user_name: (optional) The full name of the user. This name will be used by teacher for grading.
Required if this is a self-registration.
        :type user_name: string or None
        :param user_short_name: (optional) User's name as it will be displayed in discussions, messages, and comments.
        :type user_short_name: string or None
        :param user_sortable_name: (optional) User's name as used to sort alphabetically in lists.
        :type user_sortable_name: string or None
        :param user_time_zone: (optional) The time zone for the user. Allowed time zones are
{http://www.iana.org/time-zones IANA time zones} or friendlier
{http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type user_time_zone: string or None
        :param user_locale: (optional) The user's preferred language, from the list of languages Canvas supports.
This is in RFC-5646 format.
        :type user_locale: string or None
        :param user_birthdate: (optional) The user's birth date.
        :type user_birthdate: Date or None
        :param user_terms_of_use: (optional) Whether the user accepts the terms of use. Required if this is a
self-registration and this canvas instance requires users to accept
the terms (on by default).

If this is true, it will mark the user as having accepted the terms of use.
        :type user_terms_of_use: boolean or None
        :param user_skip_registration: (optional) Automatically mark the user as registered.

If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well.
Otherwise, the user will not receive any messages about their account creation.

The users communication channel confirmation can be skipped by setting
<tt>"communication_channel[skip_confirmation]"</tt> to true as well.
        :type user_skip_registration: boolean or None
        :param pseudonym_password: (optional) User's password. Cannot be set during self-registration.
        :type pseudonym_password: string or None
        :param pseudonym_sis_user_id: (optional) SIS ID for the user's account. To set this parameter, the caller must be
able to manage SIS permissions.
        :type pseudonym_sis_user_id: string or None
        :param pseudonym_integration_id: (optional) Integration ID for the login. To set this parameter, the caller must be able to
manage SIS permissions. The Integration ID is a secondary
identifier useful for more complex SIS integrations.
        :type pseudonym_integration_id: string or None
        :param pseudonym_send_confirmation: (optional) Send user notification of account creation if true.
Automatically set to true during self-registration.
        :type pseudonym_send_confirmation: boolean or None
        :param pseudonym_force_self_registration: (optional) Send user a self-registration style email if true.
Setting it means the users will get a notification asking them
to "complete the registration process" by clicking it, setting
a password, and letting them in.  Will only be executed on
if the user does not need admin approval.
Defaults to false unless explicitly provided.
        :type pseudonym_force_self_registration: boolean or None
        :param pseudonym_authentication_provider_id: (optional) The authentication provider this login is associated with. Logins
associated with a specific provider can only be used with that provider.
Legacy providers (LDAP, CAS, SAML) will search for logins associated with
them, or unassociated logins. New providers will only search for logins
explicitly associated with them. This can be the integer ID of the
provider, or the type of the provider (in which case, it will find the
first matching provider).
        :type pseudonym_authentication_provider_id: string or None
        :param communication_channel_type: (optional) The communication channel type, e.g. 'email' or 'sms'.
        :type communication_channel_type: string or None
        :param communication_channel_address: (optional) The communication channel address, e.g. the user's email address.
        :type communication_channel_address: string or None
        :param communication_channel_confirmation_url: (optional) Only valid for account admins. If true, returns the new user account
confirmation URL in the response.
        :type communication_channel_confirmation_url: boolean or None
        :param communication_channel_skip_confirmation: (optional) Only valid for site admins and account admins making requests; If true, the channel is
automatically validated and no confirmation email or SMS is sent.
Otherwise, the user must respond to a confirmation message to confirm the
channel.

If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well.
Otherwise, the user will not receive any messages about their account creation.
        :type communication_channel_skip_confirmation: boolean or None
        :param force_validations: (optional) If true, validations are performed on the newly created user (and their associated pseudonym)
even if the request is made by a privileged user like an admin. When set to false,
or not included in the request parameters, any newly created users are subject to
validations unless the request is made by a user with a 'manage_user_logins' right.
In which case, certain validations such as 'require_acceptance_of_terms' and
'require_presence_of_name' are not enforced. Use this parameter to return helpful json
errors while building users with an admin request.
        :type force_validations: boolean or None
        :param enable_sis_reactivation: (optional) When true, will first try to re-activate a deleted user with matching sis_user_id if possible.
        :type enable_sis_reactivation: boolean or None
        :return: Create a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/accounts/{account_id}/users'
    payload = {
        'user[name]': user_name,
        'user[short_name]': user_short_name,
        'user[sortable_name]': user_sortable_name,
        'user[time_zone]': user_time_zone,
        'user[locale]': user_locale,
        'user[birthdate]': user_birthdate,
        'user[terms_of_use]': user_terms_of_use,
        'user[skip_registration]': user_skip_registration,
        'pseudonym[unique_id]': pseudonym_unique_id,
        'pseudonym[password]': pseudonym_password,
        'pseudonym[sis_user_id]': pseudonym_sis_user_id,
        'pseudonym[integration_id]': pseudonym_integration_id,
        'pseudonym[send_confirmation]': pseudonym_send_confirmation,
        'pseudonym[force_self_registration]': pseudonym_force_self_registration,
        'pseudonym[authentication_provider_id]': pseudonym_authentication_provider_id,
        'communication_channel[type]': communication_channel_type,
        'communication_channel[address]': communication_channel_address,
        'communication_channel[confirmation_url]': communication_channel_confirmation_url,
        'communication_channel[skip_confirmation]': communication_channel_skip_confirmation,
        'force_validations': force_validations,
        'enable_sis_reactivation': enable_sis_reactivation,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def self_register_user(request_ctx, account_id, user_name, user_terms_of_use, pseudonym_unique_id, user_short_name=None, user_sortable_name=None, user_time_zone=None, user_locale=None, user_birthdate=None, communication_channel_type=None, communication_channel_address=None, **request_kwargs):
    """
    Self register and return a new user and pseudonym for an account.
    
    If self-registration is enabled on the account, you can use this
    endpoint to self register new users.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param user_name: (required) The full name of the user. This name will be used by teacher for grading.
        :type user_name: string
        :param user_terms_of_use: (required) Whether the user accepts the terms of use.
        :type user_terms_of_use: boolean
        :param pseudonym_unique_id: (required) User's login ID. Must be a valid email address.
        :type pseudonym_unique_id: string
        :param user_short_name: (optional) User's name as it will be displayed in discussions, messages, and comments.
        :type user_short_name: string or None
        :param user_sortable_name: (optional) User's name as used to sort alphabetically in lists.
        :type user_sortable_name: string or None
        :param user_time_zone: (optional) The time zone for the user. Allowed time zones are
{http://www.iana.org/time-zones IANA time zones} or friendlier
{http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type user_time_zone: string or None
        :param user_locale: (optional) The user's preferred language, from the list of languages Canvas supports.
This is in RFC-5646 format.
        :type user_locale: string or None
        :param user_birthdate: (optional) The user's birth date.
        :type user_birthdate: Date or None
        :param communication_channel_type: (optional) The communication channel type, e.g. 'email' or 'sms'.
        :type communication_channel_type: string or None
        :param communication_channel_address: (optional) The communication channel address, e.g. the user's email address.
        :type communication_channel_address: string or None
        :return: Self register a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/accounts/{account_id}/self_registration'
    payload = {
        'user[name]': user_name,
        'user[short_name]': user_short_name,
        'user[sortable_name]': user_sortable_name,
        'user[time_zone]': user_time_zone,
        'user[locale]': user_locale,
        'user[birthdate]': user_birthdate,
        'user[terms_of_use]': user_terms_of_use,
        'pseudonym[unique_id]': pseudonym_unique_id,
        'communication_channel[type]': communication_channel_type,
        'communication_channel[address]': communication_channel_address,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_user_settings(request_ctx, id, manual_mark_as_read=None, collapse_global_nav=None, **request_kwargs):
    """
    Update an existing user's settings.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param manual_mark_as_read: (optional) If true, require user to manually mark discussion posts as read (don't
auto-mark as read).
        :type manual_mark_as_read: boolean or None
        :param collapse_global_nav: (optional) If true, the user's page loads with the global navigation collapsed
        :type collapse_global_nav: boolean or None
        :return: Update user settings.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/settings'
    payload = {
        'manual_mark_as_read': manual_mark_as_read,
        'collapse_global_nav': collapse_global_nav,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_custom_colors(request_ctx, id, **request_kwargs):
    """
    Returns all custom colors that have been saved for a user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get custom colors
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/colors'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_custom_color(request_ctx, id, asset_string, **request_kwargs):
    """
    Returns the custom colors that have been saved for a user for a given context.
    
    The asset_string parameter should be in the format 'context_id', for example
    'course_42'.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param asset_string: (required) ID
        :type asset_string: string
        :return: Get custom color
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/colors/{asset_string}'
    url = request_ctx.base_api_url + path.format(id=id, asset_string=asset_string)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_custom_color(request_ctx, id, asset_string, hexcode=None, **request_kwargs):
    """
    Updates a custom color for a user for a given context.  This allows
    colors for the calendar and elsewhere to be customized on a user basis.
    
    The asset string parameter should be in the format 'context_id', for example
    'course_42'

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param asset_string: (required) ID
        :type asset_string: string
        :param hexcode: (optional) The hexcode of the color to set for the context, if you choose to pass the
hexcode as a query parameter rather than in the request body you should
NOT include the '#' unless you escape it first.
        :type hexcode: string or None
        :return: Update custom color
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/colors/{asset_string}'
    payload = {
        'hexcode': hexcode,
    }
    url = request_ctx.base_api_url + path.format(id=id, asset_string=asset_string)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_dashboard_postions(request_ctx, id, **request_kwargs):
    """
    Returns all dashboard positions that have been saved for a user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get dashboard postions
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/dashboard_positions'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_dashboard_positions(request_ctx, id, **request_kwargs):
    """
    Updates the dashboard positions for a user for a given context.  This allows
    positions for the dashboard cards and elsewhere to be customized on a per
    user basis.
    
    The asset string parameter should be in the format 'context_id', for example
    'course_42'

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Update dashboard positions
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{id}/dashboard_positions'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def edit_user(request_ctx, id, user_name=None, user_short_name=None, user_sortable_name=None, user_time_zone=None, user_email=None, user_locale=None, user_avatar_token=None, user_avatar_url=None, **request_kwargs):
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
        :param user_time_zone: (optional) The time zone for the user. Allowed time zones are
{http://www.iana.org/time-zones IANA time zones} or friendlier
{http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type user_time_zone: string or None
        :param user_email: (optional) The default email address of the user.
        :type user_email: string or None
        :param user_locale: (optional) The user's preferred language, from the list of languages Canvas supports.
This is in RFC-5646 format.
        :type user_locale: string or None
        :param user_avatar_token: (optional) A unique representation of the avatar record to assign as the user's
current avatar. This token can be obtained from the user avatars endpoint.
This supersedes the user [avatar] [url] argument, and if both are included
the url will be ignored. Note: this is an internal representation and is
subject to change without notice. It should be consumed with this api
endpoint and used in the user update endpoint, and should not be
constructed by the client.
        :type user_avatar_token: string or None
        :param user_avatar_url: (optional) To set the user's avatar to point to an external url, do not include a
token and instead pass the url here. Warning: For maximum compatibility,
please use 128 px square images.
        :type user_avatar_url: string or None
        :return: Edit a user
        :rtype: requests.Response (with User data)

    """

    path = '/v1/users/{id}'
    payload = {
        'user[name]': user_name,
        'user[short_name]': user_short_name,
        'user[sortable_name]': user_sortable_name,
        'user[time_zone]': user_time_zone,
        'user[email]': user_email,
        'user[locale]': user_locale,
        'user[avatar][token]': user_avatar_token,
        'user[avatar][url]': user_avatar_url,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def merge_user_into_another_user_destination_user_id(request_ctx, id, destination_user_id, **request_kwargs):
    """
    Merge a user into another user.
    To merge users, the caller must have permissions to manage both users. This
    should be considered irreversible. This will delete the user and move all
    the data into the destination user.
    
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
    To merge users, the caller must have permissions to manage both users. This
    should be considered irreversible. This will delete the user and move all
    the data into the destination user.
    
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


def split_merged_users_into_separate_users(request_ctx, id, per_page=None, **request_kwargs):
    """
    Merged users cannot be fully restored to their previous state, but this will
    attempt to split as much as possible to the previous state.
    To split a merged user, the caller must have permissions to manage all of
    the users logins. If there are multiple users that have been merged into one
    user it will split each merge into a separate user.
    A split can only happen within 90 days of a user merge. A user merge deletes
    the previous user and may be permanently deleted. In this scenario we create
    a new user object and proceed to move as much as possible to the new user.
    The user object will not have preserved the name or settings from the
    previous user. Some items may have been deleted during a user_merge that
    cannot be restored, and/or the data has become stale because of other
    changes to the objects since the time of the user_merge.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Split merged users into separate users
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{id}/split'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_user_profile(request_ctx, user_id, **request_kwargs):
    """
    Returns user profile data, including user id, name, and profile pic.
    
    When requesting the profile for the user accessing the API, the user's
    calendar feed URL and LTI user id will be returned as well.

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
        'per_page': per_page,
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
        :type start_time: DateTime or None
        :param end_time: (optional) The end of the time range from which you want page views.
        :type end_time: DateTime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List user page views
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/page_views'
    payload = {
        'start_time': start_time,
        'end_time': end_time,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def store_custom_data(request_ctx, user_id, ns, data, **request_kwargs):
    """
    Store arbitrary user data as JSON.
    
    Arbitrary JSON data can be stored for a User.
    A typical scenario would be an external site/service that registers users in Canvas
    and wants to capture additional info about them.  The part of the URL that follows
    +/custom_data/+ defines the scope of the request, and it reflects the structure of
    the JSON data to be stored or retrieved.
    
    The value +self+ may be used for +user_id+ to store data associated with the calling user.
    In order to access another user's custom data, you must be an account administrator with
    permission to manage users.
    
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
    +data+[+subscope+].
    
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
        :param ns: (required) The namespace under which to store the data.  This should be something other
Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :param data: (required) The data you want to store for the user, at the specified scope.  If the data is
composed of (possibly nested) JSON objects, scopes will be generated for the (nested)
keys (see examples).
        :type data: JSON
        :return: Store custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data'
    payload = {
        'ns': ns,
        'data': data,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def load_custom_data(request_ctx, user_id, ns, **request_kwargs):
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
        :param ns: (required) The namespace from which to retrieve the data.  This should be something other
Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :return: Load custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data'
    payload = {
        'ns': ns,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_custom_data(request_ctx, user_id, ns, **request_kwargs):
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
        :param ns: (required) The namespace from which to delete the data.  This should be something other
Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        :type ns: string
        :return: Delete custom data
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/custom_data'
    payload = {
        'ns': ns,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_course_nicknames(request_ctx, per_page=None, **request_kwargs):
    """
    Returns all course nicknames you have set.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List course nicknames
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/self/course_nicknames'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_course_nickname(request_ctx, course_id, **request_kwargs):
    """
    Returns the nickname for a specific course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Get course nickname
        :rtype: requests.Response (with CourseNickname data)

    """

    path = '/v1/users/self/course_nicknames/{course_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def set_course_nickname(request_ctx, course_id, nickname, **request_kwargs):
    """
    Set a nickname for the given course. This will replace the course's name
    in output of API calls you make subsequently, as well as in selected
    places in the Canvas web user interface.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param nickname: (required) The nickname to set.  It must be non-empty and shorter than 60 characters.
        :type nickname: string
        :return: Set course nickname
        :rtype: requests.Response (with CourseNickname data)

    """

    path = '/v1/users/self/course_nicknames/{course_id}'
    payload = {
        'nickname': nickname,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_course_nickname(request_ctx, course_id, **request_kwargs):
    """
    Remove the nickname for the given course.
    Subsequent course API calls will return the actual name for the course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Remove course nickname
        :rtype: requests.Response (with CourseNickname data)

    """

    path = '/v1/users/self/course_nicknames/{course_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def clear_course_nicknames(request_ctx, **request_kwargs):
    """
    Remove all stored course nicknames.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Clear course nicknames
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/course_nicknames'
    url = request_ctx.base_api_url + path.format()
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


