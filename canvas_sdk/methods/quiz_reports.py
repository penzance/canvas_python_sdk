from canvas_sdk import client, utils


def retrieve_all_quiz_reports(request_ctx, course_id, quiz_id, includes_all_versions=None, per_page=None, **request_kwargs):
    """
    Returns a list of all available reports.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param includes_all_versions: (optional) Whether to retrieve reports that consider all the submissions or only
the most recent. Defaults to false, ignored for item_analysis reports.
        :type includes_all_versions: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Retrieve all quiz reports
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/reports'
    payload = {
        'includes_all_versions': includes_all_versions,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_quiz_report(request_ctx, course_id, quiz_id, quiz_report_report_type, quiz_report_includes_all_versions=None, include=None, **request_kwargs):
    """
    Create and return a new report for this quiz. If a previously
    generated report matches the arguments and is still current (i.e.
    there have been no new submissions), it will be returned.
    
    *Responses*
    
    * <code>400 Bad Request</code> if the specified report type is invalid
    * <code>409 Conflict</code> if a quiz report of the specified type is already being
      generated

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param quiz_report_report_type: (required) The type of report to be generated.
        :type quiz_report_report_type: string
        :param quiz_report_includes_all_versions: (optional) Whether the report should consider all submissions or only the most
recent. Defaults to false, ignored for item_analysis.
        :type quiz_report_includes_all_versions: boolean or None
        :param include: (optional) Whether the output should include documents for the file and/or progress
objects associated with this report. (Note: JSON-API only)
        :type include: String[] or None
        :return: Create a quiz report
        :rtype: requests.Response (with QuizReport data)

    """

    quiz_report_report_type_types = ('student_analysis', 'item_analysis')
    include_types = ('file', 'progress')
    utils.validate_attr_is_acceptable(quiz_report_report_type, quiz_report_report_type_types)
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/reports'
    payload = {
        'quiz_report[report_type]': quiz_report_report_type,
        'quiz_report[includes_all_versions]': quiz_report_includes_all_versions,
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_quiz_report(request_ctx, course_id, quiz_id, id, include=None, **request_kwargs):
    """
    Returns the data for a single quiz report.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) Whether the output should include documents for the file and/or progress
objects associated with this report. (Note: JSON-API only)
        :type include: String[] or None
        :return: Get a quiz report
        :rtype: requests.Response (with QuizReport data)

    """

    include_types = ('file', 'progress')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}'
    payload = {
        'include': include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def abort_generation_of_report_or_remove_previously_generated_one(request_ctx, course_id, quiz_id, id, **request_kwargs):
    """
    This API allows you to cancel a previous request you issued for a report to
    be generated. Or in the case of an already generated report, you'd like to
    remove it, perhaps to generate it another time with an updated version that
    provides new features.
    
    You must check the report's generation status before attempting to use this
    interface. See the "workflow_state" property of the QuizReport's Progress
    object for more information. Only when the progress reports itself in a
    "queued" state can the generation be aborted.
    
    *Responses*
    
    - <code>204 No Content</code> if your request was accepted
    - <code>422 Unprocessable Entity</code> if the report is not being generated
      or can not be aborted at this stage

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :return: Abort the generation of a report, or remove a previously generated one
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


