from canvas_sdk import client, utils, config


def list_course_sections(course_id, include=None, per_page=config.LIMIT_PER_PAGE):
    """
    Returns the list of sections for this course.

    Parameters:
        course_id (string, required): ID
        include (string, optional): "students": Associations to include with the group. 
            Note: this is only available if you have permission to view users or grades in 
            the course - "avatar_url": Include the avatar URLs for students returned.
        per_page (int, optional): The number of results to return. Defaults to config.LIMIT_PER_PAGE.

    """
    
    path = '/v1/courses/{course_id}/sections'
    include_types = ('students', 'avatar_url')
    utils.validate_attr_is_acceptable(include, include_types)
    result = client.get(utils.build_url(path.format(course_id=course_id)),
                        {'include': include, 'per_page': per_page})
    return result
