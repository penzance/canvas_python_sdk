from canvas_sdk import client, utils

def list_external_tools_courses(request_ctx, course_id, search_term=None, **request_kwargs):
    """
    Returns the paginated list of external tools for the current context.
    See the get request docs for a single tool for a list of properties on an external tool.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param search_term: (optional) The partial name of the tools to match and return.
        :type search_term: string or None
        :return: List external tools
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/external_tools'
    payload = {
        'search_term' : search_term,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_external_tools_accounts(request_ctx, account_id, search_term=None, **request_kwargs):
    """
    Returns the paginated list of external tools for the current context.
    See the get request docs for a single tool for a list of properties on an external tool.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param search_term: (optional) The partial name of the tools to match and return.
        :type search_term: string or None
        :return: List external tools
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/external_tools'
    payload = {
        'search_term' : search_term,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_sessionless_launch_url_for_external_tool_courses(request_ctx, course_id, id=None, url=None, assignment_id=None, launch_type=None, **request_kwargs):
    """
    Returns a sessionless launch url for an external tool.
    
    Either the id or url must be provided.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param id: (optional) The external id of the tool to launch.
        :type id: string or None
        :param url: (optional) The LTI launch url for the external tool.
        :type url: string or None
        :param assignment_id: (optional) The assignment id for an assignment launch.
        :type assignment_id: string or None
        :param launch_type: (optional) The type of launch to perform on the external tool.
        :type launch_type: string or None
        :return: Get a sessionless launch url for an external tool.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/external_tools/sessionless_launch'
    payload = {
        'id' : id,
        'url' : url,
        'assignment_id' : assignment_id,
        'launch_type' : launch_type,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_sessionless_launch_url_for_external_tool_accounts(request_ctx, account_id, id=None, url=None, assignment_id=None, launch_type=None, **request_kwargs):
    """
    Returns a sessionless launch url for an external tool.
    
    Either the id or url must be provided.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (optional) The external id of the tool to launch.
        :type id: string or None
        :param url: (optional) The LTI launch url for the external tool.
        :type url: string or None
        :param assignment_id: (optional) The assignment id for an assignment launch.
        :type assignment_id: string or None
        :param launch_type: (optional) The type of launch to perform on the external tool.
        :type launch_type: string or None
        :return: Get a sessionless launch url for an external tool.
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/external_tools/sessionless_launch'
    payload = {
        'id' : id,
        'url' : url,
        'assignment_id' : assignment_id,
        'launch_type' : launch_type,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_external_tool_courses(request_ctx, course_id, external_tool_id, **request_kwargs):
    """
    Returns the specified external tool.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :return: Get a single external tool
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/external_tools/{external_tool_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, external_tool_id=external_tool_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_single_external_tool_accounts(request_ctx, account_id, external_tool_id, **request_kwargs):
    """
    Returns the specified external tool.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :return: Get a single external tool
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/external_tools/{external_tool_id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, external_tool_id=external_tool_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_external_tool_courses(request_ctx, course_id, name, privacy_level, consumer_key, shared_secret, description=None, url=None, domain=None, icon_url=None, text=None, custom_fields=None, account_navigation_url=None, account_navigation_enabled=None, account_navigation_text=None, user_navigation_url=None, user_navigation_enabled=None, user_navigation_text=None, course_navigation_url=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_default=None, editor_button_url=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_selection_width=None, editor_button_selection_height=None, resource_selection_url=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_width=None, resource_selection_selection_height=None, config_type=None, config_xml=None, config_url=None, **request_kwargs):
    """
    Create an external tool in the specified course/account.
    The created tool will be returned, see the "show" endpoint for an example.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param name: (required) The name of the tool
        :type name: string
        :param privacy_level: (required) What information to send to the external tool.
        :type privacy_level: string
        :param consumer_key: (required) The consumer key for the external tool
        :type consumer_key: string
        :param shared_secret: (required) The shared secret with the external tool
        :type shared_secret: string
        :param description: (optional) A description of the tool
        :type description: string or None
        :param url: (optional) The url to match links against. Either "url" or "domain" should be set, not both.
        :type url: string or None
        :param domain: (optional) The domain to match links against. Either "url" or "domain" should be set, not both.
        :type domain: string or None
        :param icon_url: (optional) The url of the icon to show for this tool
        :type icon_url: string or None
        :param text: (optional) The default text to show for this tool
        :type text: string or None
        :param custom_fields: (optional) Custom fields that will be sent to the tool consumer, specified as custom_fields[field_name]
        :type custom_fields: string or None
        :param account_navigation_url: (optional) The url of the external tool for account navigation
        :type account_navigation_url: string or None
        :param account_navigation_enabled: (optional) Set this to enable this feature
        :type account_navigation_enabled: boolean or None
        :param account_navigation_text: (optional) The text that will show on the left-tab in the account navigation
        :type account_navigation_text: string or None
        :param user_navigation_url: (optional) The url of the external tool for user navigation
        :type user_navigation_url: string or None
        :param user_navigation_enabled: (optional) Set this to enable this feature
        :type user_navigation_enabled: boolean or None
        :param user_navigation_text: (optional) The text that will show on the left-tab in the user navigation
        :type user_navigation_text: string or None
        :param course_navigation_url: (optional) The url of the external tool for course navigation
        :type course_navigation_url: string or None
        :param course_navigation_enabled: (optional) Set this to enable this feature
        :type course_navigation_enabled: boolean or None
        :param course_navigation_text: (optional) The text that will show on the left-tab in the course navigation
        :type course_navigation_text: string or None
        :param course_navigation_visibility: (optional) Who will see the navigation tab. "admins" for course admins, "members" for students, null for everyone
        :type course_navigation_visibility: string or None
        :param course_navigation_default: (optional) Whether the navigation option will show in the course by default or whether the teacher will have to explicitly enable it
        :type course_navigation_default: boolean or None
        :param editor_button_url: (optional) The url of the external tool
        :type editor_button_url: string or None
        :param editor_button_enabled: (optional) Set this to enable this feature
        :type editor_button_enabled: boolean or None
        :param editor_button_icon_url: (optional) The url of the icon to show in the WYSIWYG editor
        :type editor_button_icon_url: string or None
        :param editor_button_selection_width: (optional) The width of the dialog the tool is launched in
        :type editor_button_selection_width: string or None
        :param editor_button_selection_height: (optional) The height of the dialog the tool is launched in
        :type editor_button_selection_height: string or None
        :param resource_selection_url: (optional) The url of the external tool
        :type resource_selection_url: string or None
        :param resource_selection_enabled: (optional) Set this to enable this feature
        :type resource_selection_enabled: boolean or None
        :param resource_selection_icon_url: (optional) The url of the icon to show in the module external tool list
        :type resource_selection_icon_url: string or None
        :param resource_selection_selection_width: (optional) The width of the dialog the tool is launched in
        :type resource_selection_selection_width: string or None
        :param resource_selection_selection_height: (optional) The height of the dialog the tool is launched in
        :type resource_selection_selection_height: string or None
        :param config_type: (optional) Configuration can be passed in as CC xml instead of using query parameters. If this value is "by_url" or "by_xml" then an xml configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the xml
        :type config_type: string or None
        :param config_xml: (optional) XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_xml"
        :type config_xml: string or None
        :param config_url: (optional) URL where the server can retrieve an XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_url"
        :type config_url: string or None
        :return: Create an external tool
        :rtype: requests.Response (with void data)

    """

    privacy_level_types = ('anonymous', 'name_only', 'public')
    course_navigation_visibility_types = ('admins', 'members')
    utils.validate_attr_is_acceptable(privacy_level, privacy_level_types)
    utils.validate_attr_is_acceptable(course_navigation_visibility, course_navigation_visibility_types)
    path = '/v1/courses/{course_id}/external_tools'
    payload = {
        'name' : name,
        'privacy_level' : privacy_level,
        'consumer_key' : consumer_key,
        'shared_secret' : shared_secret,
        'description' : description,
        'url' : url,
        'domain' : domain,
        'icon_url' : icon_url,
        'text' : text,
        'custom_fields' : custom_fields,
        'account_navigation[url]' : account_navigation_url,
        'account_navigation[enabled]' : account_navigation_enabled,
        'account_navigation[text]' : account_navigation_text,
        'user_navigation[url]' : user_navigation_url,
        'user_navigation[enabled]' : user_navigation_enabled,
        'user_navigation[text]' : user_navigation_text,
        'course_navigation[url]' : course_navigation_url,
        'course_navigation[enabled]' : course_navigation_enabled,
        'course_navigation[text]' : course_navigation_text,
        'course_navigation[visibility]' : course_navigation_visibility,
        'course_navigation[default]' : course_navigation_default,
        'editor_button[url]' : editor_button_url,
        'editor_button[enabled]' : editor_button_enabled,
        'editor_button[icon_url]' : editor_button_icon_url,
        'editor_button[selection_width]' : editor_button_selection_width,
        'editor_button[selection_height]' : editor_button_selection_height,
        'resource_selection[url]' : resource_selection_url,
        'resource_selection[enabled]' : resource_selection_enabled,
        'resource_selection[icon_url]' : resource_selection_icon_url,
        'resource_selection[selection_width]' : resource_selection_selection_width,
        'resource_selection[selection_height]' : resource_selection_selection_height,
        'config_type' : config_type,
        'config_xml' : config_xml,
        'config_url' : config_url,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def create_external_tool_accounts(request_ctx, account_id, name, privacy_level, consumer_key, shared_secret, description=None, url=None, domain=None, icon_url=None, text=None, custom_fields=None, account_navigation_url=None, account_navigation_enabled=None, account_navigation_text=None, user_navigation_url=None, user_navigation_enabled=None, user_navigation_text=None, course_navigation_url=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_default=None, editor_button_url=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_selection_width=None, editor_button_selection_height=None, resource_selection_url=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_width=None, resource_selection_selection_height=None, config_type=None, config_xml=None, config_url=None, **request_kwargs):
    """
    Create an external tool in the specified course/account.
    The created tool will be returned, see the "show" endpoint for an example.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param name: (required) The name of the tool
        :type name: string
        :param privacy_level: (required) What information to send to the external tool.
        :type privacy_level: string
        :param consumer_key: (required) The consumer key for the external tool
        :type consumer_key: string
        :param shared_secret: (required) The shared secret with the external tool
        :type shared_secret: string
        :param description: (optional) A description of the tool
        :type description: string or None
        :param url: (optional) The url to match links against. Either "url" or "domain" should be set, not both.
        :type url: string or None
        :param domain: (optional) The domain to match links against. Either "url" or "domain" should be set, not both.
        :type domain: string or None
        :param icon_url: (optional) The url of the icon to show for this tool
        :type icon_url: string or None
        :param text: (optional) The default text to show for this tool
        :type text: string or None
        :param custom_fields: (optional) Custom fields that will be sent to the tool consumer, specified as custom_fields[field_name]
        :type custom_fields: string or None
        :param account_navigation_url: (optional) The url of the external tool for account navigation
        :type account_navigation_url: string or None
        :param account_navigation_enabled: (optional) Set this to enable this feature
        :type account_navigation_enabled: boolean or None
        :param account_navigation_text: (optional) The text that will show on the left-tab in the account navigation
        :type account_navigation_text: string or None
        :param user_navigation_url: (optional) The url of the external tool for user navigation
        :type user_navigation_url: string or None
        :param user_navigation_enabled: (optional) Set this to enable this feature
        :type user_navigation_enabled: boolean or None
        :param user_navigation_text: (optional) The text that will show on the left-tab in the user navigation
        :type user_navigation_text: string or None
        :param course_navigation_url: (optional) The url of the external tool for course navigation
        :type course_navigation_url: string or None
        :param course_navigation_enabled: (optional) Set this to enable this feature
        :type course_navigation_enabled: boolean or None
        :param course_navigation_text: (optional) The text that will show on the left-tab in the course navigation
        :type course_navigation_text: string or None
        :param course_navigation_visibility: (optional) Who will see the navigation tab. "admins" for course admins, "members" for students, null for everyone
        :type course_navigation_visibility: string or None
        :param course_navigation_default: (optional) Whether the navigation option will show in the course by default or whether the teacher will have to explicitly enable it
        :type course_navigation_default: boolean or None
        :param editor_button_url: (optional) The url of the external tool
        :type editor_button_url: string or None
        :param editor_button_enabled: (optional) Set this to enable this feature
        :type editor_button_enabled: boolean or None
        :param editor_button_icon_url: (optional) The url of the icon to show in the WYSIWYG editor
        :type editor_button_icon_url: string or None
        :param editor_button_selection_width: (optional) The width of the dialog the tool is launched in
        :type editor_button_selection_width: string or None
        :param editor_button_selection_height: (optional) The height of the dialog the tool is launched in
        :type editor_button_selection_height: string or None
        :param resource_selection_url: (optional) The url of the external tool
        :type resource_selection_url: string or None
        :param resource_selection_enabled: (optional) Set this to enable this feature
        :type resource_selection_enabled: boolean or None
        :param resource_selection_icon_url: (optional) The url of the icon to show in the module external tool list
        :type resource_selection_icon_url: string or None
        :param resource_selection_selection_width: (optional) The width of the dialog the tool is launched in
        :type resource_selection_selection_width: string or None
        :param resource_selection_selection_height: (optional) The height of the dialog the tool is launched in
        :type resource_selection_selection_height: string or None
        :param config_type: (optional) Configuration can be passed in as CC xml instead of using query parameters. If this value is "by_url" or "by_xml" then an xml configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the xml
        :type config_type: string or None
        :param config_xml: (optional) XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_xml"
        :type config_xml: string or None
        :param config_url: (optional) URL where the server can retrieve an XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_url"
        :type config_url: string or None
        :return: Create an external tool
        :rtype: requests.Response (with void data)

    """

    privacy_level_types = ('anonymous', 'name_only', 'public')
    course_navigation_visibility_types = ('admins', 'members')
    utils.validate_attr_is_acceptable(privacy_level, privacy_level_types)
    utils.validate_attr_is_acceptable(course_navigation_visibility, course_navigation_visibility_types)
    path = '/v1/accounts/{account_id}/external_tools'
    payload = {
        'name' : name,
        'privacy_level' : privacy_level,
        'consumer_key' : consumer_key,
        'shared_secret' : shared_secret,
        'description' : description,
        'url' : url,
        'domain' : domain,
        'icon_url' : icon_url,
        'text' : text,
        'custom_fields' : custom_fields,
        'account_navigation[url]' : account_navigation_url,
        'account_navigation[enabled]' : account_navigation_enabled,
        'account_navigation[text]' : account_navigation_text,
        'user_navigation[url]' : user_navigation_url,
        'user_navigation[enabled]' : user_navigation_enabled,
        'user_navigation[text]' : user_navigation_text,
        'course_navigation[url]' : course_navigation_url,
        'course_navigation[enabled]' : course_navigation_enabled,
        'course_navigation[text]' : course_navigation_text,
        'course_navigation[visibility]' : course_navigation_visibility,
        'course_navigation[default]' : course_navigation_default,
        'editor_button[url]' : editor_button_url,
        'editor_button[enabled]' : editor_button_enabled,
        'editor_button[icon_url]' : editor_button_icon_url,
        'editor_button[selection_width]' : editor_button_selection_width,
        'editor_button[selection_height]' : editor_button_selection_height,
        'resource_selection[url]' : resource_selection_url,
        'resource_selection[enabled]' : resource_selection_enabled,
        'resource_selection[icon_url]' : resource_selection_icon_url,
        'resource_selection[selection_width]' : resource_selection_selection_width,
        'resource_selection[selection_height]' : resource_selection_selection_height,
        'config_type' : config_type,
        'config_xml' : config_xml,
        'config_url' : config_url,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def edit_external_tool_courses(request_ctx, course_id, external_tool_id, name=None, privacy_level=None, consumer_key=None, shared_secret=None, description=None, url=None, domain=None, icon_url=None, text=None, custom_fields=None, account_navigation_url=None, account_navigation_enabled=None, account_navigation_text=None, user_navigation_url=None, user_navigation_enabled=None, user_navigation_text=None, course_navigation_url=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_default=None, editor_button_url=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_selection_width=None, editor_button_selection_height=None, resource_selection_url=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_width=None, resource_selection_selection_height=None, config_type=None, config_xml=None, config_url=None, **request_kwargs):
    """
    Update the specified external tool. Uses same parameters as create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :param name: (optional) The name of the tool
        :type name: string or None
        :param privacy_level: (optional) What information to send to the external tool.
        :type privacy_level: string or None
        :param consumer_key: (optional) The consumer key for the external tool
        :type consumer_key: string or None
        :param shared_secret: (optional) The shared secret with the external tool
        :type shared_secret: string or None
        :param description: (optional) A description of the tool
        :type description: string or None
        :param url: (optional) The url to match links against. Either "url" or "domain" should be set, not both.
        :type url: string or None
        :param domain: (optional) The domain to match links against. Either "url" or "domain" should be set, not both.
        :type domain: string or None
        :param icon_url: (optional) The url of the icon to show for this tool
        :type icon_url: string or None
        :param text: (optional) The default text to show for this tool
        :type text: string or None
        :param custom_fields: (optional) Custom fields that will be sent to the tool consumer, specified as custom_fields[field_name]
        :type custom_fields: string or None
        :param account_navigation_url: (optional) The url of the external tool for account navigation
        :type account_navigation_url: string or None
        :param account_navigation_enabled: (optional) Set this to enable this feature
        :type account_navigation_enabled: boolean or None
        :param account_navigation_text: (optional) The text that will show on the left-tab in the account navigation
        :type account_navigation_text: string or None
        :param user_navigation_url: (optional) The url of the external tool for user navigation
        :type user_navigation_url: string or None
        :param user_navigation_enabled: (optional) Set this to enable this feature
        :type user_navigation_enabled: boolean or None
        :param user_navigation_text: (optional) The text that will show on the left-tab in the user navigation
        :type user_navigation_text: string or None
        :param course_navigation_url: (optional) The url of the external tool for course navigation
        :type course_navigation_url: string or None
        :param course_navigation_enabled: (optional) Set this to enable this feature
        :type course_navigation_enabled: boolean or None
        :param course_navigation_text: (optional) The text that will show on the left-tab in the course navigation
        :type course_navigation_text: string or None
        :param course_navigation_visibility: (optional) Who will see the navigation tab. "admins" for course admins, "members" for students, null for everyone
        :type course_navigation_visibility: string or None
        :param course_navigation_default: (optional) Whether the navigation option will show in the course by default or whether the teacher will have to explicitly enable it
        :type course_navigation_default: boolean or None
        :param editor_button_url: (optional) The url of the external tool
        :type editor_button_url: string or None
        :param editor_button_enabled: (optional) Set this to enable this feature
        :type editor_button_enabled: boolean or None
        :param editor_button_icon_url: (optional) The url of the icon to show in the WYSIWYG editor
        :type editor_button_icon_url: string or None
        :param editor_button_selection_width: (optional) The width of the dialog the tool is launched in
        :type editor_button_selection_width: string or None
        :param editor_button_selection_height: (optional) The height of the dialog the tool is launched in
        :type editor_button_selection_height: string or None
        :param resource_selection_url: (optional) The url of the external tool
        :type resource_selection_url: string or None
        :param resource_selection_enabled: (optional) Set this to enable this feature
        :type resource_selection_enabled: boolean or None
        :param resource_selection_icon_url: (optional) The url of the icon to show in the module external tool list
        :type resource_selection_icon_url: string or None
        :param resource_selection_selection_width: (optional) The width of the dialog the tool is launched in
        :type resource_selection_selection_width: string or None
        :param resource_selection_selection_height: (optional) The height of the dialog the tool is launched in
        :type resource_selection_selection_height: string or None
        :param config_type: (optional) Configuration can be passed in as CC xml instead of using query parameters. If this value is "by_url" or "by_xml" then an xml configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the xml
        :type config_type: string or None
        :param config_xml: (optional) XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_xml"
        :type config_xml: string or None
        :param config_url: (optional) URL where the server can retrieve an XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_url"
        :type config_url: string or None
        :return: Edit an external tool
        :rtype: requests.Response (with void data)

    """
    privacy_level_types = ('anonymous', 'name_only', 'public')
    course_navigation_visibility_types = ('admins', 'members')
    utils.validate_attr_is_acceptable(privacy_level, privacy_level_types)
    utils.validate_attr_is_acceptable(course_navigation_visibility, course_navigation_visibility_types)
    path = '/v1/courses/{course_id}/external_tools/{external_tool_id}'
    payload = {
        'name': name,
        'privacy_level': privacy_level,
        'consumer_key': consumer_key,
        'shared_secret': shared_secret,
        'description': description,
        'url': url,
        'domain': domain,
        'icon_url': icon_url,
        'text' : text,
        'custom_fields' : custom_fields,
        'account_navigation[url]' : account_navigation_url,
        'account_navigation[enabled]' : account_navigation_enabled,
        'account_navigation[text]' : account_navigation_text,
        'user_navigation[url]' : user_navigation_url,
        'user_navigation[enabled]' : user_navigation_enabled,
        'user_navigation[text]' : user_navigation_text,
        'course_navigation[url]' : course_navigation_url,
        'course_navigation[enabled]' : course_navigation_enabled,
        'course_navigation[text]' : course_navigation_text,
        'course_navigation[visibility]' : course_navigation_visibility,
        'course_navigation[default]' : course_navigation_default,
        'editor_button[url]' : editor_button_url,
        'editor_button[enabled]' : editor_button_enabled,
        'editor_button[icon_url]' : editor_button_icon_url,
        'editor_button[selection_width]' : editor_button_selection_width,
        'editor_button[selection_height]' : editor_button_selection_height,
        'resource_selection[url]' : resource_selection_url,
        'resource_selection[enabled]' : resource_selection_enabled,
        'resource_selection[icon_url]' : resource_selection_icon_url,
        'resource_selection[selection_width]' : resource_selection_selection_width,
        'resource_selection[selection_height]' : resource_selection_selection_height,
        'config_type' : config_type,
        'config_xml' : config_xml,
        'config_url' : config_url,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, external_tool_id=external_tool_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def edit_external_tool_accounts(request_ctx, account_id, external_tool_id, name=None, privacy_level=None, consumer_key=None, shared_secret=None, description=None, url=None, domain=None, icon_url=None, text=None, custom_fields=None, account_navigation_url=None, account_navigation_enabled=None, account_navigation_text=None, user_navigation_url=None, user_navigation_enabled=None, user_navigation_text=None, course_navigation_url=None, course_navigation_enabled=None, course_navigation_text=None, course_navigation_visibility=None, course_navigation_default=None, editor_button_url=None, editor_button_enabled=None, editor_button_icon_url=None, editor_button_selection_width=None, editor_button_selection_height=None, resource_selection_url=None, resource_selection_enabled=None, resource_selection_icon_url=None, resource_selection_selection_width=None, resource_selection_selection_height=None, config_type=None, config_xml=None, config_url=None, **request_kwargs):
    """
    Update the specified external tool. Uses same parameters as create

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :param name: (optional) The name of the tool
        :type name: string or None
        :param privacy_level: (optional) What information to send to the external tool.
        :type privacy_level: string or None
        :param consumer_key: (optional) The consumer key for the external tool
        :type consumer_key: string or None
        :param shared_secret: (optional) The shared secret with the external tool
        :type shared_secret: string or None
        :param description: (optional) A description of the tool
        :type description: string or None
        :param url: (optional) The url to match links against. Either "url" or "domain" should be set, not both.
        :type url: string or None
        :param domain: (optional) The domain to match links against. Either "url" or "domain" should be set, not both.
        :type domain: string or None
        :param icon_url: (optional) The url of the icon to show for this tool
        :type icon_url: string or None
        :param text: (optional) The default text to show for this tool
        :type text: string or None
        :param custom_fields: (optional) Custom fields that will be sent to the tool consumer, specified as custom_fields[field_name]
        :type custom_fields: string or None
        :param account_navigation_url: (optional) The url of the external tool for account navigation
        :type account_navigation_url: string or None
        :param account_navigation_enabled: (optional) Set this to enable this feature
        :type account_navigation_enabled: boolean or None
        :param account_navigation_text: (optional) The text that will show on the left-tab in the account navigation
        :type account_navigation_text: string or None
        :param user_navigation_url: (optional) The url of the external tool for user navigation
        :type user_navigation_url: string or None
        :param user_navigation_enabled: (optional) Set this to enable this feature
        :type user_navigation_enabled: boolean or None
        :param user_navigation_text: (optional) The text that will show on the left-tab in the user navigation
        :type user_navigation_text: string or None
        :param course_navigation_url: (optional) The url of the external tool for course navigation
        :type course_navigation_url: string or None
        :param course_navigation_enabled: (optional) Set this to enable this feature
        :type course_navigation_enabled: boolean or None
        :param course_navigation_text: (optional) The text that will show on the left-tab in the course navigation
        :type course_navigation_text: string or None
        :param course_navigation_visibility: (optional) Who will see the navigation tab. "admins" for course admins, "members" for students, null for everyone
        :type course_navigation_visibility: string or None
        :param course_navigation_default: (optional) Whether the navigation option will show in the course by default or whether the teacher will have to explicitly enable it
        :type course_navigation_default: boolean or None
        :param editor_button_url: (optional) The url of the external tool
        :type editor_button_url: string or None
        :param editor_button_enabled: (optional) Set this to enable this feature
        :type editor_button_enabled: boolean or None
        :param editor_button_icon_url: (optional) The url of the icon to show in the WYSIWYG editor
        :type editor_button_icon_url: string or None
        :param editor_button_selection_width: (optional) The width of the dialog the tool is launched in
        :type editor_button_selection_width: string or None
        :param editor_button_selection_height: (optional) The height of the dialog the tool is launched in
        :type editor_button_selection_height: string or None
        :param resource_selection_url: (optional) The url of the external tool
        :type resource_selection_url: string or None
        :param resource_selection_enabled: (optional) Set this to enable this feature
        :type resource_selection_enabled: boolean or None
        :param resource_selection_icon_url: (optional) The url of the icon to show in the module external tool list
        :type resource_selection_icon_url: string or None
        :param resource_selection_selection_width: (optional) The width of the dialog the tool is launched in
        :type resource_selection_selection_width: string or None
        :param resource_selection_selection_height: (optional) The height of the dialog the tool is launched in
        :type resource_selection_selection_height: string or None
        :param config_type: (optional) Configuration can be passed in as CC xml instead of using query parameters. If this value is "by_url" or "by_xml" then an xml configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the xml
        :type config_type: string or None
        :param config_xml: (optional) XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_xml"
        :type config_xml: string or None
        :param config_url: (optional) URL where the server can retrieve an XML tool configuration, as specified in the CC xml specification. This is required if "config_type" is set to "by_url"
        :type config_url: string or None
        :return: Edit an external tool
        :rtype: requests.Response (with void data)

    """

    privacy_level_types = ('anonymous', 'name_only', 'public')
    course_navigation_visibility_types = ('admins', 'members')
    utils.validate_attr_is_acceptable(privacy_level, privacy_level_types)
    utils.validate_attr_is_acceptable(course_navigation_visibility, course_navigation_visibility_types)
    path = '/v1/accounts/{account_id}/external_tools/{external_tool_id}'
    payload = {
        'name': name,
        'privacy_level': privacy_level,
        'consumer_key': consumer_key,
        'shared_secret': shared_secret,
        'description': description,
        'url': url,
        'domain': domain,
        'icon_url': icon_url,
        'text' : text,
        'custom_fields' : custom_fields,
        'account_navigation[url]' : account_navigation_url,
        'account_navigation[enabled]' : account_navigation_enabled,
        'account_navigation[text]' : account_navigation_text,
        'user_navigation[url]' : user_navigation_url,
        'user_navigation[enabled]' : user_navigation_enabled,
        'user_navigation[text]' : user_navigation_text,
        'course_navigation[url]' : course_navigation_url,
        'course_navigation[enabled]' : course_navigation_enabled,
        'course_navigation[text]' : course_navigation_text,
        'course_navigation[visibility]' : course_navigation_visibility,
        'course_navigation[default]' : course_navigation_default,
        'editor_button[url]' : editor_button_url,
        'editor_button[enabled]' : editor_button_enabled,
        'editor_button[icon_url]' : editor_button_icon_url,
        'editor_button[selection_width]' : editor_button_selection_width,
        'editor_button[selection_height]' : editor_button_selection_height,
        'resource_selection[url]' : resource_selection_url,
        'resource_selection[enabled]' : resource_selection_enabled,
        'resource_selection[icon_url]' : resource_selection_icon_url,
        'resource_selection[selection_width]' : resource_selection_selection_width,
        'resource_selection[selection_height]' : resource_selection_selection_height,
        'config_type' : config_type,
        'config_xml' : config_xml,
        'config_url' : config_url,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, external_tool_id=external_tool_id)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def delete_external_tool_courses(request_ctx, course_id, external_tool_id, **request_kwargs):
    """
    Remove the specified external tool

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :return: Delete an external tool
        :rtype: requests.Response (with void data)

    """

    path = '/v1/courses/{course_id}/external_tools/{external_tool_id}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, external_tool_id=external_tool_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_external_tool_accounts(request_ctx, account_id, external_tool_id, **request_kwargs):
    """
    Remove the specified external tool

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param external_tool_id: (required) ID
        :type external_tool_id: string
        :return: Delete an external tool
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/external_tools/{external_tool_id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, external_tool_id=external_tool_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


