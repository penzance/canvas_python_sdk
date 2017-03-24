from canvas_sdk import client, utils

"""
This is required because the swagger documentation for list_users_in_account
does not currently contain information about the include[] parameter.
Documentation that needs to be updated:
https://github.com/instructure/canvas-lms/blob/release/2017-04-01.07/app/controllers/users_controller.rb#L368
Based on the following param:
https://github.com/instructure/canvas-lms/blob/release/2017-04-01.07/app/controllers/users_controller.rb#L416
"""
def list_users_in_account(request_ctx, account_id, search_term=None,
                          include=None, per_page=None, **request_kwargs):
    """
    Retrieve the list of users associated with this account.

     @example_request
       curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
          -X GET \
          -H 'Authorization: Bearer <token>'

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param search_term: (optional) The partial name or full ID of the users to match and return in the
results list. Must be at least 3 characters.

Note that the API will prefer matching on canonical user ID if the ID has
a numeric form. It will only search against other fields if non-numeric
in form, or if the numeric value doesn't yield any matches. Queries by
administrative users will search on SIS ID, name, or email address; non-
administrative queries will only be compared against name.
        :type search_term: string or None
        :param include: (optional) One of (avatar_url, email, last_login, time_zone)
        :type include: array or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: List users in account
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    include_types = ('avatar_url', 'email', 'last_login', 'time_zone')
    utils.validate_attr_is_acceptable(include, include_types)
    path = '/v1/accounts/{account_id}/users'
    payload = {
        'include[]': include,
        'search_term': search_term,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response
