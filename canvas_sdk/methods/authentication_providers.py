from canvas_sdk import client, utils

def list_authentication_providers_authentication_providers(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the list of authentication providers

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List authentication providers
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/authentication_providers'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_authentication_providers_account_authorization_configs(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the list of authentication providers

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List authentication providers
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/account_authorization_configs'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def add_authentication_provider_authentication_providers(request_ctx, account_id, **request_kwargs):
    """
    Add external authentication provider(s) for the account.
    Services may be CAS, Facebook, GitHub, Google, LDAP, OpenID Connect,
    LinkedIn, SAML, or Twitter.
    
    Each authentication provider is specified as a set of parameters as
    described below. A provider specification must include an 'auth_type'
    parameter with a value of 'canvas', 'cas', 'facebook', 'github', 'google',
    'ldap', 'linkedin', 'openid_connect', 'saml', or 'twitter'. The other recognized
    parameters depend on this auth_type; unrecognized parameters are discarded.
    Provider specifications not specifying a valid auth_type are ignored.
    
    _Deprecated_[2015-05-08] Any provider specification may include an
    optional 'login_handle_name' parameter. This parameter specifies the
    label used for unique login identifiers; for example: 'Login',
    'Username', 'Student ID', etc. The default is 'Email'.
    _Deprecated_[2015-05-20] Any provider specification besides LDAP may include
    an optional 'unknown_user_url' parameters. This parameters specifies a url
    to redirect to when a user is authorized but is not found in Canvas.
    _Deprecated_ [Use update_sso_settings instead]
    
    You can set the 'position' for any configuration. The config in the 1st position
    is considered the default. You can set 'jit_provisioning' for any configuration
    besides Canvas.
    
    For Canvas, the additional recognized parameter is:
    
    - self_registration
    
      'all', 'none', or 'observer' - who is allowed to register as a new user
    
    For CAS, the additional recognized parameters are:
    
    - auth_base
    
      The CAS server's URL.
    
    - log_in_url [Optional]
    
      An alternate SSO URL for logging into CAS. You probably should not set
      this.
    
    - unknown_user_url [Optional] _Deprecated_ [2015-05-20: use update_sso_settings instead]
    
      A url to redirect to when a user is authorized through CAS but is not
      found in Canvas.
    
    For Facebook, the additional recognized parameters are:
    
    - app_id [Required]
    
      The Facebook App ID. Not available if configured globally for Canvas.
    
    - app_secret [Required]
    
      The Facebook App Secret. Not available if configured globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'email'
    
    For GitHub, the additional recognized parameters are:
    
    - domain [Optional]
    
      The domain of a GitHub Enterprise installation. I.e.
      github.mycompany.com. If not set, it will default to the public
      github.com.
    
    - client_id [Required]
    
      The GitHub application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The GitHub application's Client Secret. Not available if configured
      globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'login'
    
    For Google, the additional recognized parameters are:
    
    - client_id [Required]
    
      The Google application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The Google application's Client Secret. Not available if configured
      globally for Canvas.
    
    - hosted_domain [Optional]
    
      A Google Apps domain to restrict logins to. See
      https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'sub' (the default), or 'email'
    
    For LDAP, the additional recognized parameters are:
    
    - auth_host
    
      The LDAP server's URL.
    
    - auth_port [Optional, Integer]
    
      The LDAP server's TCP port. (default: 389)
    
    - auth_over_tls [Optional]
    
      Whether to use TLS. Can be '', 'simple_tls', or 'start_tls'. For backwards
      compatibility, booleans are also accepted, with true meaning simple_tls.
      If not provided, it will default to start_tls.
    
    - auth_base [Optional]
    
      A default treebase parameter for searches performed against the LDAP
      server.
    
    - auth_filter
    
      LDAP search filter. Use !{{login}} as a placeholder for the username
      supplied by the user. For example: "(sAMAccountName=!{{login}})".
    
    - identifier_format [Optional]
    
      The LDAP attribute to use to look up the Canvas login. Omit to use
      the username supplied by the user.
    
    - auth_username
    
      Username
    
    - auth_password
    
      Password
    
    - change_password_url [Optional] _Deprecated_ [2015-05-08: use update_sso_settings instead]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
    For LinkedIn, the additional recognized parameters are:
    
    - client_id [Required]
    
      The LinkedIn application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The LinkedIn application's Client Secret. Not available if configured
      globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'emailAddress'
    
    For OpenID Connect, the additional recognized parameters are:
    
    - client_id [Required]
    
      The application's Client ID.
    
    - client_secret [Required]
    
      The application's Client Secret.
    
    - authorize_url [Required]
    
      The URL for getting starting the OAuth 2.0 web flow
    
    - token_url [Required]
    
      The URL for exchanging the OAuth 2.0 authorization code for an access
      token and id token
    
    - scope [Optional]
    
      Space separated additional scopes to request for the token.
    
    - login_attribute [Optional]
    
      The attribute of the ID token to look up the user's login in Canvas.
      Defaults to 'sub'.
    
    For SAML, the additional recognized parameters are:
    
    - idp_entity_id
    
      The SAML IdP's entity ID
    
    - log_in_url
    
      The SAML service's SSO target URL
    
    - log_out_url
    
      The SAML service's SLO target URL
    
    - certificate_fingerprint
    
      The SAML service's certificate fingerprint.
    
    - change_password_url [Optional] _Deprecated_ [2015-05-08: use update_sso_settings instead]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
    - unknown_user_url [Optional] _Deprecated_ [2015-05-20: use update_sso_settings instead]
    
      A url to redirect to when a user is authorized through SAML but is not
      found in Canvas.
    
    - identifier_format
    
      The SAML service's identifier format. Must be one of:
    
      - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
      - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
      - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
      - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
      - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
      - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
      - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
      - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName
    
    - requested_authn_context
    
      The SAML AuthnContext
    
    For Twitter, the additional recognized parameters are:
    
    - consumer_key [Required]
    
      The Twitter Consumer Key. Not available if configured globally for Canvas.
    
    - consumer_secret [Required]
    
      The Twitter Consumer Secret. Not available if configured globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'user_id' (the default), or 'screen_name'
    
    - parent_registration [Optional]
    
      Accepts a boolean value, true designates the authentication service
      for use on parent registrations.  Only one service can be selected
      at a time so if set to true all others will be set to false

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Add authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/authentication_providers'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def add_authentication_provider_account_authorization_configs(request_ctx, account_id, **request_kwargs):
    """
    Add external authentication provider(s) for the account.
    Services may be CAS, Facebook, GitHub, Google, LDAP, OpenID Connect,
    LinkedIn, SAML, or Twitter.
    
    Each authentication provider is specified as a set of parameters as
    described below. A provider specification must include an 'auth_type'
    parameter with a value of 'canvas', 'cas', 'facebook', 'github', 'google',
    'ldap', 'linkedin', 'openid_connect', 'saml', or 'twitter'. The other recognized
    parameters depend on this auth_type; unrecognized parameters are discarded.
    Provider specifications not specifying a valid auth_type are ignored.
    
    _Deprecated_[2015-05-08] Any provider specification may include an
    optional 'login_handle_name' parameter. This parameter specifies the
    label used for unique login identifiers; for example: 'Login',
    'Username', 'Student ID', etc. The default is 'Email'.
    _Deprecated_[2015-05-20] Any provider specification besides LDAP may include
    an optional 'unknown_user_url' parameters. This parameters specifies a url
    to redirect to when a user is authorized but is not found in Canvas.
    _Deprecated_ [Use update_sso_settings instead]
    
    You can set the 'position' for any configuration. The config in the 1st position
    is considered the default. You can set 'jit_provisioning' for any configuration
    besides Canvas.
    
    For Canvas, the additional recognized parameter is:
    
    - self_registration
    
      'all', 'none', or 'observer' - who is allowed to register as a new user
    
    For CAS, the additional recognized parameters are:
    
    - auth_base
    
      The CAS server's URL.
    
    - log_in_url [Optional]
    
      An alternate SSO URL for logging into CAS. You probably should not set
      this.
    
    - unknown_user_url [Optional] _Deprecated_ [2015-05-20: use update_sso_settings instead]
    
      A url to redirect to when a user is authorized through CAS but is not
      found in Canvas.
    
    For Facebook, the additional recognized parameters are:
    
    - app_id [Required]
    
      The Facebook App ID. Not available if configured globally for Canvas.
    
    - app_secret [Required]
    
      The Facebook App Secret. Not available if configured globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'email'
    
    For GitHub, the additional recognized parameters are:
    
    - domain [Optional]
    
      The domain of a GitHub Enterprise installation. I.e.
      github.mycompany.com. If not set, it will default to the public
      github.com.
    
    - client_id [Required]
    
      The GitHub application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The GitHub application's Client Secret. Not available if configured
      globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'login'
    
    For Google, the additional recognized parameters are:
    
    - client_id [Required]
    
      The Google application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The Google application's Client Secret. Not available if configured
      globally for Canvas.
    
    - hosted_domain [Optional]
    
      A Google Apps domain to restrict logins to. See
      https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'sub' (the default), or 'email'
    
    For LDAP, the additional recognized parameters are:
    
    - auth_host
    
      The LDAP server's URL.
    
    - auth_port [Optional, Integer]
    
      The LDAP server's TCP port. (default: 389)
    
    - auth_over_tls [Optional]
    
      Whether to use TLS. Can be '', 'simple_tls', or 'start_tls'. For backwards
      compatibility, booleans are also accepted, with true meaning simple_tls.
      If not provided, it will default to start_tls.
    
    - auth_base [Optional]
    
      A default treebase parameter for searches performed against the LDAP
      server.
    
    - auth_filter
    
      LDAP search filter. Use !{{login}} as a placeholder for the username
      supplied by the user. For example: "(sAMAccountName=!{{login}})".
    
    - identifier_format [Optional]
    
      The LDAP attribute to use to look up the Canvas login. Omit to use
      the username supplied by the user.
    
    - auth_username
    
      Username
    
    - auth_password
    
      Password
    
    - change_password_url [Optional] _Deprecated_ [2015-05-08: use update_sso_settings instead]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
    For LinkedIn, the additional recognized parameters are:
    
    - client_id [Required]
    
      The LinkedIn application's Client ID. Not available if configured globally
      for Canvas.
    
    - client_secret [Required]
    
      The LinkedIn application's Client Secret. Not available if configured
      globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'id' (the default), or 'emailAddress'
    
    For OpenID Connect, the additional recognized parameters are:
    
    - client_id [Required]
    
      The application's Client ID.
    
    - client_secret [Required]
    
      The application's Client Secret.
    
    - authorize_url [Required]
    
      The URL for getting starting the OAuth 2.0 web flow
    
    - token_url [Required]
    
      The URL for exchanging the OAuth 2.0 authorization code for an access
      token and id token
    
    - scope [Optional]
    
      Space separated additional scopes to request for the token.
    
    - login_attribute [Optional]
    
      The attribute of the ID token to look up the user's login in Canvas.
      Defaults to 'sub'.
    
    For SAML, the additional recognized parameters are:
    
    - idp_entity_id
    
      The SAML IdP's entity ID
    
    - log_in_url
    
      The SAML service's SSO target URL
    
    - log_out_url
    
      The SAML service's SLO target URL
    
    - certificate_fingerprint
    
      The SAML service's certificate fingerprint.
    
    - change_password_url [Optional] _Deprecated_ [2015-05-08: use update_sso_settings instead]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
    - unknown_user_url [Optional] _Deprecated_ [2015-05-20: use update_sso_settings instead]
    
      A url to redirect to when a user is authorized through SAML but is not
      found in Canvas.
    
    - identifier_format
    
      The SAML service's identifier format. Must be one of:
    
      - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
      - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
      - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
      - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
      - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
      - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
      - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
      - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName
    
    - requested_authn_context
    
      The SAML AuthnContext
    
    For Twitter, the additional recognized parameters are:
    
    - consumer_key [Required]
    
      The Twitter Consumer Key. Not available if configured globally for Canvas.
    
    - consumer_secret [Required]
    
      The Twitter Consumer Secret. Not available if configured globally for Canvas.
    
    - login_attribute [Optional]
    
      The attribute to use to look up the user's login in Canvas. Either
      'user_id' (the default), or 'screen_name'
    
    - parent_registration [Optional]
    
      Accepts a boolean value, true designates the authentication service
      for use on parent registrations.  Only one service can be selected
      at a time so if set to true all others will be set to false

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Add authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def update_authentication_provider_authentication_providers(request_ctx, account_id, id, **request_kwargs):
    """
    Update an authentication provider using the same options as the create endpoint.
    You can not update an existing provider to a new authentication type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Update authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/authentication_providers/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def update_authentication_provider_account_authorization_configs(request_ctx, account_id, id, **request_kwargs):
    """
    Update an authentication provider using the same options as the create endpoint.
    You can not update an existing provider to a new authentication type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Update authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def get_authentication_provider_authentication_providers(request_ctx, account_id, id, **request_kwargs):
    """
    Get the specified authentication provider

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/authentication_providers/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_authentication_provider_account_authorization_configs(request_ctx, account_id, id, **request_kwargs):
    """
    Get the specified authentication provider

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get authentication provider
        :rtype: requests.Response (with AuthenticationProvider data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def delete_authentication_provider_authentication_providers(request_ctx, account_id, id, **request_kwargs):
    """
    Delete the config

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete authentication provider
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/authentication_providers/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def delete_authentication_provider_account_authorization_configs(request_ctx, account_id, id, **request_kwargs):
    """
    Delete the config

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete authentication provider
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def get_discovery_url_deprecated(request_ctx, account_id, **request_kwargs):
    """
    Get the discovery url _Deprecated_[2015-05-08]
    
    [Use update_sso_settings instead]

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: GET discovery url _Deprecated_[2015-05-08]
        :rtype: requests.Response (with DiscoveryUrl data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def set_discovery_url_deprecated(request_ctx, account_id, **request_kwargs):
    """
    [Use update_sso_settings instead]
    
    If you have multiple IdPs configured, you can set a `discovery_url`.
    If that is set, canvas will forward all users to that URL when they need to
    be authenticated. That page will need to then help the user figure out where
    they need to go to log in.
    
    If no discovery url is configured, the 1st auth config will be used to
    attempt to authenticate the user.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Set discovery url _Deprecated_[2015-05-08]
        :rtype: requests.Response (with DiscoveryUrl data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def delete_discovery_url_deprecated(request_ctx, account_id, **request_kwargs):
    """
    Clear discovery url _Deprecated_[2015-05-08]
    
    [Use update_sso_settings instead]

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Delete discovery url _Deprecated_[2015-05-08]
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def show_account_auth_settings(request_ctx, account_id, **request_kwargs):
    """
    The way to get the current state of each account level setting
    that's relevant to Single Sign On configuration
    
    You can list the current state of each setting with "update_sso_settings"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: show account auth settings
        :rtype: requests.Response (with SSOSettings data)

    """

    path = '/v1/accounts/{account_id}/sso_settings'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def update_account_auth_settings(request_ctx, account_id, **request_kwargs):
    """
    For various cases of mixed SSO configurations, you may need to set some
    configuration at the account level to handle the particulars of your
    setup.
    
    This endpoint accepts a PUT request to set several possible account
    settings. All setting are optional on each request, any that are not
    provided at all are simply retained as is.  Any that provide the key but
    a null-ish value (blank string, null, undefined) will be UN-set.
    
    You can list the current state of each setting with "show_sso_settings"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: update account auth settings
        :rtype: requests.Response (with SSOSettings data)

    """

    path = '/v1/accounts/{account_id}/sso_settings'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


