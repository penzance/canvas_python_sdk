from canvas_sdk import client, utils


def get_blueprint_information(request_ctx, course_id, template_id, **request_kwargs):
    """
    Using 'default' as the template_id should suffice for the current implmentation (as there should be only one template per course).
    However, using specific template ids may become necessary in the future

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param template_id: (required) ID
        :type template_id: string
        :return: Get blueprint information
        :rtype: requests.Response (with BlueprintTemplate data)

    """

    path = '/v1/courses/{course_id}/blueprint_templates/{template_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, template_id=template_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_associated_course_information(request_ctx, course_id, template_id, per_page=None, **request_kwargs):
    """
    Returns a list of courses that are configured to receive updates from this blueprint

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param template_id: (required) ID
        :type template_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get associated course information
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, template_id=template_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_associated_courses(request_ctx, course_id, template_id, course_ids_to_add=None, course_ids_to_remove=None, **request_kwargs):
    """
    Send a list of course ids to add or remove new associations for the template.
    Cannot add courses that do not belong to the blueprint course's account. Also cannot add
    other blueprint courses or courses that already have an association with another blueprint course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param template_id: (required) ID
        :type template_id: string
        :param course_ids_to_add: (optional) Courses to add as associated courses
        :type course_ids_to_add: Array or None
        :param course_ids_to_remove: (optional) Courses to remove as associated courses
        :type course_ids_to_remove: Array or None
        :return: Update associated courses
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations'
    payload = {
        'course_ids_to_add': course_ids_to_add,
        'course_ids_to_remove': course_ids_to_remove,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, template_id=template_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


