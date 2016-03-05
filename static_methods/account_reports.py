
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
    fix_key = lambda (k, v): (k if ppat.match(str(k)) else 'parameters[{}]'.format(k), v)
    payload = map(fix_key, parameters.items())
    url = request_ctx.base_api_url + path.format(account_id=account_id, report=report)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response
    
