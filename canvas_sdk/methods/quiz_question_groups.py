from canvas_sdk import client, utils

def create_question_group(request_ctx, course_id, quiz_id, quiz_groups_name=None, quiz_groups_pick_count=None, quiz_groups_question_points=None, quiz_groups_assessment_question_bank_id=None, **request_kwargs):
    """
    Create a new question group for this quiz
    
    <b>201 Created</b> response code is returned if the creation was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param quiz_groups_name: (optional) The name of the question group.
        :type quiz_groups_name: string or None
        :param quiz_groups_pick_count: (optional) The number of questions to randomly select for this group.
        :type quiz_groups_pick_count: integer or None
        :param quiz_groups_question_points: (optional) The number of points to assign to each question in the group.
        :type quiz_groups_question_points: integer or None
        :param quiz_groups_assessment_question_bank_id: (optional) The id of the assessment question bank to pull questions from.
        :type quiz_groups_assessment_question_bank_id: integer or None
        :return: Create a question group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups'
    payload = {
        'quiz_groups[name]' : quiz_groups_name,
        'quiz_groups[pick_count]' : quiz_groups_pick_count,
        'quiz_groups[question_points]' : quiz_groups_question_points,
        'quiz_groups[assessment_question_bank_id]' : quiz_groups_assessment_question_bank_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_question_group(request_ctx, course_id, quiz_id, id, quiz_groups_name=None, quiz_groups_pick_count=None, quiz_groups_question_points=None, **request_kwargs):
    """
    Update a question group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param quiz_groups_name: (optional) The name of the question group.
        :type quiz_groups_name: string or None
        :param quiz_groups_pick_count: (optional) The number of questions to randomly select for this group.
        :type quiz_groups_pick_count: integer or None
        :param quiz_groups_question_points: (optional) The number of points to assign to each question in the group.
        :type quiz_groups_question_points: integer or None
        :return: Update a question group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'
    payload = {
        'quiz_groups[name]' : quiz_groups_name,
        'quiz_groups[pick_count]' : quiz_groups_pick_count,
        'quiz_groups[question_points]' : quiz_groups_question_points,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_question_group(request_ctx, course_id, quiz_id, id, **request_kwargs):
    """
    Delete a question group
    
    <b>204 No Content<b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a question group
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def reorder_question_groups(request_ctx, course_id, quiz_id, id, order_id, order_type, **request_kwargs):
    """
    Change the order of the quiz questions within the group
    
    <b>204 No Content<b> response code is returned if the reorder was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param order_id: (required) The associated item's unique identifier
        :type order_id: integer
        :param order_type: (required) The type of item is always 'question' for a group
        :type order_type: string
        :return: Reorder question groups
        :rtype: requests.Response (with void data)

    """

    type_types = ('question')
    utils.validate_attr_is_acceptable(type, type_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder'
    payload = {
        'order[id]' : order_id,
        'order[type]' : order_type,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


