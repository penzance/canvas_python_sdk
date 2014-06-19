import requests
from requests.adapters import HTTPAdapter
import time
from canvas_sdk import config

MAX_RETRIES = config.MAX_RETRIES
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
        http_adapter = HTTPAdapter(max_retries=MAX_RETRIES)
        _session.mount('https://', http_adapter)
        _session.mount('http://', http_adapter)
        _session_create_time = now

    return _session
