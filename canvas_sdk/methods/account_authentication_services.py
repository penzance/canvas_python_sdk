from canvas_sdk import client, utils

def list_authorization_configs(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    Returns the list of authorization configs

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List Authorization Configs
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


def create_authorization_config(request_ctx, account_id, **request_kwargs):
    """
    Add external account authentication service(s) for the account.
    Services may be CAS, SAML, or LDAP.
    
    Each authentication service is specified as a set of parameters as
    described below. A service specification must include an 'auth_type'
    parameter with a value of 'cas', 'saml', or 'ldap'. The other recognized
    parameters depend on this auth_type; unrecognized parameters are discarded.
    Service specifications not specifying a valid auth_type are ignored.
    
    Any service specification may include an optional 'login_handle_name'
    parameter. This parameter specifies the label used for unique login
    identifiers; for example: 'Login', 'Username', 'Student ID', etc. The
    default is 'Email'.
    
    You can set the 'position' for any configuration. The config in the 1st position
    is considered the default.
    
    For CAS authentication services, the additional recognized parameters are:
    
    - auth_base
    
      The CAS server's URL.
    
    - log_in_url [Optional]
    
      An alternate SSO URL for logging into CAS. You probably should not set
      this.
    
    For SAML authentication services, the additional recognized parameters are:
    
    - idp_entity_id
    
      The SAML IdP's entity ID - This is used to look up the correct SAML IdP if
      multiple are configured
    
    - log_in_url
    
      The SAML service's SSO target URL
    
    - log_out_url
    
      The SAML service's SLO target URL
    
    - certificate_fingerprint
    
      The SAML service's certificate fingerprint.
    
    - change_password_url [Optional]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
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
    
    For LDAP authentication services, the additional recognized parameters are:
    
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
    
    - change_password_url [Optional]
    
      Forgot Password URL. Leave blank for default Canvas behavior.
    
    - account_authorization_config[n] (deprecated)
      The nth service specification as described above. For instance, the
      auth_type of the first service is given by the
      account_authorization_config[0][auth_type] parameter. There must be
      either a single CAS or SAML specification, or one or more LDAP
      specifications. Additional services after an initial CAS or SAML service
      are ignored; additional non-LDAP services after an initial LDAP service
      are ignored.
    
    _Deprecated_ Examples:
    
    This endpoint still supports a deprecated version of setting the authorization configs.
    If you send data in this format it is considered a snapshot of how the configs
    should be setup and will clear any configs not sent.
    
    Simple CAS server integration.
    
      account_authorization_config[0][auth_type]=cas&
      account_authorization_config[0][auth_base]=cas.mydomain.edu
    
    Single SAML server integration.
    
      account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2
      account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&
      account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&
      account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&
      account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
    
    Two SAML server integration with discovery url.
    
      discovery_url=http://www.myschool.com/sso/identity_provider_selection
      account_authorization_config[0][idp_entity_id]=http://idp.myschool.com/sso/saml2&
      account_authorization_config[0][log_in_url]=saml-sso.mydomain.com&
      account_authorization_config[0][log_out_url]=saml-slo.mydomain.com&
      account_authorization_config[0][certificate_fingerprint]=1234567890ABCDEF&
      account_authorization_config[0][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress&
      account_authorization_config[1][idp_entity_id]=http://idp.otherschool.com/sso/saml2&
      account_authorization_config[1][log_in_url]=saml-sso.otherdomain.com&
      account_authorization_config[1][log_out_url]=saml-slo.otherdomain.com&
      account_authorization_config[1][certificate_fingerprint]=ABCDEFG12345678789&
      account_authorization_config[1][identifier_format]=urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
    
    Single LDAP server integration.
    
      account_authorization_config[0][auth_type]=ldap&
      account_authorization_config[0][auth_host]=ldap.mydomain.edu&
      account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&
      account_authorization_config[0][auth_username]=username&
      account_authorization_config[0][auth_password]=password
    
    Multiple LDAP server integration.
    
      account_authorization_config[0][auth_type]=ldap&
      account_authorization_config[0][auth_host]=faculty-ldap.mydomain.edu&
      account_authorization_config[0][auth_filter]=(sAMAccountName={{login}})&
      account_authorization_config[0][auth_username]=username&
      account_authorization_config[0][auth_password]=password&
      account_authorization_config[1][auth_type]=ldap&
      account_authorization_config[1][auth_host]=student-ldap.mydomain.edu&
      account_authorization_config[1][auth_filter]=(sAMAccountName={{login}})&
      account_authorization_config[1][auth_username]=username&
      account_authorization_config[1][auth_password]=password

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Create Authorization Config
        :rtype: requests.Response (with AccountAuthorizationConfig data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def update_authorization_config(request_ctx, account_id, id, **request_kwargs):
    """
    Update an authorization config using the same options as the create endpoint.
    You can not update an existing configuration to a new authentication type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Update Authorization Config
        :rtype: requests.Response (with AccountAuthorizationConfig data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def get_authorization_config(request_ctx, account_id, id, **request_kwargs):
    """
    Get the specified authorization config

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get Authorization Config
        :rtype: requests.Response (with AccountAuthorizationConfig data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def delete_authorization_config(request_ctx, account_id, id, **request_kwargs):
    """
    Delete the config

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Delete Authorization Config
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def get_discovery_url(request_ctx, account_id, **request_kwargs):
    """
    Get the discovery url

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: GET discovery url
        :rtype: requests.Response (with DiscoveryUrl data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def set_discovery_url(request_ctx, account_id, **request_kwargs):
    """
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
        :return: Set discovery url
        :rtype: requests.Response (with DiscoveryUrl data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def delete_discovery_url(request_ctx, account_id, **request_kwargs):
    """
    Clear discovery url

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: Delete discovery url
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/account_authorization_configs/discovery_url'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


