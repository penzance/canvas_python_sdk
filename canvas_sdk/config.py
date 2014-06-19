# config.py

OAUTH2_TOKEN = None  # Expects a string value

BASE_API_URL = 'change me'

SESSION_EXPIRATION_TIME_SECS = 50

LIMIT_PER_PAGE = 40

MAX_RETRIES = 3

OPTIONAL_REQUEST_PARAMS = {
    'timeout': 30,
    'stream': False,
    'proxies': None,
    'verify': None,  # True/False
    'cert': None,  # String or tuple
}
