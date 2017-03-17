from canvas_sdk import client, utils


def list_custom_gradebook_columns(request_ctx, course_id, include_hidden=None, per_page=None, **request_kwargs):
    """
    List all custom gradebook columns for a course

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param include_hidden: (optional) Include hidden parameters (defaults to false)
        :type include_hidden: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List custom gradebook columns
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/custom_gradebook_columns'
    payload = {
        'include_hidden': include_hidden,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_custom_gradebook_column(request_ctx, course_id, column_title, column_position=None, column_hidden=None, column_teacher_notes=None, **request_kwargs):
    """
    Create a custom gradebook column

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param column_title: (required) no description
        :type column_title: string
        :param column_position: (optional) The position of the column relative to other custom columns
        :type column_position: integer or None
        :param column_hidden: (optional) Hidden columns are not displayed in the gradebook
        :type column_hidden: boolean or None
        :param column_teacher_notes: (optional) Set this if the column is created by a teacher.  The gradebook only
supports one teacher_notes column.
        :type column_teacher_notes: boolean or None
        :return: Create a custom gradebook column
        :rtype: requests.Response (with CustomColumn data)

    """

    path = '/v1/courses/{course_id}/custom_gradebook_columns'
    payload = {
        'column[title]': column_title,
        'column[position]': column_position,
        'column[hidden]': column_hidden,
        'column[teacher_notes]': column_teacher_notes,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_custom_gradebook_column(request_ctx, course_id, id, **request_kwargs):
    """
    Accepts the same parameters as custom gradebook column creation

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a custom gradebook column
        :rtype: requests.Response (with CustomColumn data)

    """

    path = '/v1/courses/{course_id}/custom_gradebook_columns/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def delete_custom_gradebook_column(request_ctx, course_id, id, **request_kwargs):
    """
    Permanently deletes a custom column and its associated data

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete a custom gradebook column
        :rtype: requests.Response (with CustomColumn data)

    """

    path = '/v1/courses/{course_id}/custom_gradebook_columns/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def reorder_custom_columns(request_ctx, course_id, order, **request_kwargs):
    """
    Puts the given columns in the specified order
    
    <b>200 OK</b> is returned if successful

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param order: (required) no description
        :type order: array
        :return: Reorder custom columns
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/custom_gradebook_columns/reorder'
    payload = {
        'order[]': order,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_entries_for_column(request_ctx, course_id, id, include_hidden=None, per_page=None, **request_kwargs):
    """
    This does not list entries for students without associated data.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param include_hidden: (optional) If true, hidden columns will be included in the
result. If false or absent, only visible columns
will be returned.
        :type include_hidden: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List entries for a column
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/custom_gradebook_columns/{id}/data'
    payload = {
        'include_hidden': include_hidden,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_column_data(request_ctx, course_id, id, user_id, column_data_content, **request_kwargs):
    """
    Set the content of a custom column

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param user_id: (required) ID
        :type user_id: string
        :param column_data_content: (required) Column content.  Setting this to blank will delete the datum object.
        :type column_data_content: string
        :return: Update column data
        :rtype: requests.Response (with ColumnDatum data)

    """

    path = '/v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id}'
    payload = {
        'column_data[content]': column_data_content,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id, user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


