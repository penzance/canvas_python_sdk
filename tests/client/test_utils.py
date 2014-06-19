import unittest
from mock import patch
from canvas_sdk.client import utils

AUTH_TOKEN = 'test-token'
DEFAULT_REQUEST_PARAMS = {
    'timeout': 30,
    'stream': False,
    'proxies': {'http': True},
    'cookies': {'foo': 'bar'},
    'verify': True,  # True/False
    'cert': 'Test Cert',  # String or tuple
}


class TestUtils(unittest.TestCase):
    longMessage = True

    @patch.dict('canvas_sdk.client.utils.config.OPTIONAL_REQUEST_PARAMS', DEFAULT_REQUEST_PARAMS)
    @patch('canvas_sdk.client.utils.config.OAUTH2_TOKEN', AUTH_TOKEN)
    @patch('canvas_sdk.client.utils.get_default_headers')
    @patch('canvas_sdk.client.utils.OAuth2Bearer')
    def test_set_default_request_params_for_kwargs_with_default_auth(self, oauth2_bearer_mock, get_default_headers_mock):
        utils.set_default_request_params_for_kwargs()
        oauth2_bearer_mock.assert_called_once_with(AUTH_TOKEN)

    @patch.dict('canvas_sdk.client.utils.config.OPTIONAL_REQUEST_PARAMS', DEFAULT_REQUEST_PARAMS)
    @patch('canvas_sdk.client.utils.config.OAUTH2_TOKEN', AUTH_TOKEN)
    @patch('canvas_sdk.client.utils.get_default_headers')
    @patch('canvas_sdk.client.utils.OAuth2Bearer')
    def test_set_default_request_params_for_kwargs_with_default_headers(self, oauth2_bearer_mock, get_default_headers_mock):
        utils.set_default_request_params_for_kwargs()
        get_default_headers_mock.assert_called_once_with()

    @patch.dict('canvas_sdk.client.utils.config.OPTIONAL_REQUEST_PARAMS', DEFAULT_REQUEST_PARAMS)
    @patch('canvas_sdk.client.utils.config.OAUTH2_TOKEN', AUTH_TOKEN)
    @patch('canvas_sdk.client.utils.get_default_headers')
    @patch('canvas_sdk.client.utils.OAuth2Bearer')
    def test_set_default_request_params_for_kwargs_sets_default_values_with_no_args(self, oauth2_bearer_mock, get_default_headers_mock):
        response = utils.set_default_request_params_for_kwargs()
        self.assertEqual(response['headers'], get_default_headers_mock.return_value, "Default header should be set to get_default_heders()")
        self.assertEqual(response['auth'], oauth2_bearer_mock.return_value, "Default auth should be set to OAuth2Bearer class")
        for key, value in DEFAULT_REQUEST_PARAMS.iteritems():
            self.assertEqual(response[key], value, "Default %s should be set to %s")

    @patch.dict('canvas_sdk.client.utils.config.OPTIONAL_REQUEST_PARAMS', DEFAULT_REQUEST_PARAMS)
    @patch('canvas_sdk.client.utils.config.OAUTH2_TOKEN', AUTH_TOKEN)
    @patch('canvas_sdk.client.utils.get_default_headers')
    @patch('canvas_sdk.client.utils.OAuth2Bearer')
    def test_set_default_request_params_for_kwargs_overrides_defaults_for_none(self, oauth2_bearer_mock, get_default_headers_mock):
        """
        Test that if a caller explicitly sets a request parameter value to None, it will be used in place of a default value
        """
        none_kwargs = {'timeout': None, 'stream': None, 'proxies': None, 'cookies': None, 'verify': None, 'cert': None, 'auth': None, 'headers': None}
        response = utils.set_default_request_params_for_kwargs(none_kwargs)
        for key in none_kwargs:
            self.assertEqual(response[key], None, "User should be able to override %s as None when explicitly setting to None")

    @patch.dict('canvas_sdk.client.utils.config.OPTIONAL_REQUEST_PARAMS', DEFAULT_REQUEST_PARAMS)
    @patch('canvas_sdk.client.utils.get_default_headers')
    @patch('canvas_sdk.client.utils.OAuth2Bearer')
    def test_set_default_request_params_for_kwargs_override_defaults(self, oauth2_bearer_mock, get_default_headers_mock):
        """
        Test that if a caller explicitly sets a request parameter value, it will be used in place of a default value
        """
        test_kwargs = {'timeout': 120, 'stream': True, 'proxies': {'my': 'proxy'}, 'cookies': {'my': 'cookies'}, 'verify': False, 'cert': 'MyCert', 'auth': ('basic', 'auth'), 'headers': {'Accept': 'text/json'}}
        response = utils.set_default_request_params_for_kwargs(test_kwargs)
        for key, value in test_kwargs.iteritems():
            self.assertEqual(response[key], value, "Response dict value for %s should be set to %s")

    def test_get_default_headers_contains_accept(self):
        """
        Test that default headers dict contains an Accept.
        """
        headers = utils.get_default_headers()
        self.assertTrue('Accept' in headers, "Default header should contain an 'Accept' header")
