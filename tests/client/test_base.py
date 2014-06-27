import unittest
import mock
from mock import patch
from canvas_sdk import client
from canvas_sdk.client import base
from requests.exceptions import HTTPError


class TestBase(unittest.TestCase):
    longMessage = True
    # Expected set of optional request parameters with default values
    OPTIONAL_REQUEST_ARGS = {
        'params': None,
        'data': None,
        'files': None,
        'headers': None,
        'cookies': None,
        'timeout': None,
        'proxies': None,
        'verify': None,
        'cert': None,
        'allow_redirects': True
    }

    def setUp(self):
        self.base_api_url = "https://path/to/canvas/api"
        self.relative_url = "/fake/path/to/method"
        self.absolute_url = self.base_api_url + self.relative_url
        self.session = mock.MagicMock(name='canvas-session')
        self.req_ctx = mock.MagicMock(name='request-context')
        self.req_ctx.base_api_url = self.base_api_url
        self.req_ctx.session = self.session
        self.req_ctx.max_retries = 0
        self.payload = {'foo': 'bar'}
        self.request_kwargs = {'headers': {'my': 'header'}, 'timeout': 30}

    def make_retry_call_with_error_code(self, http_error_code, max_retries=None):
        """
        Makes a call that will raise an http error in order to potentially trigger
        the request being retried up to "max_retries" times.
        """
        self.session.request.return_value.raise_for_status.side_effect = HTTPError(
            response=mock.MagicMock(status_code=http_error_code))
        with self.assertRaises(HTTPError):
            base.call("GET", self.relative_url, self.req_ctx, max_retries=max_retries)

    @patch('canvas_sdk.client.base.call')
    def test_get_returns_call(self, call_mock):
        """
        Test that the call to get method returns the result of 'call'
        """
        result = client.get(self.req_ctx, self.relative_url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'get' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_get_makes_call_with_action_url_and_context(self, call_mock):
        """
        Test that the call to get method sends expected action, url, and request context
        """
        client.get(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with("GET", self.relative_url, self.req_ctx, params=mock.ANY)

    @patch('canvas_sdk.client.base.call')
    def test_get_makes_call_without_payload(self, call_mock):
        """
        Test that the call to get method without payload defaults params to None
        """
        client.get(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, params=None)

    @patch('canvas_sdk.client.base.call')
    def test_get_makes_call_with_payload(self, call_mock):
        """
        Test that the call to get method with a payload passes it into params
        """
        client.get(self.req_ctx, self.relative_url, self.payload)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, params=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_get_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to get method with no payload and request kwargs passes through
        properly
        """
        client.get(self.req_ctx, self.relative_url, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, params=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_get_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to get method with a payload and request kwargs passes through
        properly
        """
        client.get(self.req_ctx, self.relative_url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, params=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_put_returns_call(self, call_mock):
        """
        Test that the call to put method returns the result of 'call'
        """
        result = client.put(self.req_ctx, self.relative_url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'put' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_put_makes_call_with_action_url_and_context(self, call_mock):
        """
        Test that the call to get method sends expected action, url, and request context
        """
        client.put(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with("PUT", self.relative_url, self.req_ctx, data=mock.ANY)

    @patch('canvas_sdk.client.base.call')
    def test_put_without_payload(self, call_mock):
        """
        Test that the call to put method without payload defaults data to None
        """
        client.put(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_payload(self, call_mock):
        """
        Test that the call to put method with a payload passes it into data
        """
        client.put(self.req_ctx, self.relative_url, self.payload)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to put method with no payload and request kwargs passes through
        properly
        """
        client.put(self.req_ctx, self.relative_url, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to put method with payload and request kwargs passes through
        properly
        """
        client.put(self.req_ctx, self.relative_url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, data=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_post_returns_call(self, call_mock):
        """
        Test that the call to post method returns the result of 'call'
        """
        result = client.post(self.req_ctx, self.relative_url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'post' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_post_makes_call_with_action_url_and_context(self, call_mock):
        """
        Test that the call to get method sends expected action, url, and request context
        """
        client.post(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with("POST", self.relative_url, self.req_ctx, data=mock.ANY)

    @patch('canvas_sdk.client.base.call')
    def test_post_without_payload(self, call_mock):
        """
        Test that the call to post method without payload defaults data to None
        """
        client.post(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_payload(self, call_mock):
        """
        Test that the call to post method with a payload passes it into params
        """
        client.post(self.req_ctx, self.relative_url, self.payload)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to put method with no payload and request kwargs passes through
        properly
        """
        client.post(self.req_ctx, self.relative_url, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to put method with payload and request kwargs passes through
        properly
        """
        client.post(self.req_ctx, self.relative_url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, data=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_delete_returns_call(self, call_mock):
        """
        Test that the call to put method returns the result of 'call'
        """
        result = client.delete(self.req_ctx, self.relative_url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'delete' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_delete_makes_call_with_action_url_and_context(self, call_mock):
        """
        Test that the call to delete method sends expected action, url, and request context
        """
        client.delete(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with("DELETE", self.relative_url, self.req_ctx, data=mock.ANY)

    @patch('canvas_sdk.client.base.call')
    def test_delete_without_payload(self, call_mock):
        """
        Test that the call to delete method without payload defaults data to None
        """
        client.delete(self.req_ctx, self.relative_url)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_payload(self, call_mock):
        """
        Test that the call to delete method with a payload passes it into data
        """
        client.delete(self.req_ctx, self.relative_url, self.payload)
        call_mock.assert_called_once_with(mock.ANY, mock.ANY, mock.ANY, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to delete method with request kwargs and no payload passes through
        properly
        """
        client.delete(self.req_ctx, self.relative_url, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to delete method with payload and request kwargs passes through
        properly
        """
        client.delete(self.req_ctx, self.relative_url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
           mock.ANY, mock.ANY, mock.ANY, data=self.payload, **self.request_kwargs)

    def test_call_makes_request_with_required_parameters(self):
        """
        Test that the 'call' method makes a session request with required params and defaults for
        optional parameters.
        """
        base.call("GET", self.relative_url, self.req_ctx)
        self.session.request.assert_called_once_with(
            "GET", self.absolute_url, auth=None, **self.OPTIONAL_REQUEST_ARGS)

    @patch('canvas_sdk.client.base.OAuth2Bearer')
    def test_call_makes_request_with_auth_token(self, authentication_bearer_mock):
        """
        Test that the 'call' method uses custom authentication bearer callable when making request
        """
        auth_token = "my-oauth2-token"
        base.call("GET", self.relative_url, self.req_ctx, auth_token=auth_token)
        # Make sure custom auth class was set up properly
        authentication_bearer_mock.assert_called_once_with(auth_token)
        self.session.request.assert_called_once_with(
            "GET", self.absolute_url, auth=authentication_bearer_mock.return_value, **self.OPTIONAL_REQUEST_ARGS)

    def test_call_makes_request_with_optional_request_params(self):
        """
        Test that 'call' function makes session request with optional parameter set
        """
        custom_kwargs = self.OPTIONAL_REQUEST_ARGS.copy()
        custom_kwargs.update({
            'params': {'foo': 'param'},
            'data': {'foo': 'data'},
            'headers': {'bar': 'header'},
            'cookies': {'oreo': 'cookie'},
            'timeout': 60,
            'proxies': {'custom': 'proxy'},
            'verify': False,
            'cert': ('custom', 'cert'),
            'allow_redirects': False,
        })
        base.call("GET", self.relative_url, self.req_ctx, **custom_kwargs)
        self.session.request.assert_called_once_with(
            "GET", self.absolute_url, auth=None, **custom_kwargs)

    def test_call_raises_status_on_result(self):
        """
        Test that 'call' method makes call to raise_for_status on result object
        """
        result = base.call("GET", self.relative_url, self.req_ctx)
        result.raise_for_status.assert_called_once_with()

    def test_call_returns_value_of_session_request(self):
        """
        Test that 'call' method returns the result of session request
        """
        result = base.call("GET", self.relative_url, self.req_ctx)
        self.assertEqual(
            result, self.session.request.return_value, "Session request should be returned")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_http_error_immediately_when_status_code_not_in_retry_list(self):
        """
        Test that 'call' method raises an HTTPError without retrying if status code is not in list of retry codes
        """
        self.make_retry_call_with_error_code(404, max_retries=3)
        self.assertEqual(1, self.session.request.call_count,
                         "Request call should have been made only once")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_http_error_after_max_retries_when_status_code_in_retry_list(self):
        """
        Test that 'call' method retries an HTTPError with retriable status code up to max_retries times
        before re-raising
        """
        max_retries = 3
        self.make_retry_call_with_error_code(503, max_retries=max_retries)
        # Check that the request call was made max_retries + 1 times.  The +1 is to account for the
        # initial request call
        self.assertEqual(max_retries + 1, self.session.request.call_count,
                         "Call should have been made 'max_retries' + 1 times")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_makes_request_once_when_max_retries_explicitly_none(self):
        """
        Test that the 'call' method makes a single session request when max_retries was
        set to none on the request_context and passed in as none (parameter default).
        """
        self.req_ctx.max_retries = None
        self.make_retry_call_with_error_code(503)
        self.assertEqual(1, self.session.request.call_count,
                         "When max_retries is None, it should default to 0 and not trigger any retries")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_defaults_to_context_max_retries(self):
        """
        Test that the 'call' method retries session requests for retriable error codes
        based on the max_retries setting on the request_context object when no value
        is otherwise specified in the call.
        """
        max_retries = 5
        self.req_ctx.max_retries = max_retries
        self.make_retry_call_with_error_code(503)
        self.assertEqual(max_retries + 1, self.session.request.call_count,
                         "The number of retries should have defaulted back to value in request context")
