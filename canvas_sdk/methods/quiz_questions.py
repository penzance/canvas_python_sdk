from canvas_sdk import client, utils


def list_questions_in_quiz_or_submission(request_ctx, course_id, quiz_id, quiz_submission_id=None, quiz_submission_attempt=None, per_page=None, **request_kwargs):
    """
    Returns the list of QuizQuestions in this quiz.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param quiz_submission_id: (optional) If specified, the endpoint will return the questions that were presented
for that submission. This is useful if the quiz has been modified after
the submission was created and the latest quiz version's set of questions
does not match the submission's.
NOTE: you must specify quiz_submission_attempt as well if you specify this
parameter.
        :type quiz_submission_id: integer or None
        :param quiz_submission_attempt: (optional) The attempt of the submission you want the questions for.
        :type quiz_submission_attempt: integer or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List questions in a quiz or a submission
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/questions'
    payload = {
        'quiz_submission_id': quiz_submission_id,
        'quiz_submission_attempt': quiz_submission_attempt,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_quiz_question(request_ctx, course_id, quiz_id, id, **request_kwargs):
    """
    Returns the quiz question with the given id

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param id: (required) The quiz question unique identifier.
        :type id: integer
        :return: Get a single quiz question
        :rtype: requests.Response (with QuizQuestion data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_single_quiz_question(request_ctx, course_id, quiz_id, question_question_name=None, question_question_text=None, question_quiz_group_id=None, question_question_type=None, question_position=None, question_points_possible=None, question_correct_comments=None, question_incorrect_comments=None, question_neutral_comments=None, question_text_after_answers=None, question_answers=None, **request_kwargs):
    """
    Create a new quiz question for this quiz

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param question_question_name: (optional) The name of the question.
        :type question_question_name: string or None
        :param question_question_text: (optional) The text of the question.
        :type question_question_text: string or None
        :param question_quiz_group_id: (optional) The id of the quiz group to assign the question to.
        :type question_quiz_group_id: integer or None
        :param question_question_type: (optional) The type of question. Multiple optional fields depend upon the type of question to be used.
        :type question_question_type: string or None
        :param question_position: (optional) The order in which the question will be displayed in the quiz in relation to other questions.
        :type question_position: integer or None
        :param question_points_possible: (optional) The maximum amount of points received for answering this question correctly.
        :type question_points_possible: integer or None
        :param question_correct_comments: (optional) The comment to display if the student answers the question correctly.
        :type question_correct_comments: string or None
        :param question_incorrect_comments: (optional) The comment to display if the student answers incorrectly.
        :type question_incorrect_comments: string or None
        :param question_neutral_comments: (optional) The comment to display regardless of how the student answered.
        :type question_neutral_comments: string or None
        :param question_text_after_answers: (optional) no description
        :type question_text_after_answers: string or None
        :param question_answers: (optional) no description
        :type question_answers: [Answer] or None
        :return: Create a single quiz question
        :rtype: requests.Response (with QuizQuestion data)

    """

    question_question_type_types = ('calculated_question', 'essay_question', 'file_upload_question', 'fill_in_multiple_blanks_question', 'matching_question', 'multiple_answers_question', 'multiple_choice_question', 'multiple_dropdowns_question', 'numerical_question', 'short_answer_question', 'text_only_question', 'true_false_question')
    utils.validate_attr_is_acceptable(question_question_type, question_question_type_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/questions'
    payload = {
        'question[question_name]': question_question_name,
        'question[question_text]': question_question_text,
        'question[quiz_group_id]': question_quiz_group_id,
        'question[question_type]': question_question_type,
        'question[position]': question_position,
        'question[points_possible]': question_points_possible,
        'question[correct_comments]': question_correct_comments,
        'question[incorrect_comments]': question_incorrect_comments,
        'question[neutral_comments]': question_neutral_comments,
        'question[text_after_answers]': question_text_after_answers,
        'question[answers]': question_answers,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_existing_quiz_question(request_ctx, course_id, quiz_id, id, question_question_name=None, question_question_text=None, question_quiz_group_id=None, question_question_type=None, question_position=None, question_points_possible=None, question_correct_comments=None, question_incorrect_comments=None, question_neutral_comments=None, question_text_after_answers=None, question_answers=None, **request_kwargs):
    """
    Updates an existing quiz question for this quiz

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) The associated quiz's unique identifier.
        :type quiz_id: integer
        :param id: (required) The quiz question's unique identifier.
        :type id: integer
        :param question_question_name: (optional) The name of the question.
        :type question_question_name: string or None
        :param question_question_text: (optional) The text of the question.
        :type question_question_text: string or None
        :param question_quiz_group_id: (optional) The id of the quiz group to assign the question to.
        :type question_quiz_group_id: integer or None
        :param question_question_type: (optional) The type of question. Multiple optional fields depend upon the type of question to be used.
        :type question_question_type: string or None
        :param question_position: (optional) The order in which the question will be displayed in the quiz in relation to other questions.
        :type question_position: integer or None
        :param question_points_possible: (optional) The maximum amount of points received for answering this question correctly.
        :type question_points_possible: integer or None
        :param question_correct_comments: (optional) The comment to display if the student answers the question correctly.
        :type question_correct_comments: string or None
        :param question_incorrect_comments: (optional) The comment to display if the student answers incorrectly.
        :type question_incorrect_comments: string or None
        :param question_neutral_comments: (optional) The comment to display regardless of how the student answered.
        :type question_neutral_comments: string or None
        :param question_text_after_answers: (optional) no description
        :type question_text_after_answers: string or None
        :param question_answers: (optional) no description
        :type question_answers: [Answer] or None
        :return: Update an existing quiz question
        :rtype: requests.Response (with QuizQuestion data)

    """

    question_question_type_types = ('calculated_question', 'essay_question', 'file_upload_question', 'fill_in_multiple_blanks_question', 'matching_question', 'multiple_answers_question', 'multiple_choice_question', 'multiple_dropdowns_question', 'numerical_question', 'short_answer_question', 'text_only_question', 'true_false_question')
    utils.validate_attr_is_acceptable(question_question_type, question_question_type_types)
    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}'
    payload = {
        'question[question_name]': question_question_name,
        'question[question_text]': question_question_text,
        'question[quiz_group_id]': question_quiz_group_id,
        'question[question_type]': question_question_type,
        'question[position]': question_position,
        'question[points_possible]': question_points_possible,
        'question[correct_comments]': question_correct_comments,
        'question[incorrect_comments]': question_incorrect_comments,
        'question[neutral_comments]': question_neutral_comments,
        'question[text_after_answers]': question_text_after_answers,
        'question[answers]': question_answers,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_quiz_question(request_ctx, course_id, quiz_id, id, **request_kwargs):
    """
    <b>204 No Content</b> response code is returned if the deletion was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) The associated quiz's unique identifier
        :type quiz_id: integer
        :param id: (required) The quiz question's unique identifier
        :type id: integer
        :return: Delete a quiz question
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


