# config.py

# Canvas will generate this for a given user profile via their UI
OAUTH2_TOKEN = None

# The base api url for the Canvas instance you want to connect to.
# The url should look something like http://path/to/canvas/instance/api
BASE_API_URL = 'change me'

# Number of seconds before a request Session is considered stale
SESSION_EXPIRATION_TIME_SECS = 50

# For requests to Canvas API that return a list of data, this setting
# will serve as the default limit per page
LIMIT_PER_PAGE = 40

# This setting is used for both the number of retries that will be
# attempted before re-raising an HTTPError in cases where the error
# is a retriable type (see base.py for list), as well as the number of
# retries the HTTPAdapter will attempt for any request.
MAX_RETRIES = 3

# List of optional request params that a user may want to default to for
# each API request.  If you'd like to use a default value for a setting
# other than what the requests library provides, you can do so by importing
# the module and updating this dictionary like so:
# config.OPTIONAL_REQUEST_PARAMS['cert'] = 'my cert'
OPTIONAL_REQUEST_PARAMS = {
    'timeout': 30,
    'cookies': None,
    'stream': False,
    'allow_redirects': None,
    'proxies': None,
    'verify': None,  # True/False
    'cert': None,  # String or tuple
}
