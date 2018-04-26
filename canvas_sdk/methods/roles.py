from canvas_sdk import client, utils

def list_roles(request_ctx, account_id, state, per_page=None, **request_kwargs):
    """
    List the roles available to an account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The id of the account to retrieve roles for.
        :type account_id: string
        :param state: (required) Filter by role state. If this argument is omitted, only 'active' roles are returned.
        :type state: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List roles
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    state_types = ('active', 'inactive')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/accounts/{account_id}/roles'
    payload = {
        'state[]' : state,
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_single_role(request_ctx, account_id, role, **request_kwargs):
    """
    Retrieve information about a single role

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) The id of the account containing the role
        :type account_id: string
        :param role: (required) The name and unique identifier for the role
        :type role: string
        :return: Get a single role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{role}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, role=role)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def create_new_role(request_ctx, account_id, role, base_role_type=None, permissions={}, **request_kwargs):
    """
    Create a new course-level or account-level role.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param role: (required) Label and unique identifier for the role.
        :type role: string
        :param base_role_type: (optional) Specifies the role type that will be used as a base for the permissions granted to this role. Defaults to 'AccountMembership' if absent
        :type base_role_type: string or None
        :param permissions: (optional) Specifies the permissions that will be granted to this role. See Canvas API docs for details on the structure.
        :type permissions: dict
        :return: Create a new role
        :rtype: requests.Response (with Role data)

    """

    base_role_type_types = ('AccountMembership', 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', 'DesignerEnrollment')
    utils.validate_attr_is_acceptable(base_role_type, base_role_type_types)
    path = '/v1/accounts/{account_id}/roles'
    payload = {
        'role' : role,
        'base_role_type' : base_role_type,
    }
    # flatten the permissions dict
    for p in permissions:
        for a in permissions[p]:
            payload['permissions[{}][{}]'.format(p, a)] = permissions[p][a]

    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def deactivate_role(request_ctx, account_id, role, **request_kwargs):
    """
    Deactivates a custom role.  This hides it in the user interface and prevents it
    from being assigned to new users.  Existing users assigned to the role will
    continue to function with the same permissions they had previously.
    Built-in roles cannot be deactivated.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param role: (required) Label and unique identifier for the role.
        :type role: string
        :return: Deactivate a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{role}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, role=role)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def activate_role(request_ctx, account_id, role, **request_kwargs):
    """
    Re-activates an inactive role (allowing it to be assigned to new users)

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param role: (required) Label and unique identifier for the role.
        :type role: string
        :return: Activate a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{role}/activate'
    url = request_ctx.base_api_url + path.format(account_id=account_id, role=role)
    response = client.post(request_ctx, url, **request_kwargs)

    return response


def update_role(request_ctx, account_id, role, label=None, permissions={}, **request_kwargs):
    """
    Update permissions for an existing role.

    Recognized roles are:
    * TeacherEnrollment
    * StudentEnrollment
    * TaEnrollment
    * ObserverEnrollment
    * DesignerEnrollment
    * AccountAdmin
    * Any previously created custom role

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param role: (required) ID
        :type role: string
        :param label: The label for the role. Can only change the label of a custom role that belongs directly to the account.
        :type label: string
        :param permissions: (optional) Specifies the permissions that will be granted to this role. See Canvas API docs for details on the structure.
        :type permissions: dict
        :return: Update a role
        :rtype: requests.Response (with Role data)

    """

    path = '/v1/accounts/{account_id}/roles/{role}'
    payload = {}
    if label and label != '':
        payload['label'] = label
    # flatten the permissions dict
    for p in permissions:
        for a in permissions[p]:
            payload['permissions[{}][{}]'.format(p, a)] = permissions[p][a]
    
    url = request_ctx.base_api_url + path.format(account_id=account_id, role=role)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response
