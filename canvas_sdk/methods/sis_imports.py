from canvas_sdk import client, utils


def get_sis_import_list(request_ctx, account_id, created_since=None, per_page=None, **request_kwargs):
    """
    Returns the list of SIS imports for an account
    
    Example:
      curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports' \
        -H "Authorization: Bearer <token>"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param created_since: (optional) If set, only shows imports created after the specified date (use ISO8601 format)
        :type created_since: DateTime or None
        :param per_page: (optional) Set how many results canvas should return, defaults to config.LIMIT_PER_PAGE
        :type per_page: integer or None
        :return: Get SIS import list
        :rtype: requests.Response (with array data)

    """

    if per_page is None:
        per_page = request_ctx.per_page
    path = '/v1/accounts/{account_id}/sis_imports'
    payload = {
        'created_since': created_since,
        'per_page': per_page,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.get(request_ctx, url, payload=payload, **request_kwargs)

    return response


def import_sis_data(request_ctx, account_id, import_type=None, attachment=None, extension=None, batch_mode=None, batch_mode_term_id=None, override_sis_stickiness=None, add_sis_stickiness=None, clear_sis_stickiness=None, diffing_data_set_identifier=None, diffing_remaster_data_set=None, **request_kwargs):
    """
    Import SIS data into Canvas. Must be on a root account with SIS imports
    enabled.
    
    For more information on the format that's expected here, please see the
    "SIS CSV" section in the API docs.

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param import_type: (optional) Choose the data format for reading SIS data. With a standard Canvas
install, this option can only be 'instructure_csv', and if unprovided,
will be assumed to be so. Can be part of the query string.
        :type import_type: string or None
        :param attachment: (optional) There are two ways to post SIS import data - either via a
multipart/form-data form-field-style attachment, or via a non-multipart
raw post request.

'attachment' is required for multipart/form-data style posts. Assumed to
be SIS data from a file upload form field named 'attachment'.

Examples:
  curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
      'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'

If you decide to do a raw post, you can skip the 'attachment' argument,
but you will then be required to provide a suitable Content-Type header.
You are encouraged to also provide the 'extension' argument.

Examples:
  curl -H 'Content-Type: application/octet-stream' --data-binary @<filename>.zip \
      -H "Authorization: Bearer <token>" \
      'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&extension=zip'

  curl -H 'Content-Type: application/zip' --data-binary @<filename>.zip \
      -H "Authorization: Bearer <token>" \
      'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'

  curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
      -H "Authorization: Bearer <token>" \
      'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv'

  curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
      -H "Authorization: Bearer <token>" \
      'https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&batch_mode=1&batch_mode_term_id=15'
        :type attachment: string or None
        :param extension: (optional) Recommended for raw post request style imports. This field will be used to
distinguish between zip, xml, csv, and other file format extensions that
would usually be provided with the filename in the multipart post request
scenario. If not provided, this value will be inferred from the
Content-Type, falling back to zip-file format if all else fails.
        :type extension: string or None
        :param batch_mode: (optional) If set, this SIS import will be run in batch mode, deleting any data
previously imported via SIS that is not present in this latest import.
See the SIS CSV Format page for details.
        :type batch_mode: boolean or None
        :param batch_mode_term_id: (optional) Limit deletions to only this term. Required if batch mode is enabled.
        :type batch_mode_term_id: string or None
        :param override_sis_stickiness: (optional) Many fields on records in Canvas can be marked "sticky," which means that
when something changes in the UI apart from the SIS, that field gets
"stuck." In this way, by default, SIS imports do not override UI changes.
If this field is present, however, it will tell the SIS import to ignore
"stickiness" and override all fields.
        :type override_sis_stickiness: boolean or None
        :param add_sis_stickiness: (optional) This option, if present, will process all changes as if they were UI
changes. This means that "stickiness" will be added to changed fields.
This option is only processed if 'override_sis_stickiness' is also provided.
        :type add_sis_stickiness: boolean or None
        :param clear_sis_stickiness: (optional) This option, if present, will clear "stickiness" from all fields touched
by this import. Requires that 'override_sis_stickiness' is also provided.
If 'add_sis_stickiness' is also provided, 'clear_sis_stickiness' will
overrule the behavior of 'add_sis_stickiness'
        :type clear_sis_stickiness: boolean or None
        :param diffing_data_set_identifier: (optional) If set on a CSV import, Canvas will attempt to optimize the SIS import by
comparing this set of CSVs to the previous set that has the same data set
identifier, and only appliying the difference between the two. See the
SIS CSV Format documentation for more details.
        :type diffing_data_set_identifier: string or None
        :param diffing_remaster_data_set: (optional) If true, and diffing_data_set_identifier is sent, this SIS import will be
part of the data set, but diffing will not be performed. See the SIS CSV
Format documentation for details.
        :type diffing_remaster_data_set: boolean or None
        :return: Import SIS data
        :rtype: requests.Response (with SisImport data)

    """

    path = '/v1/accounts/{account_id}/sis_imports'
    payload = {
        'import_type': import_type,
        'attachment': attachment,
        'extension': extension,
        'batch_mode': batch_mode,
        'batch_mode_term_id': batch_mode_term_id,
        'override_sis_stickiness': override_sis_stickiness,
        'add_sis_stickiness': add_sis_stickiness,
        'clear_sis_stickiness': clear_sis_stickiness,
        'diffing_data_set_identifier': diffing_data_set_identifier,
        'diffing_remaster_data_set': diffing_remaster_data_set,
    }
    url = request_ctx.base_api_url + path.format(account_id=account_id)
    response = client.post(request_ctx, url, payload=payload, **request_kwargs)

    return response


def get_sis_import_status(request_ctx, account_id, id, **request_kwargs):
    """
    Get the status of an already created SIS import.
    
      Examples:
        curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id>' \
            -H "Authorization: Bearer <token>"

        :param request_ctx: The request context
        :type request_ctx: :class:RequestContext
        :param account_id: (required) ID
        :type account_id: string
        :param id: (required) ID
        :type id: string
        :return: Get SIS import status
        :rtype: requests.Response (with SisImport data)

    """

    path = '/v1/accounts/{account_id}/sis_imports/{id}'
    url = request_ctx.base_api_url + path.format(account_id=account_id, id=id)
    response = client.get(request_ctx, url, **request_kwargs)

    return response


