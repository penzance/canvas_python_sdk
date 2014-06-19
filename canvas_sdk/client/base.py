import requests
from requests.exceptions import HTTPError
from canvas_sdk import config
from .session import get_canvas_session
from .utils import set_default_request_params_for_kwargs

MAX_RETRIES = config.MAX_RETRIES


def get(url, payload=None, **optional_request_params):
    """
    Shortcut for making a GET call to the API
    """
    return call("GET", url, params=payload, **optional_request_params)


def put(url, payload=None, **optional_request_params):
    """
    Shortcut for making a PUT call to the API
    """
    return call("PUT", url, data=payload, **optional_request_params)


def post(url, payload=None, **optional_request_params):
    """
    Shortcut for making a POST call to the API
    """
    return call("POST", url, data=payload, **optional_request_params)


def delete(url, payload=None, **optional_request_params):
    """
    Shortcut for making a DELETE call to the API
    """
    return call("DELETE", url, data=payload, **optional_request_params)


def call(action, url, **kwarg_request_params):
    """This method servers as a pass-through to the requests library request functionality, but provides some configurable default
    values.  Constructs and sends a :class:`requests.Request <Request>`.
    Returns :class:`requests.Response <Response>` object.

    :param action: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of 'name': file-like-objects (or {'name': ('filename', fileobj)}) for multipart encoding upload.
    :param auth: (optional) Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) Float describing the timeout of the request in seconds.
    :param allow_redirects: (optional) Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) if ``True``, the SSL cert will be verified. A CA_BUNDLE path can also be provided.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

    Usage::

      >>> from canvas_sdk import base
      >>> req = base.call('GET', 'http://httpbin.org/get')
      <Response [200]>
    """
    set_default_request_params_for_kwargs(kwarg_request_params)
    canvas_session = get_canvas_session()
    # try the request until max_retries is reached
    for retry in range(0, MAX_RETRIES):
        try:
            # build and send the request
            response = canvas_session.request(action, url, **kwarg_request_params)

            # raise an http exception if one occured
            response.raise_for_status()

            break

        except HTTPError as http_error:
            # Need to check its an 404, 503, 500, 403 etc.
            http_codes = requests.codes
            http_error_codes = [
                http_codes['conflict'],  # 409
                http_codes['internal_server_error'],  # 500
                http_codes['bad_gateway'],  # 502
                http_codes['service_unavailable'],  # 503
                http_codes['gateway_timeout']  # 504
            ]
            status_code = http_error.response.status_code
            if status_code in http_error_codes:
                # continue in a retry loop until max_retries
                if retry < MAX_RETRIES:
                    continue
            raise

    # Otherwise, return raw response
    return response
