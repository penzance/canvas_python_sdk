from canvas_sdk import client, utils

def list_favorite_courses(request_ctx, per_page=None, **request_kwargs):
    """
    Retrieve the list of favorite courses for the current user. If the user has not chosen
    any favorites, then a selection of currently enrolled courses will be returned.
    
    See the {api:CoursesController#index List courses API} for details on accepted include[] parameters.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List favorite courses
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/self/favorites/courses'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def add_course_to_favorites(request_ctx, id, **request_kwargs):
    """
    Add a course to the current user's favorites.  If the course is already
    in the user's favorites, nothing happens.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) The ID or SIS ID of the course to add. The current user must be registered in the course.
        :type id: string
        :return: Add course to favorites
        :rtype: requests.Response (with Favorite data)

    """

    path = '/v1/users/self/favorites/courses/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def remove_course_from_favorites(request_ctx, id, **request_kwargs):
    """
    Remove a course from the current user's favorites.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) the ID or SIS ID of the course to remove
        :type id: string
        :return: Remove course from favorites
        :rtype: requests.Response (with Favorite data)

    """

    path = '/v1/users/self/favorites/courses/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def reset_course_favorites(request_ctx, **request_kwargs):
    """
    Reset the current user's course favorites to the default
    automatically generated list of enrolled courses

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :return: Reset course favorites
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/favorites/courses'
    url = request_ctx.base_api_url + path.format()
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


