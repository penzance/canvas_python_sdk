import unittest
from unittest import mock
from mock import patch
from canvas_sdk.client import RequestContext


class TestRequestContext(unittest.TestCase):
    longMessage = True

    def setUp(self):
        patcher = patch.object(RequestContext, 'get_default_headers')
        self.auth_token = 'my-auth-token'
        self.base_api_url = 'http://fake/canvas/instance/api'
        self.addCleanup(patcher.stop)
        self.mock_default_headers = patcher.start()

    def test_get_default_headers_contains_accept_text_json(self):
        """
        Test that the result of get_default_headers contains an accept header with text/json.
        """
        self.doCleanups()  # First, stop the patch so we can test the result of the actual call
        result = RequestContext.get_default_headers()
        self.assertTrue('Accept' in result, "Default headers should contain an Accept key")
        self.assertEqual('text/json', result.get('Accept', None),
                         "Default header should indicate that request accepts a text/json header")

    def test_initialize_calls_get_default_headers(self):
        """
        Test that get_default_headers is called as part of initializing a RequestContext
        """
        RequestContext(self.auth_token, self.base_api_url)
        self.mock_default_headers.assert_called_once_with()

    def test_initialize_raises_attribute_exception_when_using_malformed_api_url(self):
        """
        Test that an AttributeError is raised in case the base_api url being passed is a malformed http
        or https url.
        """
        bogus_urls = (
            "http//canvas.com/api",
            "ftp://canavas.com/api",  # Valid url, but not http or https
            "https//canavas.com",
            "canvas.api.com/api"
        )
        for bogus_url in bogus_urls:
            with self.assertRaises(AttributeError):
                RequestContext(self.auth_token, bogus_url)

    def test_initialize_with_defaults_sets_auth_token_and_base_url(self):
        """
        Test that required parameters auth_token and base_api_url are set on creation
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(self.auth_token, context.auth_token,
                         "RequestContext should have an auth_token instance attribute")
        self.assertEqual(self.base_api_url, context.base_api_url,
                         "RequestContext should have a base_api_url instance attribute")

    def test_initialize_max_retries_defaults_to_zero(self):
        """
        Test that if max_retries is not passed in, the value defaults to zero
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(0, context.max_retries, "max_retries should default to zero on creation")

    def test_initialize_headers_defaults_to_get_default_headers(self):
        """
        Test that if headers is not passed in, the value defaults to result of get_default_headers
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(self.mock_default_headers.return_value,
                         context.headers, "max_retries should default to zero on creation")

    def test_initialize_cookies_defaults_to_none(self):
        """
        Test that if cookies is not passed in, the instance attribute defaults to None
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(None, context.cookies, "cookies should default to None on creation")

    def test_initialize_timeout_defaults_to_none(self):
        """
        Test that if timeout is not passed in, the instance attribute defaults to None
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(None, context.timeout, "timeout should default to None on creation")

    def test_initialize_cert_defaults_to_none(self):
        """
        Test that if cert is not passed in, the instance attribute defaults to None
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(None, context.cert, "cert should default to None on creation")

    def test_initialize_proxies_defaults_to_none(self):
        """
        Test that if proxies is not passed in, the instance attribute defaults to None
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(None, context.proxies, "proxies should default to None on creation")

    def test_initialize_verify_defaults_to_true(self):
        """
        Test that if verify is not passed in, the instance attribute defaults to True
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(True, context.verify, "verify should default to True on creation")

    def test_initialize_merges_headers(self):
        """
        Test that if headers are passed in, they are merged into the default headers
        """
        default_headers = {'Accept': 'text/json', 'Custom': 'foo'}
        self.mock_default_headers.return_value = default_headers
        context = RequestContext(
            self.auth_token, self.base_api_url, headers={'Custom': 'bar', 'Content': 'xml'})
        self.assertEqual({'Accept': 'text/json', 'Custom': 'bar', 'Content': 'xml'},
                         context.headers, "headers should be merged with default headers")

    def test_initialize_per_page_defaults_to_none(self):
        """
        Test that if cert is not passed in, the instance attribute defaults to None
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        self.assertEqual(None, context.per_page, "per_page should default to None on creation")

    def test_initialize_from_dictionary(self):
        """
        Test that RequestContext can be initialized from a dictionary of settings
        """
        dict_settings = {
            'auth_token': self.auth_token,
            'base_api_url': self.base_api_url,
            'max_retries': 5,
            'per_page': 20,
            'timeout': 60,
            'headers': {'foo': 'bar'},
            'cookies': {'oreo': 'cookie'},
            'proxies': {'my': 'proxy'},
            'verify': False,
            'cert': 'my-cert'
        }
        self.mock_default_headers.return_value = {}  # Need to merge into a dictionary
        context = RequestContext(**dict_settings)
        for setting_key in dict_settings:
            self.assertEqual(dict_settings.get(setting_key), getattr(context, setting_key),
                             "Attribute %s should match value passed in through dictionary" % setting_key)

    @patch('canvas_sdk.client.request_context.OAuth2Bearer')
    def test_auth_property_returns_custom_authorization_callable(self, mock_oauth_bearer):
        """
        Test that auth property of RequestContext returns a new instance of OAuth2Bearer
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        result = context.auth
        mock_oauth_bearer.assert_called_once_with(self.auth_token)
        self.assertEqual(mock_oauth_bearer.return_value, result,
                         "Auth property of RequestContext should return an instance of OAuth2Bearer")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_occurs_by_default_when_accessing_property(self, mock_auth, mock_requests_session):
        """
        Test that accessing session property when no session has been set (default) creates a new requests.Session object
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        context.session
        mock_requests_session.assert_called_once_with()

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_auth_to_instance_property(self, mock_auth, mock_requests_session):
        """
        Test that Session object has an "auth" property that is the value of the context object's auth property.
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        result = context.session
        self.assertEqual(result.auth, mock_auth.return_value,
                         "Session attribute should have auth set to context auth")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_updates_headers_with_instance_headers(self, mock_auth, mock_requests_session):
        """
        Test that Session object headers are updated with context headers, when context headers are present (they are
        by default set to the value of get_default_headers).
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        context.session
        mock_requests_session.return_value.headers.update.assert_called_once_with(context.headers)

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_updates_headers_with_empty_dict_when_no_instance_headers(self, mock_auth, mock_requests_session):
        """
        Test that Session object headers are updated with an empty dictionary if context headers are explicitly set to None.
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        context.headers = None
        context.session
        mock_requests_session.return_value.headers.update.assert_called_once_with({})

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_has_stream_set_to_false(self, mock_auth, mock_requests_session):
        """
        Test that Session object is created with streaming disabled.
        """
        context = RequestContext(self.auth_token, self.base_api_url)
        result = context.session
        self.assertEqual(
            False, result.stream, "Streaming should be disabled for newly created sessions")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_verify_to_instance_value(self, mock_auth, mock_requests_session):
        """
        Test that Session object is created with context verify value.
        """
        context = RequestContext(self.auth_token, self.base_api_url, verify=False)
        result = context.session
        self.assertEqual(
            False, result.verify, "Verify attribute on session should be equivalent to attribute passed in to context")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_cert_to_instance_value(self, mock_auth, mock_requests_session):
        """
        Test that Session object is created with context cert value.
        """
        context = RequestContext(self.auth_token, self.base_api_url, cert='my-cert')
        result = context.session
        self.assertEqual(
            'my-cert', result.cert, "Cert attribute on session should be equivalent to attribute passed in to context")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_timeout_to_instance_value(self, mock_auth, mock_requests_session):
        """
        Test that Session object is created with context timeout value.
        """
        context = RequestContext(self.auth_token, self.base_api_url, timeout=60)
        result = context.session
        self.assertEqual(
            60, result.timeout, "Timeout attribute on session should be equivalent to attribute passed in to context")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_does_not_explicitly_set_proxies_if_none(self, mock_auth, mock_requests_session):
        """
        Test that proxies attribute that Session object may be initialized with is not overriden by an empty/None context property
        """
        session_proxy = {'proxy': 'session'}
        mock_requests_session.return_value.proxies = session_proxy
        context = RequestContext(self.auth_token, self.base_api_url)
        context.proxies = None
        result = context.session
        self.assertEqual(session_proxy, result.proxies,
                         "Proxies attribute should not be overriden on session when no proxies set on context")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_proxies_with_context_value(self, mock_auth, mock_requests_session):
        """
        Test that proxies attribute that Session object may be initialized with is overriden by corresponding context property
        """
        context_proxy = {'proxy': 'session'}
        context = RequestContext(self.auth_token, self.base_api_url, proxies=context_proxy)
        result = context.session
        self.assertEqual(context_proxy, result.proxies,
                         "Proxies attribute should be set to context value")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_does_not_explicitly_set_cookies_if_none(self, mock_auth, mock_requests_session):
        """
        Test that proxies attribute that Session object may be initialized with is not overriden by an empty/None context property
        """
        session_cookies = {'cookies': 'session'}
        mock_requests_session.return_value.cookies = session_cookies
        context = RequestContext(self.auth_token, self.base_api_url)
        context.cookies = None
        result = context.session
        self.assertEqual(session_cookies, result.cookies,
                         "Cookies attribute should not be overriden on session when no cookies set on context")

    @patch('canvas_sdk.client.request_context.requests.Session')
    @patch.object(RequestContext, 'auth', new_callable=mock.PropertyMock)
    def test_session_creation_sets_cookies_with_context_value(self, mock_auth, mock_requests_session):
        """
        Test that proxies attribute that Session object may be initialized with is overriden by corresponding context property
        """
        context_cookies = {'cookies': 'context'}
        context = RequestContext(self.auth_token, self.base_api_url, cookies=context_cookies)
        result = context.session
        self.assertEqual(context_cookies, result.cookies,
                         "Cookies attribute should be set to context value")

    def test_session_returns_stored_value_after_initial_creation(self):
        """
        Test that a previously created session is stored/returned when session property is called
        """
        previous_session = mock.Mock('previous-session')
        context = RequestContext(self.auth_token, self.base_api_url)
        context.session = previous_session  # Use setter to establish a stored value
        self.assertEqual(previous_session, context.session,
                         "Prior stored session should be returned by a subsequent call to session property")

    def test_expire_session_clears_stored_session(self):
        """
        Test that a previously created session is cleared out when calling expire_session
        """
        previous_session = mock.Mock('previous-session')
        context = RequestContext(self.auth_token, self.base_api_url)
        context.session = previous_session  # Use setter to establish a stored value
        context.expire_session()
        self.assertNotEqual(previous_session, context.session,
                            "Prior stored session should have been cleared out after call to expire_session")
