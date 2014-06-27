from .. import client, utils


def list_course_sections(request_ctx, course_id, include=None, per_page=None, **request_kwargs):
    """
    Returns the list of sections for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param str course_id: ID
        :param include: (optional) - "students": Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned.
        :type include: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List course sections
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('students', 'avatar_url')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/sections'
    payload = {
        'include': include,
        'per_page': per_page,
    }
    response = client.get(request_ctx, path.format(course_id=course_id), payload=payload, **request_kwargs)

    return response


def create_course_section(request_ctx, course_id, name, sis_section_id=None, start_at=None, end_at=None, **request_kwargs):
    """
    Creates a new section for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param name: (required) The name of the section
        :type name: string
        :param sis_section_id: (optional) The sis ID of the section
        :type sis_section_id: string or None
        :param start_at: (optional) Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type start_at: datetime or None
        :param end_at: (optional) Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type end_at: datetime or None
        :return: Create course section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/courses/{course_id}/sections'
    payload = {
        'course_section[name]': name,
        'course_section[sis_section_id]': sis_section_id,
        'course_section[start_at]': start_at,
        'course_section[end_at]': end_at,
    }
    response = client.post(request_ctx, path.format(course_id=course_id), payload=payload, **request_kwargs)

    return response


def edit_section(request_ctx, id, **request_kwargs):
    """
    Modify an existing section. See the documentation for {api:SectionsController#create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Edit a section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}'
    response = client.put(request_ctx, path.format(id=id), **request_kwargs)

    return response


def delete_section(request_ctx, id, **request_kwargs):
    """
    Delete an existing section.  Returns the former Section.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete a section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}'
    response = client.delete(request_ctx, path.format(id=id), **request_kwargs)

    return response
