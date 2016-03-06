from canvas_sdk import client, utils


def upload_file(request_ctx, course_id, assignment_id, user_id, **request_kwargs):
    """
    Upload a file to attach to a submission comment
    
    See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
    
    The final step of the file upload workflow will return the attachment data,
    including the new file id. The caller can then PUT the file_id to the
    submission API to attach it to a comment

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param assignment_id: (required) ID
        :type assignment_id: string
        :param user_id: (required) ID
        :type user_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files'
    url = request_ctx.base_api_url + path.format(course_id=course_id, assignment_id=assignment_id, user_id=user_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


