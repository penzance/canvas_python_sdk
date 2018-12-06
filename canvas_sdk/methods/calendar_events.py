from __future__ import unicode_literals
from canvas_sdk import client, utils

def list_calendar_events(request_ctx, type=None, start_date=None, end_date=None, undated=None, all_events=None, context_codes=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of calendar events or assignments for the current user

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param type: (optional) Defaults to "event"
        :type type: string or None
        :param start_date: (optional) Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        :type start_date: date or None
        :param end_date: (optional) Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned.
        :type end_date: date or None
        :param undated: (optional) Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date.
        :type undated: boolean or None
        :param all_events: (optional) Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria.
        :type all_events: boolean or None
        :param context_codes: (optional) List of context codes of courses/groups/users whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42
        :type context_codes: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List calendar events
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    type_types = ('event', 'assignment')
    utils.validate_attr_is_acceptable(type, type_types)
    path = '/v1/calendar_events'
    payload = {
        'type' : type,
        'start_date' : start_date,
        'end_date' : end_date,
        'undated' : undated,
        'all_events' : all_events,
        'context_codes' : context_codes,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_calendar_event(request_ctx, calendar_event_context_code, calendar_event_title=None, calendar_event_description=None, calendar_event_start_at=None, calendar_event_end_at=None, calendar_event_location_name=None, calendar_event_location_address=None, calendar_event_time_zone_edited=None, calendar_event_child_event_data_X_start_at=None, calendar_event_child_event_data_X_end_at=None, calendar_event_child_event_data_X_context_code=None, **request_kwargs):
    """
    Create and return a new calendar event

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param calendar_event_context_code: (required) Context code of the course/group/user whose calendar this event should be added to.
        :type calendar_event_context_code: string
        :param calendar_event_title: (optional) Short title for the calendar event.
        :type calendar_event_title: string or None
        :param calendar_event_description: (optional) Longer HTML description of the event.
        :type calendar_event_description: string or None
        :param calendar_event_start_at: (optional) Start date/time of the event.
        :type calendar_event_start_at: datetime or None
        :param calendar_event_end_at: (optional) End date/time of the event.
        :type calendar_event_end_at: datetime or None
        :param calendar_event_location_name: (optional) Location name of the event.
        :type calendar_event_location_name: string or None
        :param calendar_event_location_address: (optional) Location address
        :type calendar_event_location_address: string or None
        :param calendar_event_time_zone_edited: (optional) Time zone of the user editing the event. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type calendar_event_time_zone_edited: string or None
        :param calendar_event_child_event_data_X_start_at: (optional) Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start_at, end_at and context_code
        :type calendar_event_child_event_data_X_start_at: datetime or None
        :param calendar_event_child_event_data_X_end_at: (optional) Section-level end time(s) if this is a course event.
        :type calendar_event_child_event_data_X_end_at: datetime or None
        :param calendar_event_child_event_data_X_context_code: (optional) Context code(s) corresponding to the section-level start and end time(s).
        :type calendar_event_child_event_data_X_context_code: string or None
        :return: Create a calendar event
        :rtype: requests.Response (with void data)

    """

    path = '/v1/calendar_events'
    payload = {
        'calendar_event[context_code]' : calendar_event_context_code,
        'calendar_event[title]' : calendar_event_title,
        'calendar_event[description]' : calendar_event_description,
        'calendar_event[start_at]' : calendar_event_start_at,
        'calendar_event[end_at]' : calendar_event_end_at,
        'calendar_event[location_name]' : calendar_event_location_name,
        'calendar_event[location_address]' : calendar_event_location_address,
        'calendar_event[time_zone_edited]' : calendar_event_time_zone_edited,
        'calendar_event[child_event_data][X][start_at]' : calendar_event_child_event_data_X_start_at,
        'calendar_event[child_event_data][X][end_at]' : calendar_event_child_event_data_X_end_at,
        'calendar_event[child_event_data][X][context_code]' : calendar_event_child_event_data_X_context_code,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_calendar_event_or_assignment(request_ctx, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get a single calendar event or assignment
        :rtype: requests.Response (with CalendarEvent data)

    """

    path = '/v1/calendar_events/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def reserve_time_slot(request_ctx, id, participant_id=None, cancel_existing=None, **request_kwargs):
    """
    Reserves a particular time slot and return the new reservation

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param participant_id: (optional) User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user's candidate group).
        :type participant_id: string or None
        :param cancel_existing: (optional) Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group.
        :type cancel_existing: boolean or None
        :return: Reserve a time slot
        :rtype: requests.Response (with void data)

    """

    path = '/v1/calendar_events/{id}/reservations'
    payload = {
        'participant_id' : participant_id,
        'cancel_existing' : cancel_existing,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def reserve_time_slot_participant_id(request_ctx, id, participant_id=None, cancel_existing=None, **request_kwargs):
    """
    Reserves a particular time slot and return the new reservation

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param participant_id: (optional) User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user's candidate group).
        :type participant_id: string or None
        :param cancel_existing: (optional) Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group.
        :type cancel_existing: boolean or None
        :return: Reserve a time slot
        :rtype: requests.Response (with void data)

    """

    path = '/v1/calendar_events/{id}/reservations/{participant_id}'
    payload = {
        'cancel_existing' : cancel_existing,
    }
    url = request_ctx.base_api_url + path.format(id=id, participant_id=participant_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_calendar_event(request_ctx, id, calendar_event_context_code, calendar_event_title=None, calendar_event_description=None, calendar_event_start_at=None, calendar_event_end_at=None, calendar_event_location_name=None, calendar_event_location_address=None, calendar_event_time_zone_edited=None, calendar_event_child_event_data_X_start_at=None, calendar_event_child_event_data_X_end_at=None, calendar_event_child_event_data_X_context_code=None, **request_kwargs):
    """
    Update and return a calendar event

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param calendar_event_context_code: (required) Context code of the course/group/user whose calendar this event should be added to.
        :type calendar_event_context_code: string
        :param calendar_event_title: (optional) Short title for the calendar event.
        :type calendar_event_title: string or None
        :param calendar_event_description: (optional) Longer HTML description of the event.
        :type calendar_event_description: string or None
        :param calendar_event_start_at: (optional) Start date/time of the event.
        :type calendar_event_start_at: datetime or None
        :param calendar_event_end_at: (optional) End date/time of the event.
        :type calendar_event_end_at: datetime or None
        :param calendar_event_location_name: (optional) Location name of the event.
        :type calendar_event_location_name: string or None
        :param calendar_event_location_address: (optional) Location address
        :type calendar_event_location_address: string or None
        :param calendar_event_time_zone_edited: (optional) Time zone of the user editing the event. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        :type calendar_event_time_zone_edited: string or None
        :param calendar_event_child_event_data_X_start_at: (optional) Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start_at, end_at and context_code
        :type calendar_event_child_event_data_X_start_at: datetime or None
        :param calendar_event_child_event_data_X_end_at: (optional) Section-level end time(s) if this is a course event.
        :type calendar_event_child_event_data_X_end_at: datetime or None
        :param calendar_event_child_event_data_X_context_code: (optional) Context code(s) corresponding to the section-level start and end time(s).
        :type calendar_event_child_event_data_X_context_code: string or None
        :return: Update a calendar event
        :rtype: requests.Response (with void data)

    """

    path = '/v1/calendar_events/{id}'
    payload = {
        'calendar_event[context_code]' : calendar_event_context_code,
        'calendar_event[title]' : calendar_event_title,
        'calendar_event[description]' : calendar_event_description,
        'calendar_event[start_at]' : calendar_event_start_at,
        'calendar_event[end_at]' : calendar_event_end_at,
        'calendar_event[location_name]' : calendar_event_location_name,
        'calendar_event[location_address]' : calendar_event_location_address,
        'calendar_event[time_zone_edited]' : calendar_event_time_zone_edited,
        'calendar_event[child_event_data][X][start_at]' : calendar_event_child_event_data_X_start_at,
        'calendar_event[child_event_data][X][end_at]' : calendar_event_child_event_data_X_end_at,
        'calendar_event[child_event_data][X][context_code]' : calendar_event_child_event_data_X_context_code,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_calendar_event(request_ctx, id, cancel_reason=None, **request_kwargs):
    """
    Delete an event from the calendar and return the deleted event

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param cancel_reason: (optional) Reason for deleting/canceling the event.
        :type cancel_reason: string or None
        :return: Delete a calendar event
        :rtype: requests.Response (with void data)

    """

    path = '/v1/calendar_events/{id}'
    payload = {
        'cancel_reason' : cancel_reason,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


