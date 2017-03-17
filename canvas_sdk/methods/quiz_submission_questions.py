from canvas_sdk import client, utils


def get_all_quiz_submission_questions(request_ctx, quiz_submission_id, include=None, **request_kwargs):
    """
    Get a list of all the question records for this quiz submission.
    
    <b>200 OK</b> response code is returned if the request was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param quiz_submission_id: (required) ID
        :type quiz_submission_id: string
        :param include: (optional) Associations to include with the quiz submission question.
        :type include: array or None
        :return: Get all quiz submission questions.
        :rtype: requests.Response (with void data)

    """

    include_types = ('quiz_question')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/quiz_submissions/{quiz_submission_id}/questions'
    payload = {
        'include[]': include,
    }
    url = request_ctx.base_api_url + path.format(quiz_submission_id=quiz_submission_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def answering_questions(request_ctx, quiz_submission_id, attempt, validation_token, access_code=None, quiz_questions=None, per_page=None, **request_kwargs):
    """
    Provide or update an answer to one or more QuizQuestions.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param quiz_submission_id: (required) ID
        :type quiz_submission_id: string
        :param attempt: (required) The attempt number of the quiz submission being taken. Note that this
must be the latest attempt index, as questions for earlier attempts can
not be modified.
        :type attempt: integer
        :param validation_token: (required) The unique validation token you received when the Quiz Submission was
created.
        :type validation_token: string
        :param access_code: (optional) Access code for the Quiz, if any.
        :type access_code: string or None
        :param quiz_questions: (optional) Set of question IDs and the answer value.

See {Appendix: Question Answer Formats} for the accepted answer formats
for each question type.
        :type quiz_questions: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Answering questions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/quiz_submissions/{quiz_submission_id}/questions'
    payload = {
        'attempt': attempt,
        'validation_token': validation_token,
        'access_code': access_code,
        'quiz_questions[]': quiz_questions,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(quiz_submission_id=quiz_submission_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def flagging_question(request_ctx, quiz_submission_id, id, attempt, validation_token, access_code=None, **request_kwargs):
    """
    Set a flag on a quiz question to indicate that you want to return to it
    later.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param quiz_submission_id: (required) ID
        :type quiz_submission_id: string
        :param id: (required) ID
        :type id: string
        :param attempt: (required) The attempt number of the quiz submission being taken. Note that this
must be the latest attempt index, as questions for earlier attempts can
not be modified.
        :type attempt: integer
        :param validation_token: (required) The unique validation token you received when the Quiz Submission was
created.
        :type validation_token: string
        :param access_code: (optional) Access code for the Quiz, if any.
        :type access_code: string or None
        :return: Flagging a question.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag'
    payload = {
        'attempt': attempt,
        'validation_token': validation_token,
        'access_code': access_code,
    }
    url = request_ctx.base_api_url + path.format(quiz_submission_id=quiz_submission_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def unflagging_question(request_ctx, quiz_submission_id, id, attempt, validation_token, access_code=None, **request_kwargs):
    """
    Remove the flag that you previously set on a quiz question after you've
    returned to it.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param quiz_submission_id: (required) ID
        :type quiz_submission_id: string
        :param id: (required) ID
        :type id: string
        :param attempt: (required) The attempt number of the quiz submission being taken. Note that this
must be the latest attempt index, as questions for earlier attempts can
not be modified.
        :type attempt: integer
        :param validation_token: (required) The unique validation token you received when the Quiz Submission was
created.
        :type validation_token: string
        :param access_code: (optional) Access code for the Quiz, if any.
        :type access_code: string or None
        :return: Unflagging a question.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag'
    payload = {
        'attempt': attempt,
        'validation_token': validation_token,
        'access_code': access_code,
    }
    url = request_ctx.base_api_url + path.format(quiz_submission_id=quiz_submission_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


