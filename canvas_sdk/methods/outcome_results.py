from canvas_sdk import client, utils


def get_outcome_results(request_ctx, course_id, user_ids=None, outcome_ids=None, include=None, **request_kwargs):
    """
    Gets the outcome results for users and outcomes in the specified context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param user_ids: (optional) If specified, only the users whose ids are given will be included in the
results. SIS ids can be used, prefixed by "sis_user_id:".
It is an error to specify an id for a user who is not a student in
the context.
        :type user_ids: array or None
        :param outcome_ids: (optional) If specified, only the outcomes whose ids are given will be included in the
results. it is an error to specify an id for an outcome which is not linked
to the context.
        :type outcome_ids: array or None
        :param include: (optional) [String, "alignments"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
Specify additional collections to be side loaded with the result.
"alignments" includes only the alignments referenced by the returned
results.
"outcomes.alignments" includes all alignments referenced by outcomes in the
context.
        :type include: array or None
        :return: Get outcome results
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/outcome_results'
    payload = {
        'user_ids[]': user_ids,
        'outcome_ids[]': outcome_ids,
        'include[]': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_outcome_result_rollups(request_ctx, course_id, aggregate=None, user_ids=None, outcome_ids=None, include=None, **request_kwargs):
    """
    Gets the outcome rollups for the users and outcomes in the specified
    context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param aggregate: (optional) If specified, instead of returning one rollup for each user, all the user
rollups will be combined into one rollup for the course that will contain
the average rollup score for each outcome.
        :type aggregate: string or None
        :param user_ids: (optional) If specified, only the users whose ids are given will be included in the
results or used in an aggregate result. it is an error to specify an id
for a user who is not a student in the context
        :type user_ids: array or None
        :param outcome_ids: (optional) If specified, only the outcomes whose ids are given will be included in the
results. it is an error to specify an id for an outcome which is not linked
to the context.
        :type outcome_ids: array or None
        :param include: (optional) [String, "courses"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
Specify additional collections to be side loaded with the result.
        :type include: array or None
        :return: Get outcome result rollups
        :rtype: requests.Response (with void data)

    """

    aggregate_types = ('course')
    utils.validate_attr_is_acceptable(aggregate, aggregate_types)
    path = '/v1/courses/{course_id}/outcome_rollups'
    payload = {
        'aggregate': aggregate,
        'user_ids[]': user_ids,
        'outcome_ids[]': outcome_ids,
        'include[]': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


