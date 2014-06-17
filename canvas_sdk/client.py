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
    Return a new session if one does not exist or has expired return a new
    session, otherwise return the exisitng session.
    """
    global _session, _session_create_time

    now = int(time.time())
    session_age = now - _session_create_time
    # "Expire" old sessions by setting to None, and let garbage
    # collector handle session closing
    if session_age > config.SESSION_EXPIRATION_TIME_SECS:
        _session = None

    if _session is None:
        _session = requests.Session()
        _session.stream = False
        _session.headers.update(get_default_headers())
        http_adapter = HTTPAdapter(max_retries=MAX_RETRIES)
        _session.mount('https://', http_adapter)
        _session.mount('http://', http_adapter)
        _session_create_time = int(time.time())

    return _session


def get_default_headers():
    """
    These are headers that are sent with every API request and include authorization.  The
    headers themselves are not exposed in config since users can pass their own headers in
    to the call methods below, but be careful of overriding these headers since the API
    calls may not work with modifications.
    """
    default_headers = {
        'Authorization ': 'Bearer %s' % config.AUTH_TOKEN,
        'Accept': 'text/json'
    }
    return default_headers
