from canvas_sdk import client, utils

def get_quota_information_courses(request_ctx, course_id, **request_kwargs):
    """
    Returns the total and used storage quota for the course, group, or user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Get quota information
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/files/quota'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_quota_information_groups(request_ctx, group_id, **request_kwargs):
    """
    Returns the total and used storage quota for the course, group, or user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Get quota information
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/files/quota'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_quota_information_users(request_ctx, user_id, **request_kwargs):
    """
    Returns the total and used storage quota for the course, group, or user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :return: Get quota information
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/files/quota'
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def list_files_courses(request_ctx, course_id, content_types=None, search_term=None, include=None, only=None, sort=None, order=None, per_page=None, **request_kwargs):
    """
    Returns the paginated list of files for the folder or course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param content_types: (optional) Filter results by content-type. You can specify type/subtype pairs (e.g.,
'image/jpeg'), or simply types (e.g., 'image', which will match
'image/gif', 'image/jpeg', etc.).
        :type content_types: array or None
        :param search_term: (optional) The partial name of the files to match and return.
        :type search_term: string or None
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :param only: (optional) Array of information to restrict to. Overrides include[]

"names":: only returns file name information
        :type only: array or None
        :param sort: (optional) Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List files
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('user')
    sort_types = ('name', 'size', 'created_at', 'updated_at', 'content_type', 'user')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/courses/{course_id}/files'
    payload = {
        'content_types' : content_types,
        'search_term' : search_term,
        'include' : include,
        'only' : only,
        'sort' : sort,
        'order' : order,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_files_users(request_ctx, user_id, content_types=None, search_term=None, include=None, only=None, sort=None, order=None, per_page=None, **request_kwargs):
    """
    Returns the paginated list of files for the folder or course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param content_types: (optional) Filter results by content-type. You can specify type/subtype pairs (e.g.,
'image/jpeg'), or simply types (e.g., 'image', which will match
'image/gif', 'image/jpeg', etc.).
        :type content_types: array or None
        :param search_term: (optional) The partial name of the files to match and return.
        :type search_term: string or None
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :param only: (optional) Array of information to restrict to. Overrides include[]

"names":: only returns file name information
        :type only: array or None
        :param sort: (optional) Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List files
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('user')
    sort_types = ('name', 'size', 'created_at', 'updated_at', 'content_type', 'user')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/users/{user_id}/files'
    payload = {
        'content_types' : content_types,
        'search_term' : search_term,
        'include' : include,
        'only' : only,
        'sort' : sort,
        'order' : order,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_files_groups(request_ctx, group_id, content_types=None, search_term=None, include=None, only=None, sort=None, order=None, per_page=None, **request_kwargs):
    """
    Returns the paginated list of files for the folder or course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param content_types: (optional) Filter results by content-type. You can specify type/subtype pairs (e.g.,
'image/jpeg'), or simply types (e.g., 'image', which will match
'image/gif', 'image/jpeg', etc.).
        :type content_types: array or None
        :param search_term: (optional) The partial name of the files to match and return.
        :type search_term: string or None
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :param only: (optional) Array of information to restrict to. Overrides include[]

"names":: only returns file name information
        :type only: array or None
        :param sort: (optional) Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List files
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('user')
    sort_types = ('name', 'size', 'created_at', 'updated_at', 'content_type', 'user')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/groups/{group_id}/files'
    payload = {
        'content_types' : content_types,
        'search_term' : search_term,
        'include' : include,
        'only' : only,
        'sort' : sort,
        'order' : order,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_files_folders(request_ctx, id, content_types=None, search_term=None, include=None, only=None, sort=None, order=None, per_page=None, **request_kwargs):
    """
    Returns the paginated list of files for the folder or course.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param content_types: (optional) Filter results by content-type. You can specify type/subtype pairs (e.g.,
'image/jpeg'), or simply types (e.g., 'image', which will match
'image/gif', 'image/jpeg', etc.).
        :type content_types: array or None
        :param search_term: (optional) The partial name of the files to match and return.
        :type search_term: string or None
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :param only: (optional) Array of information to restrict to. Overrides include[]

"names":: only returns file name information
        :type only: array or None
        :param sort: (optional) Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List files
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('user')
    sort_types = ('name', 'size', 'created_at', 'updated_at', 'content_type', 'user')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(include, include_types)
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/folders/{id}/files'
    payload = {
        'content_types' : content_types,
        'search_term' : search_term,
        'include' : include,
        'only' : only,
        'sort' : sort,
        'order' : order,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_quota_information(request_ctx, id, **request_kwargs):
    """
    Determine the URL that should be used for inline preview of the file.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get quota information
        :rtype: requests.Response (with void data)

    """

    path = '/v1/files/{id}/public_url'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_file_files(request_ctx, id, include=None, **request_kwargs):
    """
    Returns the standard attachment json object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :return: Get file
        :rtype: requests.Response (with File data)

    """

    include_types = ('user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/files/{id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_file_courses(request_ctx, course_id, id, include=None, **request_kwargs):
    """
    Returns the standard attachment json object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :return: Get file
        :rtype: requests.Response (with File data)

    """

    include_types = ('user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/courses/{course_id}/files/{id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_file_groups(request_ctx, group_id, id, include=None, **request_kwargs):
    """
    Returns the standard attachment json object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :return: Get file
        :rtype: requests.Response (with File data)

    """

    include_types = ('user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/groups/{group_id}/files/{id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_file_users(request_ctx, user_id, id, include=None, **request_kwargs):
    """
    Returns the standard attachment json object

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :param include: (optional) Array of additional information to include.

"user":: the user who uploaded the file or last edited its content
"usage_rights":: copyright and license information for the file (see UsageRights)
        :type include: array or None
        :return: Get file
        :rtype: requests.Response (with File data)

    """

    include_types = ('user')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/users/{user_id}/files/{id}'
    payload = {
        'include' : include,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_file(request_ctx, id, name=None, parent_folder_id=None, on_duplicate=None, lock_at=None, unlock_at=None, locked=None, hidden=None, **request_kwargs):
    """
    Update some settings on the specified file

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param name: (optional) The new display name of the file
        :type name: string or None
        :param parent_folder_id: (optional) The id of the folder to move this file into.
The new folder must be in the same context as the original parent folder.
If the file is in a context without folders this does not apply.
        :type parent_folder_id: string or None
        :param on_duplicate: (optional) If the file is moved to a folder containing a file with the same name,
or renamed to a name matching an existing file, the API call will fail
unless this parameter is supplied.

"overwrite":: Replace the existing file with the same name
"rename":: Add a qualifier to make the new filename unique
        :type on_duplicate: string or None
        :param lock_at: (optional) The datetime to lock the file at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the file at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the file as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the file as hidden
        :type hidden: boolean or None
        :return: Update file
        :rtype: requests.Response (with File data)

    """

    on_duplicate_types = ('overwrite', 'rename')
    utils.validate_attr_is_acceptable(on_duplicate, on_duplicate_types)
    path = '/v1/files/{id}'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'on_duplicate' : on_duplicate,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_file(request_ctx, id, **request_kwargs):
    """
    Remove the specified file
    
      curl -XDELETE 'https://<canvas>/api/v1/files/<file_id>' \
           -H 'Authorization: Bearer <token>'

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Delete file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/files/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_folders(request_ctx, id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of folders in the folder.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List folders
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/folders/{id}/folders'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_all_folders_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of all folders for the given context. This will
    be returned as a flat list containing all subfolders as well.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List all folders
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/folders'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_all_folders_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of all folders for the given context. This will
    be returned as a flat list containing all subfolders as well.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List all folders
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/folders'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_all_folders_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Returns the paginated list of all folders for the given context. This will
    be returned as a flat list containing all subfolders as well.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List all folders
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/folders'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_courses_full_path(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/folders/by_path/*full_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/folders/by_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_users_full_path(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/folders/by_path/*full_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/folders/by_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_groups_full_path(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/folders/by_path/*full_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def resolve_path_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Given the full path to a folder, returns a list of all Folders in the path hierarchy,
    starting at the root folder, and ending at the requested folder. The given path is
    relative to the context's root folder and does not include the root folder's name
    (e.g., "course files"). If an empty path is given, the context's root folder alone
    is returned. Otherwise, if no folder exists with the given full path, a Not Found
    error is returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Resolve path
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/folders/by_path'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_folder_courses(request_ctx, course_id, id, **request_kwargs):
    """
    Returns the details for a folder
    
    You can get the root folder from a context by using 'root' as the :id.
    For example, you could get the root folder for a course like:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (required) ID
        :type id: string
        :return: Get folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/courses/{course_id}/folders/{id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_folder_users(request_ctx, user_id, id, **request_kwargs):
    """
    Returns the details for a folder
    
    You can get the root folder from a context by using 'root' as the :id.
    For example, you could get the root folder for a course like:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param id: (required) ID
        :type id: string
        :return: Get folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/users/{user_id}/folders/{id}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_folder_groups(request_ctx, group_id, id, **request_kwargs):
    """
    Returns the details for a folder
    
    You can get the root folder from a context by using 'root' as the :id.
    For example, you could get the root folder for a course like:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param id: (required) ID
        :type id: string
        :return: Get folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/groups/{group_id}/folders/{id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_folder_folders(request_ctx, id, **request_kwargs):
    """
    Returns the details for a folder
    
    You can get the root folder from a context by using 'root' as the :id.
    For example, you could get the root folder for a course like:

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Get folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/folders/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_folder(request_ctx, id, name=None, parent_folder_id=None, lock_at=None, unlock_at=None, locked=None, hidden=None, position=None, **request_kwargs):
    """
    Updates a folder

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param name: (optional) The new name of the folder
        :type name: string or None
        :param parent_folder_id: (optional) The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder.
        :type parent_folder_id: string or None
        :param lock_at: (optional) The datetime to lock the folder at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the folder at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the folder as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the folder as hidden
        :type hidden: boolean or None
        :param position: (optional) Set an explicit sort position for the folder
        :type position: integer or None
        :return: Update folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/folders/{id}'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
        'position' : position,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_folder_courses(request_ctx, course_id, name, parent_folder_id=None, parent_folder_path=None, lock_at=None, unlock_at=None, locked=None, hidden=None, position=None, **request_kwargs):
    """
    Creates a folder in the specified context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param name: (required) The name of the folder
        :type name: string
        :param parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_id: string or None
        :param parent_folder_path: (optional) The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_path: string or None
        :param lock_at: (optional) The datetime to lock the folder at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the folder at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the folder as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the folder as hidden
        :type hidden: boolean or None
        :param position: (optional) Set an explicit sort position for the folder
        :type position: integer or None
        :return: Create folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/courses/{course_id}/folders'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'parent_folder_path' : parent_folder_path,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
        'position' : position,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_folder_users(request_ctx, user_id, name, parent_folder_id=None, parent_folder_path=None, lock_at=None, unlock_at=None, locked=None, hidden=None, position=None, **request_kwargs):
    """
    Creates a folder in the specified context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param name: (required) The name of the folder
        :type name: string
        :param parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_id: string or None
        :param parent_folder_path: (optional) The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_path: string or None
        :param lock_at: (optional) The datetime to lock the folder at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the folder at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the folder as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the folder as hidden
        :type hidden: boolean or None
        :param position: (optional) Set an explicit sort position for the folder
        :type position: integer or None
        :return: Create folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/users/{user_id}/folders'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'parent_folder_path' : parent_folder_path,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
        'position' : position,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_folder_groups(request_ctx, group_id, name, parent_folder_id=None, parent_folder_path=None, lock_at=None, unlock_at=None, locked=None, hidden=None, position=None, **request_kwargs):
    """
    Creates a folder in the specified context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param name: (required) The name of the folder
        :type name: string
        :param parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_id: string or None
        :param parent_folder_path: (optional) The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_path: string or None
        :param lock_at: (optional) The datetime to lock the folder at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the folder at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the folder as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the folder as hidden
        :type hidden: boolean or None
        :param position: (optional) Set an explicit sort position for the folder
        :type position: integer or None
        :return: Create folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/groups/{group_id}/folders'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'parent_folder_path' : parent_folder_path,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
        'position' : position,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_folder_folders(request_ctx, folder_id, name, parent_folder_id=None, parent_folder_path=None, lock_at=None, unlock_at=None, locked=None, hidden=None, position=None, **request_kwargs):
    """
    Creates a folder in the specified context

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param folder_id: (required) ID
        :type folder_id: string
        :param name: (required) The name of the folder
        :type name: string
        :param parent_folder_id: (optional) The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_id: string or None
        :param parent_folder_path: (optional) The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used.
        :type parent_folder_path: string or None
        :param lock_at: (optional) The datetime to lock the folder at
        :type lock_at: DateTime or None
        :param unlock_at: (optional) The datetime to unlock the folder at
        :type unlock_at: DateTime or None
        :param locked: (optional) Flag the folder as locked
        :type locked: boolean or None
        :param hidden: (optional) Flag the folder as hidden
        :type hidden: boolean or None
        :param position: (optional) Set an explicit sort position for the folder
        :type position: integer or None
        :return: Create folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/folders/{folder_id}/folders'
    payload = {
        'name' : name,
        'parent_folder_id' : parent_folder_id,
        'parent_folder_path' : parent_folder_path,
        'lock_at' : lock_at,
        'unlock_at' : unlock_at,
        'locked' : locked,
        'hidden' : hidden,
        'position' : position,
    }
    url = request_ctx.base_api_url + path.format(folder_id=folder_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_folder(request_ctx, id, force=None, **request_kwargs):
    """
    Remove the specified folder. You can only delete empty folders unless you
    set the 'force' flag

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :param force: (optional) Set to 'true' to allow deleting a non-empty folder
        :type force: boolean or None
        :return: Delete folder
        :rtype: requests.Response (with void data)

    """

    path = '/v1/folders/{id}'
    payload = {
        'force' : force,
    }
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def upload_file(request_ctx, folder_id, **request_kwargs):
    """
    Upload a file to a folder.
    
    This API endpoint is the first step in uploading a file.
    See the {file:file_uploads.html File Upload Documentation} for details on
    the file upload workflow.
    
    Only those with the "Manage Files" permission on a course or group can
    upload files to a folder in that course or group.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param folder_id: (required) ID
        :type folder_id: string
        :return: Upload a file
        :rtype: requests.Response (with void data)

    """

    path = '/v1/folders/{folder_id}/files'
    url = request_ctx.base_api_url + path.format(folder_id=folder_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def copy_file(request_ctx, dest_folder_id, source_file_id, on_duplicate=None, **request_kwargs):
    """
    Copy a file from elsewhere in Canvas into a folder.
    
    Copying a file across contexts (between courses and users) is permitted,
    but the source and destination must belong to the same institution.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param dest_folder_id: (required) ID
        :type dest_folder_id: string
        :param source_file_id: (required) The id of the source file
        :type source_file_id: string
        :param on_duplicate: (optional) What to do if a file with the same name already exists at the destination.
If such a file exists and this parameter is not given, the call will fail.

"overwrite":: Replace an existing file with the same name
"rename":: Add a qualifier to make the new filename unique
        :type on_duplicate: string or None
        :return: Copy a file
        :rtype: requests.Response (with File data)

    """

    on_duplicate_types = ('overwrite', 'rename')
    utils.validate_attr_is_acceptable(on_duplicate, on_duplicate_types)
    path = '/v1/folders/{dest_folder_id}/copy_file'
    payload = {
        'source_file_id' : source_file_id,
        'on_duplicate' : on_duplicate,
    }
    url = request_ctx.base_api_url + path.format(dest_folder_id=dest_folder_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def copy_folder(request_ctx, dest_folder_id, source_folder_id, **request_kwargs):
    """
    Copy a folder (and its contents) from elsewhere in Canvas into a folder.
    
    Copying a folder across contexts (between courses and users) is permitted,
    but the source and destination must belong to the same institution.
    If the source and destination folders are in the same context, the
    source folder may not contain the destination folder. A folder will be
    renamed at its destination if another folder with the same name already
    exists.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param dest_folder_id: (required) ID
        :type dest_folder_id: string
        :param source_folder_id: (required) The id of the source folder
        :type source_folder_id: string
        :return: Copy a folder
        :rtype: requests.Response (with Folder data)

    """

    path = '/v1/folders/{dest_folder_id}/copy_folder'
    payload = {
        'source_folder_id' : source_folder_id,
    }
    url = request_ctx.base_api_url + path.format(dest_folder_id=dest_folder_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def set_usage_rights_courses(request_ctx, course_id, file_ids, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None, **request_kwargs):
    """
    Sets copyright and license information for one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param file_ids: (required) List of ids of files to set usage rights for.
        :type file_ids: array
        :param usage_rights_use_justification: (required) The intellectual property justification for using the files in Canvas
        :type usage_rights_use_justification: string
        :param folder_ids: (optional) List of ids of folders to search for files to set usage rights for.
Note that new files uploaded to these folders do not automatically inherit these rights.
        :type folder_ids: array or None
        :param publish: (optional) Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save).
        :type publish: boolean or None
        :param usage_rights_legal_copyright: (optional) The legal copyright line for the files
        :type usage_rights_legal_copyright: string or None
        :param usage_rights_license: (optional) The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types.
        :type usage_rights_license: string or None
        :return: Set usage rights
        :rtype: requests.Response (with UsageRights data)

    """

    usage_rights_use_justification_types = ('own_copyright', 'used_by_permission', 'fair_use', 'public_domain', 'creative_commons')
    utils.validate_attr_is_acceptable(usage_rights_use_justification, usage_rights_use_justification_types)
    path = '/v1/courses/{course_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
        'publish' : publish,
        'usage_rights[use_justification]' : usage_rights_use_justification,
        'usage_rights[legal_copyright]' : usage_rights_legal_copyright,
        'usage_rights[license]' : usage_rights_license,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def set_usage_rights_groups(request_ctx, group_id, file_ids, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None, **request_kwargs):
    """
    Sets copyright and license information for one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param file_ids: (required) List of ids of files to set usage rights for.
        :type file_ids: array
        :param usage_rights_use_justification: (required) The intellectual property justification for using the files in Canvas
        :type usage_rights_use_justification: string
        :param folder_ids: (optional) List of ids of folders to search for files to set usage rights for.
Note that new files uploaded to these folders do not automatically inherit these rights.
        :type folder_ids: array or None
        :param publish: (optional) Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save).
        :type publish: boolean or None
        :param usage_rights_legal_copyright: (optional) The legal copyright line for the files
        :type usage_rights_legal_copyright: string or None
        :param usage_rights_license: (optional) The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types.
        :type usage_rights_license: string or None
        :return: Set usage rights
        :rtype: requests.Response (with UsageRights data)

    """

    usage_rights_use_justification_types = ('own_copyright', 'used_by_permission', 'fair_use', 'public_domain', 'creative_commons')
    utils.validate_attr_is_acceptable(usage_rights_use_justification, usage_rights_use_justification_types)
    path = '/v1/groups/{group_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
        'publish' : publish,
        'usage_rights[use_justification]' : usage_rights_use_justification,
        'usage_rights[legal_copyright]' : usage_rights_legal_copyright,
        'usage_rights[license]' : usage_rights_license,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def set_usage_rights_users(request_ctx, user_id, file_ids, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None, **request_kwargs):
    """
    Sets copyright and license information for one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param file_ids: (required) List of ids of files to set usage rights for.
        :type file_ids: array
        :param usage_rights_use_justification: (required) The intellectual property justification for using the files in Canvas
        :type usage_rights_use_justification: string
        :param folder_ids: (optional) List of ids of folders to search for files to set usage rights for.
Note that new files uploaded to these folders do not automatically inherit these rights.
        :type folder_ids: array or None
        :param publish: (optional) Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save).
        :type publish: boolean or None
        :param usage_rights_legal_copyright: (optional) The legal copyright line for the files
        :type usage_rights_legal_copyright: string or None
        :param usage_rights_license: (optional) The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types.
        :type usage_rights_license: string or None
        :return: Set usage rights
        :rtype: requests.Response (with UsageRights data)

    """

    usage_rights_use_justification_types = ('own_copyright', 'used_by_permission', 'fair_use', 'public_domain', 'creative_commons')
    utils.validate_attr_is_acceptable(usage_rights_use_justification, usage_rights_use_justification_types)
    path = '/v1/users/{user_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
        'publish' : publish,
        'usage_rights[use_justification]' : usage_rights_use_justification,
        'usage_rights[legal_copyright]' : usage_rights_legal_copyright,
        'usage_rights[license]' : usage_rights_license,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_usage_rights_courses(request_ctx, course_id, file_ids, folder_ids=None, **request_kwargs):
    """
    Removes copyright and license information associated with one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param file_ids: (required) List of ids of files to remove associated usage rights from.
        :type file_ids: array
        :param folder_ids: (optional) List of ids of folders. Usage rights will be removed from all files in these folders.
        :type folder_ids: array or None
        :return: Remove usage rights
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_usage_rights_groups(request_ctx, group_id, file_ids, folder_ids=None, **request_kwargs):
    """
    Removes copyright and license information associated with one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param file_ids: (required) List of ids of files to remove associated usage rights from.
        :type file_ids: array
        :param folder_ids: (optional) List of ids of folders. Usage rights will be removed from all files in these folders.
        :type folder_ids: array or None
        :return: Remove usage rights
        :rtype: requests.Response (with void data)

    """

    path = '/v1/groups/{group_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_usage_rights_users(request_ctx, user_id, file_ids, folder_ids=None, **request_kwargs):
    """
    Removes copyright and license information associated with one or more files

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param file_ids: (required) List of ids of files to remove associated usage rights from.
        :type file_ids: array
        :param folder_ids: (optional) List of ids of folders. Usage rights will be removed from all files in these folders.
        :type folder_ids: array or None
        :return: Remove usage rights
        :rtype: requests.Response (with void data)

    """

    path = '/v1/users/{user_id}/usage_rights'
    payload = {
        'file_ids' : file_ids,
        'folder_ids' : folder_ids,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.delete(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_licenses_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    Lists licenses that can be applied

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List licenses
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/content_licenses'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_licenses_groups(request_ctx, group_id, per_page=None, **request_kwargs):
    """
    Lists licenses that can be applied

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List licenses
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/content_licenses'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_licenses_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    Lists licenses that can be applied

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List licenses
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/content_licenses'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


