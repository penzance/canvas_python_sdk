# request_context.py
import requests
from .auth import OAuth2Bearer
from urlparse import urlparse


class RequestContext(object):

    """
    A class that holds the default configuration values used to make Canvas API requests.  The requests
    library is heavily leveraged in terms of the attributes that may be passed in.  Most of the attributes
    are used to construct a requests.Session instance that by default will be reused across requests
    made with a given :class:`RequestContext <RequestContext>`.  See below for a full list of parameters:

    :param str auth_token: OAuth2 token retrieved from a Canvas site
    :param str base_api_url: The api endpoint of the Canvas site in the form "http(s)://[canvas.site.com]/api"
    :param int max_retries: (optional) Number of times a request that generates a certain class of HTTP exception will be retried
        before being raised back to the caller.  See :py:mod:`client.base` for a list of those error types.
    :param dictionary headers: (optional) dictionary of headers to send for each request.  Will be merged with a default set of headers.
    :param cookies: (optional) Cookies to attach to each requests.
    :type cookies: dictionary or CookieJar
    :param float timeout: (optional) The timeout of the request in seconds.
    :param dictionary proxies: (optional) Mapping protocol to the URL of the proxy.
    :param verify: (optional) if ``True``, the SSL cert will be verified.  A CA_BUNDLE path can also be provided.
    :type verify: boolean or str
    :param cert: (optional) if String, path to ssl client cert file (.pem).  If Tuple, ('cert', 'key') pair.
    :type cert: str or Tuple
    """

    @classmethod
    def get_default_headers(cls):
        """
        These are headers that are sent with every API request.  Be careful of overriding these headers since the API
        calls may not work if these are modified.
        """
        default_headers = {
            'Accept': 'text/json'
        }
        return default_headers

    def __init__(self, auth_token, base_api_url, max_retries=0, headers=None, cookies=None, timeout=None, proxies=None, verify=True, cert=None):
        self._session = None
        self.auth_token = auth_token
        parsed_url = urlparse(base_api_url)
        if 'http' not in parsed_url.scheme:
            raise AttributeError(
                "'%s' was provided, but base_url should be in the format http(s)://path/to/canvas/instance/api." % base_api_url)
        self.base_api_url = base_api_url
        self.headers = self.get_default_headers()
        # Allow overriding of default values with values passed in by user
        if headers:
            self.headers.update(headers)
        self.cookies = cookies
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify
        self.cert = cert
        self.max_retries = max_retries

    @property
    def auth(self):
        """
        A custom OAuth2 authentication handler for the instance's auth_token
        """
        return OAuth2Bearer(self.auth_token)

    @property
    def session(self):
        """
        Get or set a requests.Session instance based on the session related values passed into the
        class.  The setter should only be used if you need fine-grained control over your session.
        You can refer to the requests library documentation for information on available options for
        the session object: http://docs.python-requests.org/en/latest/
        """
        if not self._session:
            self._session = requests.Session()
            # Streaming is disabled by default when creating a requests.Session
            # object, but let's be explicit here to prevent connections from staying
            # open indefinitely
            self._session.stream = False
            self._session.auth = self.auth
            self._session.headers.update(self.headers or {})
            self._session.timeout = self.timeout
            self._session.cert = self.cert
            self._session.verify = self.verify
            # We only need to set proxies and cookies if not None or empty since the
            # defaults are empty dicts
            if self.proxies:
                self._session.proxies = self.proxies
            if self.cookies:
                self._session.cookies = self.cookies
        return self._session

    @session.setter
    def session(self, sess):
        self._session = sess

    def expire_session(self):
        """
        To expire a session, it just needs to be set to None according to requests doc.
        """
        self.session = None
