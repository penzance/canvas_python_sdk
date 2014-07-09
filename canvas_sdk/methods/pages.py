from canvas_sdk import client, utils

def show_front_page_courses(request_ctx, course_id, **request_kwargs):
    """
    Retrieve the content of the front page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :return: Show front page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/courses/{course_id}/front_page'
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_front_page_groups(request_ctx, group_id, **request_kwargs):
    """
    Retrieve the content of the front page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :return: Show front page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/groups/{group_id}/front_page'
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_create_front_page_courses(request_ctx, course_id, wiki_page_body, wiki_page_title=None, wiki_page_hide_from_students=None, wiki_page_editing_roles=None, wiki_page_notify_of_update=None, wiki_page_published=None, **request_kwargs):
    """
    Update the title or contents of the front page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_title: (optional) The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        :type wiki_page_title: string or None
        :param wiki_page_hide_from_students: (optional) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean or None
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_notify_of_update: (optional) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :return: Update/create front page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/courses/{course_id}/front_page'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_create_front_page_groups(request_ctx, group_id, wiki_page_body, wiki_page_title=None, wiki_page_hide_from_students=None, wiki_page_editing_roles=None, wiki_page_notify_of_update=None, wiki_page_published=None, **request_kwargs):
    """
    Update the title or contents of the front page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_title: (optional) The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        :type wiki_page_title: string or None
        :param wiki_page_hide_from_students: (optional) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean or None
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_notify_of_update: (optional) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :return: Update/create front page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/groups/{group_id}/front_page'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_pages_courses(request_ctx, course_id, sort=None, order=None, search_term=None, published=None, per_page=None, **request_kwargs):
    """
    List the wiki pages associated with a course or group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param sort: (optional) Sort results by this field.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param search_term: (optional) The partial title of the pages to match and return.
        :type search_term: string or None
        :param published: (optional) If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status.
        :type published: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List pages
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    sort_types = ('title', 'created_at', 'updated_at')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/courses/{course_id}/pages'
    payload = {
        'sort' : sort,
        'order' : order,
        'search_term' : search_term,
        'published' : published,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_pages_groups(request_ctx, group_id, sort=None, order=None, search_term=None, published=None, per_page=None, **request_kwargs):
    """
    List the wiki pages associated with a course or group

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param sort: (optional) Sort results by this field.
        :type sort: string or None
        :param order: (optional) The sorting order. Defaults to 'asc'.
        :type order: string or None
        :param search_term: (optional) The partial title of the pages to match and return.
        :type search_term: string or None
        :param published: (optional) If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status.
        :type published: boolean or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List pages
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    sort_types = ('title', 'created_at', 'updated_at')
    order_types = ('asc', 'desc')
    utils.validate_attr_is_acceptable(sort, sort_types)
    utils.validate_attr_is_acceptable(order, order_types)
    path = '/v1/groups/{group_id}/pages'
    payload = {
        'sort' : sort,
        'order' : order,
        'search_term' : search_term,
        'published' : published,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_page_courses(request_ctx, course_id, wiki_page_title, wiki_page_body, wiki_page_hide_from_students, wiki_page_notify_of_update, wiki_page_editing_roles=None, wiki_page_published=None, wiki_page_front_page=None, **request_kwargs):
    """
    Create a new wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param wiki_page_title: (required) The title for the new page.
        :type wiki_page_title: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_hide_from_students: (required) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean
        :param wiki_page_notify_of_update: (required) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :param wiki_page_front_page: (optional) Set an unhidden page as the front page (if true)
        :type wiki_page_front_page: boolean or None
        :return: Create page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/courses/{course_id}/pages'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
        'wiki_page[front_page]' : wiki_page_front_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_page_groups(request_ctx, group_id, wiki_page_title, wiki_page_body, wiki_page_hide_from_students, wiki_page_notify_of_update, wiki_page_editing_roles=None, wiki_page_published=None, wiki_page_front_page=None, **request_kwargs):
    """
    Create a new wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param wiki_page_title: (required) The title for the new page.
        :type wiki_page_title: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_hide_from_students: (required) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean
        :param wiki_page_notify_of_update: (required) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :param wiki_page_front_page: (optional) Set an unhidden page as the front page (if true)
        :type wiki_page_front_page: boolean or None
        :return: Create page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/groups/{group_id}/pages'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
        'wiki_page[front_page]' : wiki_page_front_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_page_courses(request_ctx, course_id, url, **request_kwargs):
    """
    Retrieve the content of a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :return: Show page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/courses/{course_id}/pages/{url}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def show_page_groups(request_ctx, group_id, url, **request_kwargs):
    """
    Retrieve the content of a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :return: Show page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/groups/{group_id}/pages/{url}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_create_page_courses(request_ctx, course_id, url, wiki_page_title, wiki_page_body, wiki_page_hide_from_students, wiki_page_notify_of_update, wiki_page_editing_roles=None, wiki_page_published=None, wiki_page_front_page=None, **request_kwargs):
    """
    Update the title or contents of a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :param wiki_page_title: (required) The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        :type wiki_page_title: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_hide_from_students: (required) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean
        :param wiki_page_notify_of_update: (required) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :param wiki_page_front_page: (optional) Set an unhidden page as the front page (if true)
        :type wiki_page_front_page: boolean or None
        :return: Update/create page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/courses/{course_id}/pages/{url}'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
        'wiki_page[front_page]' : wiki_page_front_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_create_page_groups(request_ctx, group_id, url, wiki_page_title, wiki_page_body, wiki_page_hide_from_students, wiki_page_notify_of_update, wiki_page_editing_roles=None, wiki_page_published=None, wiki_page_front_page=None, **request_kwargs):
    """
    Update the title or contents of a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :param wiki_page_title: (required) The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        :type wiki_page_title: string
        :param wiki_page_body: (required) The content for the new page.
        :type wiki_page_body: string
        :param wiki_page_hide_from_students: (required) Whether the page should be hidden from students. *Note:* when draft state is enabled, attempts to set +hide_from_students+ will be ignored and the value returned will always be the inverse of the +published+ value.
        :type wiki_page_hide_from_students: boolean
        :param wiki_page_notify_of_update: (required) Whether participants should be notified when this page changes.
        :type wiki_page_notify_of_update: boolean
        :param wiki_page_editing_roles: (optional) Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        :type wiki_page_editing_roles: string or None
        :param wiki_page_published: (optional) Whether the page is published (true) or draft state (false). *Note:* when draft state is disabled, attempts to set +published+ will be ignored and the value returned will always be the inverse of the +hide_from_students+ value.
        :type wiki_page_published: boolean or None
        :param wiki_page_front_page: (optional) Set an unhidden page as the front page (if true)
        :type wiki_page_front_page: boolean or None
        :return: Update/create page
        :rtype: requests.Response (with Page data)

    """

    editing_roles_types = ('teachers', 'students', 'members', 'public')
    utils.validate_attr_is_acceptable(editing_roles, editing_roles_types)
    path = '/v1/groups/{group_id}/pages/{url}'
    payload = {
        'wiki_page[title]' : wiki_page_title,
        'wiki_page[body]' : wiki_page_body,
        'wiki_page[hide_from_students]' : wiki_page_hide_from_students,
        'wiki_page[editing_roles]' : wiki_page_editing_roles,
        'wiki_page[notify_of_update]' : wiki_page_notify_of_update,
        'wiki_page[published]' : wiki_page_published,
        'wiki_page[front_page]' : wiki_page_front_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_page_courses(request_ctx, course_id, url, **request_kwargs):
    """
    Delete a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :return: Delete page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/courses/{course_id}/pages/{url}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_page_groups(request_ctx, group_id, url, **request_kwargs):
    """
    Delete a wiki page

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :return: Delete page
        :rtype: requests.Response (with Page data)

    """

    path = '/v1/groups/{group_id}/pages/{url}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def list_revisions_courses(request_ctx, course_id, url, per_page=None, **request_kwargs):
    """
    List the revisions of a page. Callers must have update rights on the page in order to see page history.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List revisions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/pages/{url}/revisions'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_revisions_groups(request_ctx, group_id, url, per_page=None, **request_kwargs):
    """
    List the revisions of a page. Callers must have update rights on the page in order to see page history.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List revisions
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/groups/{group_id}/pages/{url}/revisions'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_revision_courses_latest(request_ctx, course_id, url, summary=None, **request_kwargs):
    """
    Retrieve the metadata and optionally content of a revision of the page.
    Note that retrieving historic versions of pages requires edit rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :param summary: (optional) If set, exclude page content from results
        :type summary: boolean or None
        :return: Show revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/courses/{course_id}/pages/{url}/revisions/latest'
    payload = {
        'summary' : summary,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_revision_groups_latest(request_ctx, group_id, url, summary=None, **request_kwargs):
    """
    Retrieve the metadata and optionally content of a revision of the page.
    Note that retrieving historic versions of pages requires edit rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :param summary: (optional) If set, exclude page content from results
        :type summary: boolean or None
        :return: Show revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/groups/{group_id}/pages/{url}/revisions/latest'
    payload = {
        'summary' : summary,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_revision_courses_revision_id(request_ctx, course_id, url, revision_id, summary=None, **request_kwargs):
    """
    Retrieve the metadata and optionally content of a revision of the page.
    Note that retrieving historic versions of pages requires edit rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :param revision_id: (required) ID
        :type revision_id: string
        :param summary: (optional) If set, exclude page content from results
        :type summary: boolean or None
        :return: Show revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/courses/{course_id}/pages/{url}/revisions/{revision_id}'
    payload = {
        'summary' : summary,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url, revision_id=revision_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def show_revision_groups_revision_id(request_ctx, group_id, url, revision_id, summary=None, **request_kwargs):
    """
    Retrieve the metadata and optionally content of a revision of the page.
    Note that retrieving historic versions of pages requires edit rights.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :param revision_id: (required) ID
        :type revision_id: string
        :param summary: (optional) If set, exclude page content from results
        :type summary: boolean or None
        :return: Show revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/groups/{group_id}/pages/{url}/revisions/{revision_id}'
    payload = {
        'summary' : summary,
    }
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url, revision_id=revision_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def revert_to_revision_courses(request_ctx, course_id, url, revision_id, **request_kwargs):
    """
    Revert a page to a prior revision.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param url: (required) ID
        :type url: string
        :param revision_id: (required) The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
        :type revision_id: integer
        :return: Revert to revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/courses/{course_id}/pages/{url}/revisions/{revision_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, url=url, revision_id=revision_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def revert_to_revision_groups(request_ctx, group_id, url, revision_id, **request_kwargs):
    """
    Revert a page to a prior revision.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param group_id: (required) ID
        :type group_id: string
        :param url: (required) ID
        :type url: string
        :param revision_id: (required) The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
        :type revision_id: integer
        :return: Revert to revision
        :rtype: requests.Response (with PageRevision data)

    """

    path = '/v1/groups/{group_id}/pages/{url}/revisions/{revision_id}'
    url = request_ctx.base_api_url + path.format(group_id=group_id, url=url, revision_id=revision_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


