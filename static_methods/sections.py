
def edit_section(request_ctx, id, course_section_name=None, course_section_sis_section_id=None, course_section_start_at=None, course_section_end_at=None, **request_kwargs):
    """
    Modify an existing section. See the documentation for `SectionsController#create <https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb>`_.
    :param request_ctx: The request context
    :type request_ctx: :class:RequestContext
    :param id: (required) ID
    :type id: string
    :param course_section_name: (optional) The name of the section
    :type course_section_name: string or None
    :param course_section_sis_section_id: (optional) The sis ID of the section
    :type course_section_sis_section_id: string or None
    :param course_section_start_at: (optional) Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z
    :type course_section_start_at: datetime or None
    :param course_section_end_at: (optional) Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z
    :type course_section_end_at: datetime or None
    :return: Edit a section
    :rtype: requests.Response (with Section data)
    """
    path = '/v1/sections/{id}'
    payload = {
        'course_section[name]' : course_section_name,
        'course_section[sis_section_id]' : course_section_sis_section_id,
        'course_section[start_at]' : course_section_start_at,
        'course_section[end_at]' : course_section_end_at,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)
    return response

