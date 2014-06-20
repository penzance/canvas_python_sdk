from canvas_sdk import client, utils, config

def list_course_sections(course_id, include=None, per_page=None):
    """
    Returns the list of sections for this course.

        :param course_id: (required) ID
        :type course_id: string
        :param include: (optional) - "students": Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned.
        :type include: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List course sections
        :rtype: array

    """

    if per_page is None:
        per_page=config.LIMIT_PER_PAGE
    include_types = ('students', 'avatar_url')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/sections'
    payload = {
        'include' : include,
        'per_page' : per_page,
    }
    response = client.get(utils.build_url(path.format(course_id=course_id)), payload=payload)

    return response


def create_course_section(course_id, name, sis_section_id=None, start_at=None, end_at=None):
    """
    Creates a new section for this course.

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
        :rtype: Section

    """

    path = '/v1/courses/{course_id}/sections'
    payload = {
        'course_section[name]' : name,
        'course_section[sis_section_id]' : sis_section_id,
        'course_section[start_at]' : start_at,
        'course_section[end_at]' : end_at,
    }
    response = client.post(utils.build_url(path.format(course_id=course_id)), payload=payload)

    return response


def cross_list_section(id, new_course_id):
    """
    Move the Section to another course. The new course may be in a different
    account (department), but must belong to the same root account (institution).

        :param id: (required) ID
        :type id: string
        :param new_course_id: (required) ID
        :type new_course_id: string
        :return: Cross-list a Section
        :rtype: Section

    """

    path = '/v1/sections/{id}/crosslist/{new_course_id}'
    response = client.post(utils.build_url(path.format(id=id, new_course_id=new_course_id)))

    return response


def de_cross_list_section(id):
    """
    Undo cross-listing of a Section, returning it to its original course.

        :param id: (required) ID
        :type id: string
        :return: De-cross-list a Section
        :rtype: Section

    """

    path = '/v1/sections/{id}/crosslist'
    response = client.delete(utils.build_url(path.format(id=id)))

    return response


def edit_section(id):
    """
    Modify an existing section. See the documentation for {api:SectionsController#create

        :param id: (required) ID
        :type id: string
        :return: Edit a section
        :rtype: Section

    """

    path = '/v1/sections/{id}'
    response = client.put(utils.build_url(path.format(id=id)))

    return response


def get_section_information_courses(course_id, id):
    """
    Gets details about a specific section

        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get section information
        :rtype: Section

    """

    path = '/v1/courses/{course_id}/sections/{id}'
    response = client.get(utils.build_url(path.format(course_id=course_id, id=id)))

    return response


def get_section_information_sections(id):
    """
    Gets details about a specific section

        :param id: (required) ID
        :type id: string
        :return: Get section information
        :rtype: Section

    """

    path = '/v1/sections/{id}'
    response = client.get(utils.build_url(path.format(id=id)))

    return response


def delete_section(id):
    """
    Delete an existing section.  Returns the former Section.

        :param id: (required) ID
        :type id: string
        :return: Delete a section
        :rtype: Section

    """

    path = '/v1/sections/{id}'
    response = client.delete(utils.build_url(path.format(id=id)))

    return response


