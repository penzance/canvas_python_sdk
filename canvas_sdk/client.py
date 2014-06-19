import requests
from requests.adapters import HTTPAdapter
import config
import time

MAX_RETRIES = config.REQUEST.get('MAX_RETRIES')
TIMEOUT_SECS = config.REQUEST.get('TIMEOUT_SECS')
# Global variables used to control session connection to API
_session = None
_session_create_time = 0


def get_canvas_session():
    """
    Use global session and creation time variables to keep track of existing
    session.  Return a new session if one does not exist or has expired, otherwise
    return the existing session.
    """
    global _session, _session_create_time

    now = int(time.time())
    session_age = now - _session_create_time
    # "Expire" old sessions by assigning a new session object - according to
    # requests library documentation we shouldn't have to explicitly close a
    # session.
    if _session is None or session_age > config.SESSION_EXPIRATION_TIME_SECS:
        _session = requests.Session()
        _session.stream = False
        _session.headers.update(get_default_headers())
        http_adapter = HTTPAdapter(max_retries=MAX_RETRIES)
        _session.mount('https://', http_adapter)
        _session.mount('http://', http_adapter)
        _session_create_time = now

    return _session


def get_auth_token():
    """ Return the authentication token from config and raise an exception if None """
    token = config.AUTH_TOKEN
    if token is None:
        raise NotImplementedError("Authentication token must be set to a value other than None in config module.")
    return token


def get_default_headers():
    """
    These are headers that are sent with every API request and include authorization.  The
    headers themselves are not exposed in config since users can pass their own headers in
    to the call methods below, but be careful of overriding these headers since the API
    calls may not work if these are modified.
    """
    default_headers = {
        'Authorization': 'Bearer %s' % get_auth_token(),
        'Accept': 'text/json'
    }
    return default_headers
