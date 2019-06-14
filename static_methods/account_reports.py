def start_report(request_ctx, account_id, report, parameters, **request_kwargs):
    """
    Generates a report instance for the account.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param report: (required) ID
        :type report: string
        :param parameters: (required) The parameters will vary for each report
        :type parameters: dict
        :return: Start a Report
        :rtype: requests.Response (with Report data)

    """

    path = '/v1/accounts/{account_id}/reports/{report}'

    # if the parameters dict has keys like 'enrollments', 'xlist', 'include_deleted'
    # we need to translate them to be like 'parameters[enrollments]'
    ppat = re.compile('parameters\[.+\]')
    fix_key = lambda k_v: (k_v[0] if ppat.match(str(k_v[0])) else 'parameters[{}]'.format(k_v[0]), k_v[1])
    payload = list(map(fix_key, list(parameters.items())))
    url = request_ctx.base_api_url + path.format(account_id=account_id, report=report)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def status_of_report(request_ctx, account_id, report, id, **request_kwargs):
    """
    Returns the status of a report.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param report: (required) ID
        :type report: string
        :param id: (required) ID
        :type id: string
        :return: Status of a Report
        :rtype: requests.Response (with Report data)

    """

    path = '/v1/accounts/{account_id}/reports/{report}/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, report=report, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response
