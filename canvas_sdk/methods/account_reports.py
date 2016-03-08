from canvas_sdk import client, utils
import re


def list_available_reports(request_ctx, account_id, **request_kwargs):
    """
    Returns the list of reports for the current context.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :return: List Available Reports
        :rtype: requests.Response (with void data)

    """

    path = '/v1/accounts/{account_id}/reports'
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


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


def index_of_reports(request_ctx, account_id, report, per_page=None, **request_kwargs):
    """
    Shows all reports that have been run for the account of a specific type.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param report: (required) ID
        :type report: string
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Index of Reports
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/reports/{report}'
    payload = {
        'per_page' : per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id, report=report)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

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


def delete_report(request_ctx, account_id, report, id, **request_kwargs):
    """
    Deletes a generated report instance.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param report: (required) ID
        :type report: string
        :param id: (required) ID
        :type id: string
        :return: Delete a Report
        :rtype: requests.Response (with Report data)

    """

    path = '/v1/accounts/{account_id}/reports/{report}/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, report=report, id=id)
    response = client.delete(request_ctx, url, **request_kwargs)

    return response
