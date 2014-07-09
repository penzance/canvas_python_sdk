from canvas_sdk import client, utils

def list_course_sections(request_ctx, course_id, include=None, per_page=None, **request_kwargs):
    """
    Returns the list of sections for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
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
        'include' : include,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_course_section(request_ctx, course_id, course_section_name, course_section_sis_section_id=None, course_section_start_at=None, course_section_end_at=None, **request_kwargs):
    """
    Creates a new section for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param course_section_name: (required) The name of the section
        :type course_section_name: string
        :param course_section_sis_section_id: (optional) The sis ID of the section
        :type course_section_sis_section_id: string or None
        :param course_section_start_at: (optional) Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        :type course_section_start_at: datetime or None
        :param course_section_end_at: (optional) Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        :type course_section_end_at: datetime or None
        :return: Create course section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/courses/{course_id}/sections'
    payload = {
        'course_section[name]' : course_section_name,
        'course_section[sis_section_id]' : course_section_sis_section_id,
        'course_section[start_at]' : course_section_start_at,
        'course_section[end_at]' : course_section_end_at,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def cross_list_section(request_ctx, id, new_course_id, **request_kwargs):
    """
    Move the Section to another course.  The new course may be in a different account (department),
    but must belong to the same root account (institution).

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param new_course_id: (required) ID
        :type new_course_id: string
        :return: Cross-list a Section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}/crosslist/{new_course_id}'
    url = request_ctx.base_api_url + path.format(id=id, new_course_id=new_course_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def de_cross_list_section(request_ctx, id, **request_kwargs):
    """
    Undo cross-listing of a Section, returning it to its original course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: De-cross-list a Section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}/crosslist'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def edit_section(request_ctx, id, **request_kwargs):
    """
    Modify an existing section.  See the documentation for {api:SectionsController#create create API action}.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Edit a section
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def get_section_information_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Gets details about a specific section

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get section information
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/courses/{course_id}/sections/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_section_information_sections(request_ctx, id, **request_kwargs):
    """
    Gets details about a specific section

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get section information
        :rtype: requests.Response (with Section data)

    """

    path = '/v1/sections/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

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
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


