from canvas_sdk import client, utils

def get_all_quiz_submissions(request_ctx, course_id, quiz_id, include, **request_kwargs):
    """
    Get a list of all submissions for this quiz.
    
    <b>200 OK</b> response code is returned if the request was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param include: (required) Associations to include with the quiz submission.
        :type include: string
        :return: Get all quiz submissions.
        :rtype: requests.Response (with void data)

    """

    include_types = ('submission', 'quiz', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_quiz_submission(request_ctx, course_id, quiz_id, id, include, **request_kwargs):
    """
    Get a single quiz submission.
    
    <b>200 OK</b> response code is returned if the request was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param include: (required) Associations to include with the quiz submission.
        :type include: string
        :return: Get a single quiz submission.
        :rtype: requests.Response (with void data)

    """

    include_types = ('submission', 'quiz', 'user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_quiz_submission_start_quiz_taking_session(request_ctx, course_id, quiz_id, access_code=None, preview=None, **request_kwargs):
    """
    Start taking a Quiz by creating a QuizSubmission which you can use to answer
    questions and submit your answers.
    
    <b>Responses</b>
    
    * <b>200 OK</b> if the request was successful
    * <b>400 Bad Request</b> if the quiz is locked
    * <b>403 Forbidden</b> if an invalid access code is specified
    * <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
    * <b>409 Conflict</b> if a QuizSubmission already exists for this user and quiz

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param access_code: (optional) Access code for the Quiz, if any.
        :type access_code: string or None
        :param preview: (optional) Whether this should be a preview QuizSubmission and not count towards the user's course record. Teachers only.
        :type preview: boolean or None
        :return: Create the quiz submission (start a quiz-taking session)
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions'
    payload = {
        'access_code' : access_code,
        'preview' : preview,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_student_question_scores_and_comments(request_ctx, course_id, quiz_id, id, attempt, fudge_points=None, questions=None, **request_kwargs):
    """
    Update the amount of points a student has scored for questions they've
    answered, provide comments for the student about their answer(s), or simply
    fudge the total score by a specific amount of points.
    
    <b>Responses</b>
    
    * <b>200 OK</b> if the request was successful
    * <b>403 Forbidden</b> if you are not a teacher in this course
    * <b>400 Bad Request</b> if the attempt parameter is missing or invalid
    * <b>400 Bad Request</b> if the specified QS attempt is not yet complete

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param attempt: (required) The attempt number of the quiz submission that should be updated. This attempt MUST be already completed.
        :type attempt: integer
        :param fudge_points: (optional) Amount of positive or negative points to fudge the total score by.
        :type fudge_points: float or None
        :param questions: (optional) A set of scores and comments for each question answered by the student. The keys are the question IDs, and the values are hashes of `score` and `comment` entries. See {Appendix: Manual Scoring} for more on this parameter.
        :type questions: hash or None
        :return: Update student question scores and comments.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}'
    payload = {
        'attempt' : attempt,
        'fudge_points' : fudge_points,
        'questions' : questions,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def complete_quiz_submission_turn_it_in(request_ctx, course_id, quiz_id, id, attempt, validation_token, access_code=None, **request_kwargs):
    """
    Complete the quiz submission by marking it as complete and grading it. When
    the quiz submission has been marked as complete, no further modifications
    will be allowed.
    
    <b>Responses</b>
    
    * <b>200 OK</b> if the request was successful
    * <b>403 Forbidden</b> if an invalid access code is specified
    * <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
    * <b>403 Forbidden</b> if an invalid token is specified
    * <b>400 Bad Request</b> if the QS is already complete
    * <b>400 Bad Request</b> if the attempt parameter is missing
    * <b>400 Bad Request</b> if the attempt parameter is not the latest attempt

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) ID
        :type id: string
        :param attempt: (required) The attempt number of the quiz submission that should be completed. Note that this must be the latest attempt index, as earlier attempts can not be modified.
        :type attempt: integer
        :param validation_token: (required) The unique validation token you received when this Quiz Submission was created.
        :type validation_token: string
        :param access_code: (optional) Access code for the Quiz, if any.
        :type access_code: string or None
        :return: Complete the quiz submission (turn it in).
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete'
    payload = {
        'attempt' : attempt,
        'validation_token' : validation_token,
        'access_code' : access_code,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


