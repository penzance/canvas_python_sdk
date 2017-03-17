from canvas_sdk import client, utils


def share_brandconfig_theme(request_ctx, account_id, shared_brand_config_name, shared_brand_config_brand_config_md5, **request_kwargs):
    """
    Create a SharedBrandConfig, which will give the given brand_config a name
    and make it available to other users of this account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param shared_brand_config_name: (required) Name to share this BrandConfig (theme) as.
        :type shared_brand_config_name: string
        :param shared_brand_config_brand_config_md5: (required) MD5 of brand_config to share
        :type shared_brand_config_brand_config_md5: string
        :return: Share a BrandConfig (Theme)
        :rtype: requests.Response (with SharedBrandConfig data)

    """

    path = '/v1/accounts/{account_id}/shared_brand_configs'
    payload = {
        'shared_brand_config[name]': shared_brand_config_name,
        'shared_brand_config[brand_config_md5]': shared_brand_config_brand_config_md5,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def update_shared_theme(request_ctx, account_id, id, **request_kwargs):
    """
    Update the specified shared_brand_config with a new name or to point to a new brand_config.
    Uses same parameters as create.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Update a shared theme
        :rtype: requests.Response (with SharedBrandConfig data)

    """

    path = '/v1/accounts/{account_id}/shared_brand_configs/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.put(request_ctx, url, **request_kwargs)

    return response


def un_share_brandconfig_theme(request_ctx, id, **request_kwargs):
    """
    Delete a SharedBrandConfig, which will unshare it so you nor anyone else in
    your account will see it as an option to pick from.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param id: (required) ID
        :type id: string
        :return: Un-share a BrandConfig (Theme)
        :rtype: requests.Response (with SharedBrandConfig data)

    """

    path = '/v1/shared_brand_configs/{id}'
    url = request_ctx.base_api_url + path.format(id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response


