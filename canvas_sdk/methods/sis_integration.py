from canvas_sdk import client, utils


def retrieve_assignments_enabled_for_grade_export_to_sis_accounts(request_ctx, account_id, course_id=None, starts_before=None, ends_after=None, include=None, **request_kwargs):
    """
    Retrieve a list of published assignments flagged as "post_to_sis". Assignment group and section information are
    included for convenience.
    
    Each section includes course information for the origin course and the cross-listed course, if applicable. The
    `origin_course` is the course to which the section belongs or the course from which the section was cross-listed.
    Generally, the `origin_course` should be preferred when performing integration work. The `xlist_course` is provided
    for consistency and is only present when the section has been cross-listed.
    
    The `override` is only provided if the Differentiated Assignments course feature is turned on and the assignment
    has an override for that section. When there is an override for the assignment the override object's keys/values can
    be merged with the top level assignment object to create a view of the assignment object specific to that section.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The ID of the account to query.
        :type account_id: integer
        :param course_id: (optional) The ID of the course to query.
        :type course_id: integer or None
        :param starts_before: (optional) When searching on an account, restricts to courses that start before
this date (if they have a start date)
        :type starts_before: DateTime or None
        :param ends_after: (optional) When searching on an account, restricts to courses that end after this
date (if they have an end date)
        :type ends_after: DateTime or None
        :param include: (optional) Array of additional information to include.

"student_overrides":: returns individual student override information
        :type include: string or None
        :return: Retrieve assignments enabled for grade export to SIS
        :rtype: requests.Response (with void data)

    """

    include_types = ('student_overrides')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/sis/accounts/{account_id}/assignments'
    payload = {
        'course_id': course_id,
        'starts_before': starts_before,
        'ends_after': ends_after,
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def retrieve_assignments_enabled_for_grade_export_to_sis_courses(request_ctx, course_id, account_id=None, starts_before=None, ends_after=None, include=None, **request_kwargs):
    """
    Retrieve a list of published assignments flagged as "post_to_sis". Assignment group and section information are
    included for convenience.
    
    Each section includes course information for the origin course and the cross-listed course, if applicable. The
    `origin_course` is the course to which the section belongs or the course from which the section was cross-listed.
    Generally, the `origin_course` should be preferred when performing integration work. The `xlist_course` is provided
    for consistency and is only present when the section has been cross-listed.
    
    The `override` is only provided if the Differentiated Assignments course feature is turned on and the assignment
    has an override for that section. When there is an override for the assignment the override object's keys/values can
    be merged with the top level assignment object to create a view of the assignment object specific to that section.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) The ID of the course to query.
        :type course_id: integer
        :param account_id: (optional) The ID of the account to query.
        :type account_id: integer or None
        :param starts_before: (optional) When searching on an account, restricts to courses that start before
this date (if they have a start date)
        :type starts_before: DateTime or None
        :param ends_after: (optional) When searching on an account, restricts to courses that end after this
date (if they have an end date)
        :type ends_after: DateTime or None
        :param include: (optional) Array of additional information to include.

"student_overrides":: returns individual student override information
        :type include: string or None
        :return: Retrieve assignments enabled for grade export to SIS
        :rtype: requests.Response (with void data)

    """

    include_types = ('student_overrides')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/sis/courses/{course_id}/assignments'
    payload = {
        'account_id': account_id,
        'starts_before': starts_before,
        'ends_after': ends_after,
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


