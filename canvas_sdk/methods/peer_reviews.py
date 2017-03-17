from canvas_sdk import client, utils


def get_all_peer_reviews_courses_peer_reviews(request_ctx, course_id, assignment_id, include=None, per_page=None, **request_kwargs):
    """
    Get a list of all Peer Reviews for this assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param include: (optional) Associations to include with the peer review.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all Peer Reviews
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_comments', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews'
    payload = {
        'include[]': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_peer_reviews_sections_peer_reviews(request_ctx, section_id, assignment_id, include=None, per_page=None, **request_kwargs):
    """
    Get a list of all Peer Reviews for this assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param include: (optional) Associations to include with the peer review.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all Peer Reviews
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_comments', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews'
    payload = {
        'include[]': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_peer_reviews_courses_submissions(request_ctx, course_id, assignment_id, submission_id, include=None, per_page=None, **request_kwargs):
    """
    Get a list of all Peer Reviews for this assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param include: (optional) Associations to include with the peer review.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all Peer Reviews
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_comments', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'include[]': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_all_peer_reviews_sections_submissions(request_ctx, section_id, assignment_id, submission_id, include=None, per_page=None, **request_kwargs):
    """
    Get a list of all Peer Reviews for this assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param include: (optional) Associations to include with the peer review.
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get all Peer Reviews
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('submission_comments', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'include[]': include,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_peer_review_courses(request_ctx, course_id, assignment_id, submission_id, user_id, **request_kwargs):
    """
    Create a peer review for the assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param user_id: (required) user_id to assign as reviewer on this assignment
        :type user_id: integer
        :return: Create Peer Review
        :rtype: requests.Response (with PeerReview data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'user_id': user_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_peer_review_sections(request_ctx, section_id, assignment_id, submission_id, user_id, **request_kwargs):
    """
    Create a peer review for the assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param user_id: (required) user_id to assign as reviewer on this assignment
        :type user_id: integer
        :return: Create Peer Review
        :rtype: requests.Response (with PeerReview data)

    """

    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'user_id': user_id,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_peer_review_courses(request_ctx, course_id, assignment_id, submission_id, user_id, **request_kwargs):
    """
    Delete a peer review for the assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param user_id: (required) user_id to delete as reviewer on this assignment
        :type user_id: integer
        :return: Delete Peer Review
        :rtype: requests.Response (with PeerReview data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'user_id': user_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_peer_review_sections(request_ctx, section_id, assignment_id, submission_id, user_id, **request_kwargs):
    """
    Delete a peer review for the assignment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param section_id: (required) ID
        :type section_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param submission_id: (required) ID
        :type submission_id: string
        :param user_id: (required) user_id to delete as reviewer on this assignment
        :type user_id: integer
        :return: Delete Peer Review
        :rtype: requests.Response (with PeerReview data)

    """

    path = '/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews'
    payload = {
        'user_id': user_id,
    }
    url = request_ctx.base_api_url + path.format(section_id=section_id, assignment_id=assignment_id, submission_id=submission_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


