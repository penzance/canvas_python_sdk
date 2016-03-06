from canvas_sdk import client, utils

def list_quizzes_in_course(request_ctx, course_id, search_term=None, per_page=None, **request_kwargs):
    """
    Returns the list of Quizzes in this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param search_term: (optional) The partial title of the quizzes to match and return.
        :type search_term: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List quizzes in a course
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/quizzes'
    payload = {
        'search_term' : search_term,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_quiz(request_ctx, course_id, id, **request_kwargs):
    """
    Returns the quiz with the given id.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get a single quiz
        :rtype: requests.Response (with Quiz data)

    """

    path = '/v1/courses/{course_id}/quizzes/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_quiz(request_ctx, course_id, quiz_title, quiz_description=None, quiz_quiz_type=None, quiz_assignment_group_id=None, quiz_time_limit=None, quiz_shuffle_answers=None, quiz_hide_results=None, quiz_show_correct_answers=None, quiz_show_correct_answers_last_attempt=None, quiz_show_correct_answers_at=None, quiz_hide_correct_answers_at=None, quiz_allowed_attempts=None, quiz_scoring_policy=None, quiz_one_question_at_a_time=None, quiz_cant_go_back=None, quiz_access_code=None, quiz_ip_filter=None, quiz_due_at=None, quiz_lock_at=None, quiz_unlock_at=None, quiz_published=None, quiz_one_time_results=None, **request_kwargs):
    """
    Create a new quiz for this course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_title: (required) The quiz title.
        :type quiz_title: string
        :param quiz_description: (optional) A description of the quiz.
        :type quiz_description: string or None
        :param quiz_quiz_type: (optional) The type of quiz.
        :type quiz_quiz_type: string or None
        :param quiz_assignment_group_id: (optional) The assignment group id to put the assignment in. Defaults to the top
assignment group in the course. Only valid if the quiz is graded, i.e. if
quiz_type is "assignment" or "graded_survey".
        :type quiz_assignment_group_id: integer or None
        :param quiz_time_limit: (optional) Time limit to take this quiz, in minutes. Set to null for no time limit.
Defaults to null.
        :type quiz_time_limit: integer or None
        :param quiz_shuffle_answers: (optional) If true, quiz answers for multiple choice questions will be randomized for
each student. Defaults to false.
        :type quiz_shuffle_answers: boolean or None
        :param quiz_hide_results: (optional) Dictates whether or not quiz results are hidden from students.
If null, students can see their results after any attempt.
If "always", students can never see their results.
If "until_after_last_attempt", students can only see results after their
last attempt. (Only valid if allowed_attempts > 1). Defaults to null.
        :type quiz_hide_results: string or None
        :param quiz_show_correct_answers: (optional) Only valid if hide_results=null
If false, hides correct answers from students when quiz results are viewed.
Defaults to true.
        :type quiz_show_correct_answers: boolean or None
        :param quiz_show_correct_answers_last_attempt: (optional) Only valid if show_correct_answers=true and allowed_attempts > 1
If true, hides correct answers from students when quiz results are viewed
until they submit the last attempt for the quiz.
Defaults to false.
        :type quiz_show_correct_answers_last_attempt: boolean or None
        :param quiz_show_correct_answers_at: (optional) Only valid if show_correct_answers=true
If set, the correct answers will be visible by students only after this
date, otherwise the correct answers are visible once the student hands in
their quiz submission.
        :type quiz_show_correct_answers_at: DateTime or None
        :param quiz_hide_correct_answers_at: (optional) Only valid if show_correct_answers=true
If set, the correct answers will stop being visible once this date has
passed. Otherwise, the correct answers will be visible indefinitely.
        :type quiz_hide_correct_answers_at: DateTime or None
        :param quiz_allowed_attempts: (optional) Number of times a student is allowed to take a quiz.
Set to -1 for unlimited attempts.
Defaults to 1.
        :type quiz_allowed_attempts: integer or None
        :param quiz_scoring_policy: (optional) Required and only valid if allowed_attempts > 1.
Scoring policy for a quiz that students can take multiple times.
Defaults to "keep_highest".
        :type quiz_scoring_policy: string or None
        :param quiz_one_question_at_a_time: (optional) If true, shows quiz to student one question at a time.
Defaults to false.
        :type quiz_one_question_at_a_time: boolean or None
        :param quiz_cant_go_back: (optional) Only valid if one_question_at_a_time=true
If true, questions are locked after answering.
Defaults to false.
        :type quiz_cant_go_back: boolean or None
        :param quiz_access_code: (optional) Restricts access to the quiz with a password.
For no access code restriction, set to null.
Defaults to null.
        :type quiz_access_code: string or None
        :param quiz_ip_filter: (optional) Restricts access to the quiz to computers in a specified IP range.
Filters can be a comma-separated list of addresses, or an address followed by a mask

Examples:
  "192.168.217.1"
  "192.168.217.1/24"
  "192.168.217.1/255.255.255.0"

For no IP filter restriction, set to null.
Defaults to null.
        :type quiz_ip_filter: string or None
        :param quiz_due_at: (optional) The day/time the quiz is due.
Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        :type quiz_due_at: DateTime or None
        :param quiz_lock_at: (optional) The day/time the quiz is locked for students.
Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        :type quiz_lock_at: DateTime or None
        :param quiz_unlock_at: (optional) The day/time the quiz is unlocked for students.
Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z.
        :type quiz_unlock_at: DateTime or None
        :param quiz_published: (optional) Whether the quiz should have a draft state of published or unpublished.
NOTE: If students have started taking the quiz, or there are any
submissions for the quiz, you may not unpublish a quiz and will recieve
an error.
        :type quiz_published: boolean or None
        :param quiz_one_time_results: (optional) Whether students should be prevented from viewing their quiz results past
the first time (right after they turn the quiz in.)
Only valid if "hide_results" is not set to "always".
Defaults to false.
        :type quiz_one_time_results: boolean or None
        :return: Create a quiz
        :rtype: requests.Response (with Quiz data)

    """

    quiz_quiz_type_types = ('practice_quiz', 'assignment', 'graded_survey', 'survey')
    quiz_hide_results_types = ('always', 'until_after_last_attempt')
    quiz_scoring_policy_types = ('keep_highest', 'keep_latest')
    utils.validate_attr_is_acceptable(quiz_quiz_type, quiz_quiz_type_types)
    utils.validate_attr_is_acceptable(quiz_hide_results, quiz_hide_results_types)
    utils.validate_attr_is_acceptable(quiz_scoring_policy, quiz_scoring_policy_types)
    path = '/v1/courses/{course_id}/quizzes'
    payload = {
        'quiz[title]' : quiz_title,
        'quiz[description]' : quiz_description,
        'quiz[quiz_type]' : quiz_quiz_type,
        'quiz[assignment_group_id]' : quiz_assignment_group_id,
        'quiz[time_limit]' : quiz_time_limit,
        'quiz[shuffle_answers]' : quiz_shuffle_answers,
        'quiz[hide_results]' : quiz_hide_results,
        'quiz[show_correct_answers]' : quiz_show_correct_answers,
        'quiz[show_correct_answers_last_attempt]' : quiz_show_correct_answers_last_attempt,
        'quiz[show_correct_answers_at]' : quiz_show_correct_answers_at,
        'quiz[hide_correct_answers_at]' : quiz_hide_correct_answers_at,
        'quiz[allowed_attempts]' : quiz_allowed_attempts,
        'quiz[scoring_policy]' : quiz_scoring_policy,
        'quiz[one_question_at_a_time]' : quiz_one_question_at_a_time,
        'quiz[cant_go_back]' : quiz_cant_go_back,
        'quiz[access_code]' : quiz_access_code,
        'quiz[ip_filter]' : quiz_ip_filter,
        'quiz[due_at]' : quiz_due_at,
        'quiz[lock_at]' : quiz_lock_at,
        'quiz[unlock_at]' : quiz_unlock_at,
        'quiz[published]' : quiz_published,
        'quiz[one_time_results]' : quiz_one_time_results,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_quiz(request_ctx, course_id, id, quiz_notify_of_update=None, **request_kwargs):
    """
    Modify an existing quiz. See the documentation for quiz creation.
    
    Additional arguments:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param quiz_notify_of_update: (optional) If true, notifies users that the quiz has changed.
Defaults to true
        :type quiz_notify_of_update: boolean or None
        :return: Edit a quiz
        :rtype: requests.Response (with Quiz data)

    """

    path = '/v1/courses/{course_id}/quizzes/{id}'
    payload = {
        'quiz[notify_of_update]' : quiz_notify_of_update,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_quiz(request_ctx, course_id, id, **request_kwargs):
    """

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a quiz
        :rtype: requests.Response (with Quiz data)

    """

    path = '/v1/courses/{course_id}/quizzes/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def reorder_quiz_items(request_ctx, course_id, id, order_id, order_type=None, **request_kwargs):
    """
    Change order of the quiz questions or groups within the quiz
    
    <b>204 No Content</b> response code is returned if the reorder was successful.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param order_id: (required) The associated item's unique identifier
        :type order_id: array
        :param order_type: (optional) The type of item is either 'question' or 'group'
        :type order_type: array or None
        :return: Reorder quiz items
        :rtype: requests.Response (with void data)

    """

    order_type_types = ('question', 'group')
    utils.validate_attr_is_acceptable(order_type, order_type_types)
    path = '/v1/courses/{course_id}/quizzes/{id}/reorder'
    payload = {
        'order[id]' : order_id,
        'order[type]' : order_type,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def validate_quiz_access_code(request_ctx, course_id, id, access_code, **request_kwargs):
    """
    Accepts an access code and returns a boolean indicating whether that access code is correct

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param access_code: (required) The access code being validated
        :type access_code: string
        :return: Validate quiz access code
        :rtype: requests.Response (with boolean data)

    """

    path = '/v1/courses/{course_id}/quizzes/{id}/validate_access_code'
    payload = {
        'access_code' : access_code,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


