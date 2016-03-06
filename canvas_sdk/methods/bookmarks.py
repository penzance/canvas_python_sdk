from canvas_sdk import client, utils

def list_bookmarks(request_ctx, per_page=None, **request_kwargs):
    """
    Returns the list of bookmarks.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List bookmarks
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/self/bookmarks'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_bookmark(request_ctx, name=None, url=None, position=None, data=None, **request_kwargs):
    """
    Creates a bookmark.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param name: (optional) The name of the bookmark
        :type name: string or None
        :param url: (optional) The url of the bookmark
        :type url: string or None
        :param position: (optional) The position of the bookmark. Defaults to the bottom.
        :type position: integer or None
        :param data: (optional) The data associated with the bookmark
        :type data: string or None
        :return: Create bookmark
        :rtype: requests.Response (with Bookmark data)

    """

    path = '/v1/users/self/bookmarks'
    payload = {
        'name' : name,
        'url' : url,
        'position' : position,
        'data' : data,
    }
    url = request_ctx.base_api_url + path.format()
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_bookmark(request_ctx, id, **request_kwargs):
    """
    Returns the details for a bookmark.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get bookmark
        :rtype: requests.Response (with Bookmark data)

    """

    path = '/v1/users/self/bookmarks/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_bookmark(request_ctx, id, name=None, url=None, position=None, data=None, **request_kwargs):
    """
    Updates a bookmark

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param name: (optional) The name of the bookmark
        :type name: string or None
        :param url: (optional) The url of the bookmark
        :type url: string or None
        :param position: (optional) The position of the bookmark. Defaults to the bottom.
        :type position: integer or None
        :param data: (optional) The data associated with the bookmark
        :type data: string or None
        :return: Update bookmark
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/users/self/bookmarks/{id}'
    payload = {
        'name' : name,
        'url' : url,
        'position' : position,
        'data' : data,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_bookmark(request_ctx, id, **request_kwargs):
    """
    Deletes a bookmark

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete bookmark
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/self/bookmarks/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


