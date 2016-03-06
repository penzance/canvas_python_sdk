from canvas_sdk import client, utils


def list_features_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    List all features that apply to a given Account, Course, or User.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List features
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/features'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_features_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    List all features that apply to a given Account, Course, or User.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List features
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/features'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_features_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    List all features that apply to a given Account, Course, or User.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List features
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/features'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enabled_features_courses(request_ctx, course_id, per_page=None, **request_kwargs):
    """
    List all features that are enabled on a given Account, Course, or User.
    Only the feature names are returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enabled features
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/courses/{course_id}/features/enabled'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enabled_features_accounts(request_ctx, account_id, per_page=None, **request_kwargs):
    """
    List all features that are enabled on a given Account, Course, or User.
    Only the feature names are returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enabled features
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/features/enabled'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def list_enabled_features_users(request_ctx, user_id, per_page=None, **request_kwargs):
    """
    List all features that are enabled on a given Account, Course, or User.
    Only the feature names are returned.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List enabled features
        :rtype: requests.Response (with void data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/users/{user_id}/features/enabled'
    payload = {
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_feature_flag_courses(request_ctx, course_id, feature, **request_kwargs):
    """
    Get the feature flag that applies to a given Account, Course, or User.
    The flag may be defined on the object, or it may be inherited from a parent
    account. You can look at the context_id and context_type of the returned object
    to determine which is the case. If these fields are missing, then the object
    is the global Canvas default.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Get feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/courses/{course_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, feature=feature)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_feature_flag_accounts(request_ctx, account_id, feature, **request_kwargs):
    """
    Get the feature flag that applies to a given Account, Course, or User.
    The flag may be defined on the object, or it may be inherited from a parent
    account. You can look at the context_id and context_type of the returned object
    to determine which is the case. If these fields are missing, then the object
    is the global Canvas default.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Get feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/accounts/{account_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, feature=feature)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def get_feature_flag_users(request_ctx, user_id, feature, **request_kwargs):
    """
    Get the feature flag that applies to a given Account, Course, or User.
    The flag may be defined on the object, or it may be inherited from a parent
    account. You can look at the context_id and context_type of the returned object
    to determine which is the case. If these fields are missing, then the object
    is the global Canvas default.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Get feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/users/{user_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, feature=feature)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


def set_feature_flag_courses(request_ctx, course_id, feature, state=None, locking_account_id=None, **request_kwargs):
    """
    Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
    a feature flag for the same feature in any state other than "allowed".

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param feature: (required) ID
        :type feature: string
        :param state: (optional) "off":: The feature is not available for the course, user, or account and sub-accounts.
"allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
            sub-accounts and courses by setting a feature flag on the sub-account or course.
"on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts.
        :type state: string or None
        :param locking_account_id: (optional) If set, this FeatureFlag may only be modified by someone with administrative rights
in the specified account. The locking account must be above the target object in the
account chain.
        :type locking_account_id: integer or None
        :return: Set feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    state_types = ('off', 'allowed', 'on')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/courses/{course_id}/features/flags/{feature}'
    payload = {
        'state': state,
        'locking_account_id': locking_account_id,
    }
    url = request_ctx.base_api_url + path.format(course_id=course_id, feature=feature)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def set_feature_flag_accounts(request_ctx, account_id, feature, state=None, locking_account_id=None, **request_kwargs):
    """
    Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
    a feature flag for the same feature in any state other than "allowed".

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param feature: (required) ID
        :type feature: string
        :param state: (optional) "off":: The feature is not available for the course, user, or account and sub-accounts.
"allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
            sub-accounts and courses by setting a feature flag on the sub-account or course.
"on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts.
        :type state: string or None
        :param locking_account_id: (optional) If set, this FeatureFlag may only be modified by someone with administrative rights
in the specified account. The locking account must be above the target object in the
account chain.
        :type locking_account_id: integer or None
        :return: Set feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    state_types = ('off', 'allowed', 'on')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/accounts/{account_id}/features/flags/{feature}'
    payload = {
        'state': state,
        'locking_account_id': locking_account_id,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, feature=feature)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def set_feature_flag_users(request_ctx, user_id, feature, state=None, locking_account_id=None, **request_kwargs):
    """
    Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
    a feature flag for the same feature in any state other than "allowed".

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param feature: (required) ID
        :type feature: string
        :param state: (optional) "off":: The feature is not available for the course, user, or account and sub-accounts.
"allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
            sub-accounts and courses by setting a feature flag on the sub-account or course.
"on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts.
        :type state: string or None
        :param locking_account_id: (optional) If set, this FeatureFlag may only be modified by someone with administrative rights
in the specified account. The locking account must be above the target object in the
account chain.
        :type locking_account_id: integer or None
        :return: Set feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    state_types = ('off', 'allowed', 'on')
    utils.validate_attr_is_acceptable(state, state_types)
    path = '/v1/users/{user_id}/features/flags/{feature}'
    payload = {
        'state': state,
        'locking_account_id': locking_account_id,
    }
    url = request_ctx.base_api_url + path.format(user_id=user_id, feature=feature)
    response = client.put(request_ctx, url, payload=payload, **request_kwargs)

    return response


def remove_feature_flag_courses(request_ctx, course_id, feature, **request_kwargs):
    """
    Remove feature flag for a given Account, Course, or User.  (Note that the flag must
    be defined on the Account, Course, or User directly.)  The object will then inherit
    the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
    then lower-level account flags that were masked by this one will apply again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param course_id: (required) ID
        :type course_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Remove feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/courses/{course_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(course_id=course_id, feature=feature)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def remove_feature_flag_accounts(request_ctx, account_id, feature, **request_kwargs):
    """
    Remove feature flag for a given Account, Course, or User.  (Note that the flag must
    be defined on the Account, Course, or User directly.)  The object will then inherit
    the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
    then lower-level account flags that were masked by this one will apply again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Remove feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/accounts/{account_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, feature=feature)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


def remove_feature_flag_users(request_ctx, user_id, feature, **request_kwargs):
    """
    Remove feature flag for a given Account, Course, or User.  (Note that the flag must
    be defined on the Account, Course, or User directly.)  The object will then inherit
    the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
    then lower-level account flags that were masked by this one will apply again.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param user_id: (required) ID
        :type user_id: string
        :param feature: (required) ID
        :type feature: string
        :return: Remove feature flag
        :rtype: requests.Response (with FeatureFlag data)

    """

    path = '/v1/users/{user_id}/features/flags/{feature}'
    url = request_ctx.base_api_url + path.format(user_id=user_id, feature=feature)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


