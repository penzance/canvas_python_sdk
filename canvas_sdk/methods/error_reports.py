from canvas_sdk import client, utils


def create_error_report(request_ctx, error_subject, error_url=None, error_email=None, error_comments=None, error_http_env=None, **request_kwargs):
    """
    Create a new error report documenting an experienced problem
    
    Performs the same action as when a user uses the "help -> report a problem"
    dialog.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param error_subject: (required) The summary of the problem
        :type error_subject: string
        :param error_url: (optional) URL from which the report was issued
        :type error_url: string or None
        :param error_email: (optional) Email address for the reporting user
        :type error_email: string or None
        :param error_comments: (optional) The long version of the story from the user one what they experienced
        :type error_comments: string or None
        :param error_http_env: (optional) A collection of metadata about the users' environment.  If not provided,
canvas will collect it based on information found in the request.
(Doesn't have to be HTTPENV info, could be anything JSON object that can be
serialized as a hash, a mobile app might include relevant metadata for
itself)
        :type error_http_env: SerializedHash or None
        :return: Create Error Report
        :rtype: requests.Response (with void data)

    """

    path = '/v1/error_reports'
    payload = {
        'error[subject]': error_subject,
        'error[url]': error_url,
        'error[email]': error_email,
        'error[comments]': error_comments,
        'error[http_env]': error_http_env,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


