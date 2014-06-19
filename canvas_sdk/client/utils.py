from canvas_sdk import config
from .auth import OAuth2Bearer


def get_default_headers():
    """
    These are headers that are sent with every API request and include authorization.  The
    headers themselves are not exposed in config since users can pass their own headers in
    to the call methods below, but be careful of overriding these headers since the API
    calls may not work if these are modified.
    """
    default_headers = {
        'Accept': 'text/json'
    }
    return default_headers


def set_default_request_params_for_kwargs(request_kwargs={}):
    request_kwargs.setdefault('headers', get_default_headers())
    request_kwargs.setdefault('auth', OAuth2Bearer(config.OAUTH2_TOKEN))
    request_kwargs.setdefault('proxies', config.OPTIONAL_REQUEST_PARAMS.get('proxies', None))
    request_kwargs.setdefault('timeout', config.OPTIONAL_REQUEST_PARAMS.get('timeout', None))
    request_kwargs.setdefault('cookies', config.OPTIONAL_REQUEST_PARAMS.get('cookies', None))
    request_kwargs.setdefault('stream', config.OPTIONAL_REQUEST_PARAMS.get('stream', None))
    request_kwargs.setdefault('verify', config.OPTIONAL_REQUEST_PARAMS.get('verify', None))
    request_kwargs.setdefault('cert', config.OPTIONAL_REQUEST_PARAMS.get('cert', None))
    return request_kwargs
