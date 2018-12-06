from __future__ import unicode_literals
from canvas_sdk import client, utils

def upload_file(request_ctx, course_id, quiz_id, name, on_duplicate, **request_kwargs):
    """
    Associate a new quiz submission file
    
    This API endpoint is the first step in uploading a quiz submission file.
    See the {file:file_uploads.html File Upload Documentation} for details on
    the file upload workflow as these parameters are interpreted as per the
    documentation there.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param quiz_id: (required) ID
        :type quiz_id: string
        :param name: (required) The name of the quiz submission file
        :type name: string
        :param on_duplicate: (required) How to handle duplicate names
        :type on_duplicate: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files'
    payload = {
        'name' : name,
        'on_duplicate' : on_duplicate,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, quiz_id=quiz_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


