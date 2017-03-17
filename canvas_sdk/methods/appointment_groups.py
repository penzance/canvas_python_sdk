from canvas_sdk import client, utils


def list_appointment_groups(request_ctx, scope=None, context_codes=None, include_past_appointments=None, include=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of appointment groups that can be reserved or managed by
    the current user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param scope: (optional) Defaults to "reservable"
        :type scope: string or None
        :param context_codes: (optional) Array of context codes used to limit returned results.
        :type context_codes: array or None
        :param include_past_appointments: (optional) Defaults to false. If true, includes past appointment groups
        :type include_past_appointments: boolean or None
        :param include: (optional) Array of additional information to include.

"appointments":: calendar event time slots for this appointment group
"child_events":: reservations of those time slots
"participant_count":: number of reservations
"reserved_times":: the event id, start time and end time of reservations
                   the current user has made)
"all_context_codes":: all context codes associated with this appointment group
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List appointment groups
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    scope_types = ('reservable', 'manageable')
    include_types = ('appointments', 'child_events', 'participant_count', 'reserved_times', 'all_context_codes')
    utils.validate_attr_is_acceptable(scope, scope_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/appointment_groups'
    payload = {
        'scope': scope,
        'context_codes[]': context_codes,
        'include_past_appointments': include_past_appointments,
        'include[]': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_appointment_group(request_ctx, appointment_group_context_codes, appointment_group_title, appointment_group_sub_context_codes=None, appointment_group_description=None, appointment_group_location_name=None, appointment_group_location_address=None, appointment_group_publish=None, appointment_group_participants_per_appointment=None, appointment_group_min_appointments_per_participant=None, appointment_group_max_appointments_per_participant=None, appointment_group_new_appointments_X=None, appointment_group_participant_visibility=None, **request_kwargs):
    """
    Create and return a new appointment group. If new_appointments are
    specified, the response will return a new_appointments array (same format
    as appointments array, see "List appointment groups" action)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param appointment_group_context_codes: (required) Array of context codes (courses, e.g. course_1) this group should be
linked to (1 or more). Users in the course(s) with appropriate permissions
will be able to sign up for this appointment group.
        :type appointment_group_context_codes: array
        :param appointment_group_title: (required) Short title for the appointment group.
        :type appointment_group_title: string
        :param appointment_group_sub_context_codes: (optional) Array of sub context codes (course sections or a single group category)
this group should be linked to. Used to limit the appointment group to
particular sections. If a group category is specified, students will sign
up in groups and the participant_type will be "Group" instead of "User".
        :type appointment_group_sub_context_codes: array or None
        :param appointment_group_description: (optional) Longer text description of the appointment group.
        :type appointment_group_description: string or None
        :param appointment_group_location_name: (optional) Location name of the appointment group.
        :type appointment_group_location_name: string or None
        :param appointment_group_location_address: (optional) Location address.
        :type appointment_group_location_address: string or None
        :param appointment_group_publish: (optional) Indicates whether this appointment group should be published (i.e. made
available for signup). Once published, an appointment group cannot be
unpublished. Defaults to false.
        :type appointment_group_publish: boolean or None
        :param appointment_group_participants_per_appointment: (optional) Maximum number of participants that may register for each time slot.
Defaults to null (no limit).
        :type appointment_group_participants_per_appointment: integer or None
        :param appointment_group_min_appointments_per_participant: (optional) Minimum number of time slots a user must register for. If not set, users
do not need to sign up for any time slots.
        :type appointment_group_min_appointments_per_participant: integer or None
        :param appointment_group_max_appointments_per_participant: (optional) Maximum number of time slots a user may register for.
        :type appointment_group_max_appointments_per_participant: integer or None
        :param appointment_group_new_appointments_X: (optional) Nested array of start time/end time pairs indicating time slots for this
appointment group. Refer to the example request.
        :type appointment_group_new_appointments_X: array or None
        :param appointment_group_participant_visibility: (optional) "private":: participants cannot see who has signed up for a particular
            time slot
"protected":: participants can see who has signed up.  Defaults to
              "private".
        :type appointment_group_participant_visibility: string or None
        :return: Create an appointment group
        :rtype: requests.Response (with void data)

    """

    appointment_group_participant_visibility_types = ('private', 'protected')
    utils.validate_attr_is_acceptable(appointment_group_participant_visibility, appointment_group_participant_visibility_types)
    path = '/v1/appointment_groups'
    payload = {
        'appointment_group[context_codes][]': appointment_group_context_codes,
        'appointment_group[sub_context_codes][]': appointment_group_sub_context_codes,
        'appointment_group[title]': appointment_group_title,
        'appointment_group[description]': appointment_group_description,
        'appointment_group[location_name]': appointment_group_location_name,
        'appointment_group[location_address]': appointment_group_location_address,
        'appointment_group[publish]': appointment_group_publish,
        'appointment_group[participants_per_appointment]': appointment_group_participants_per_appointment,
        'appointment_group[min_appointments_per_participant]': appointment_group_min_appointments_per_participant,
        'appointment_group[max_appointments_per_participant]': appointment_group_max_appointments_per_participant,
        'appointment_group[new_appointments][X][]': appointment_group_new_appointments_X,
        'appointment_group[participant_visibility]': appointment_group_participant_visibility,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_appointment_group(request_ctx, id, include=None, **request_kwargs):
    """
    Returns information for a single appointment group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param include: (optional) Array of additional information to include. See include[] argument of
"List appointment groups" action.

"child_events":: reservations of time slots time slots
"appointments":: will always be returned
"all_context_codes":: all context codes associated with this appointment group
        :type include: array or None
        :return: Get a single appointment group
        :rtype: requests.Response (with void data)

    """

    include_types = ('child_events', 'appointments', 'all_context_codes')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/appointment_groups/{id}'
    payload = {
        'include[]': include,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_appointment_group(request_ctx, id, appointment_group_context_codes, appointment_group_sub_context_codes=None, appointment_group_title=None, appointment_group_description=None, appointment_group_location_name=None, appointment_group_location_address=None, appointment_group_publish=None, appointment_group_participants_per_appointment=None, appointment_group_min_appointments_per_participant=None, appointment_group_max_appointments_per_participant=None, appointment_group_new_appointments_X=None, appointment_group_participant_visibility=None, **request_kwargs):
    """
    Update and return an appointment group. If new_appointments are specified,
    the response will return a new_appointments array (same format as
    appointments array, see "List appointment groups" action).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param appointment_group_context_codes: (required) Array of context codes (courses, e.g. course_1) this group should be
linked to (1 or more). Users in the course(s) with appropriate permissions
will be able to sign up for this appointment group.
        :type appointment_group_context_codes: array
        :param appointment_group_sub_context_codes: (optional) Array of sub context codes (course sections or a single group category)
this group should be linked to. Used to limit the appointment group to
particular sections. If a group category is specified, students will sign
up in groups and the participant_type will be "Group" instead of "User".
        :type appointment_group_sub_context_codes: array or None
        :param appointment_group_title: (optional) Short title for the appointment group.
        :type appointment_group_title: string or None
        :param appointment_group_description: (optional) Longer text description of the appointment group.
        :type appointment_group_description: string or None
        :param appointment_group_location_name: (optional) Location name of the appointment group.
        :type appointment_group_location_name: string or None
        :param appointment_group_location_address: (optional) Location address.
        :type appointment_group_location_address: string or None
        :param appointment_group_publish: (optional) Indicates whether this appointment group should be published (i.e. made
available for signup). Once published, an appointment group cannot be
unpublished. Defaults to false.
        :type appointment_group_publish: boolean or None
        :param appointment_group_participants_per_appointment: (optional) Maximum number of participants that may register for each time slot.
Defaults to null (no limit).
        :type appointment_group_participants_per_appointment: integer or None
        :param appointment_group_min_appointments_per_participant: (optional) Minimum number of time slots a user must register for. If not set, users
do not need to sign up for any time slots.
        :type appointment_group_min_appointments_per_participant: integer or None
        :param appointment_group_max_appointments_per_participant: (optional) Maximum number of time slots a user may register for.
        :type appointment_group_max_appointments_per_participant: integer or None
        :param appointment_group_new_appointments_X: (optional) Nested array of start time/end time pairs indicating time slots for this
appointment group. Refer to the example request.
        :type appointment_group_new_appointments_X: array or None
        :param appointment_group_participant_visibility: (optional) "private":: participants cannot see who has signed up for a particular
            time slot
"protected":: participants can see who has signed up. Defaults to "private".
        :type appointment_group_participant_visibility: string or None
        :return: Update an appointment group
        :rtype: requests.Response (with void data)

    """

    appointment_group_participant_visibility_types = ('private', 'protected')
    utils.validate_attr_is_acceptable(appointment_group_participant_visibility, appointment_group_participant_visibility_types)
    path = '/v1/appointment_groups/{id}'
    payload = {
        'appointment_group[context_codes][]': appointment_group_context_codes,
        'appointment_group[sub_context_codes][]': appointment_group_sub_context_codes,
        'appointment_group[title]': appointment_group_title,
        'appointment_group[description]': appointment_group_description,
        'appointment_group[location_name]': appointment_group_location_name,
        'appointment_group[location_address]': appointment_group_location_address,
        'appointment_group[publish]': appointment_group_publish,
        'appointment_group[participants_per_appointment]': appointment_group_participants_per_appointment,
        'appointment_group[min_appointments_per_participant]': appointment_group_min_appointments_per_participant,
        'appointment_group[max_appointments_per_participant]': appointment_group_max_appointments_per_participant,
        'appointment_group[new_appointments][X][]': appointment_group_new_appointments_X,
        'appointment_group[participant_visibility]': appointment_group_participant_visibility,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_appointment_group(request_ctx, id, cancel_reason=None, **request_kwargs):
    """
    Delete an appointment group (and associated time slots and reservations)
    and return the deleted group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param cancel_reason: (optional) Reason for deleting/canceling the appointment group.
        :type cancel_reason: string or None
        :return: Delete an appointment group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/appointment_groups/{id}'
    payload = {
        'cancel_reason': cancel_reason,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_user_participants(request_ctx, id, registration_status=None, per_page=None, **request_kwargs):
    """
    List users that are (or may be) participating in this appointment group.
    Refer to the Users API for the response fields. Returns no results for
    appointment groups with the "Group" participant_type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param registration_status: (optional) Limits results to the a given participation status, defaults to "all"
        :type registration_status: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List user participants
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    registration_status_types = ('all', 'registered', 'registered')
    utils.validate_attr_is_acceptable(registration_status, registration_status_types)
    path = '/v1/appointment_groups/{id}/users'
    payload = {
        'registration_status': registration_status,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_student_group_participants(request_ctx, id, registration_status=None, per_page=None, **request_kwargs):
    """
    List student groups that are (or may be) participating in this appointment
    group. Refer to the Groups API for the response fields. Returns no results
    for appointment groups with the "User" participant_type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param registration_status: (optional) Limits results to the a given participation status, defaults to "all"
        :type registration_status: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List student group participants
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    registration_status_types = ('all', 'registered', 'registered')
    utils.validate_attr_is_acceptable(registration_status, registration_status_types)
    path = '/v1/appointment_groups/{id}/groups'
    payload = {
        'registration_status': registration_status,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_next_appointment(request_ctx, appointment_group_ids=None, per_page=None, **request_kwargs):
    """
    Return the next appointment available to sign up for. The appointment
    is returned in a one-element array. If no future appointments are
    available, an empty array is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param appointment_group_ids: (optional) List of ids of appointment groups to search.
        :type appointment_group_ids: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get next appointment
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/appointment_groups/next_appointment'
    payload = {
        'appointment_group_ids[]': appointment_group_ids,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


