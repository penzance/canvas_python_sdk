from canvas_sdk import client, utils


def send_message_to_unsubmitted_or_submitted_users_for_quiz(request_ctx, course_id, id, conversations=None, **request_kwargs):
    """
    {
      "body": {
        "type": "string",
        "description": "message body of the conversation to be created",
        "example": "Please take the quiz."
      },
      "recipients": {
        "type": "string",
        "description": "Who to send the message to. May be either 'submitted' or 'unsubmitted'",
        "example": "submitted"
      },
      "subject": {
        "type": "string",
        "description": "Subject of the new Conversation created",
        "example": "ATTN: Quiz 101 Students"
      }
    }

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param conversations: (optional) - Body and recipients to send the message to.
        :type conversations: QuizUserConversation or None
        :return: Send a message to unsubmitted or submitted users for the quiz
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{id}/submission_users/message'
    payload = {
        'conversations': conversations,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


