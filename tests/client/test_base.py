import unittest

import mock
from mock import patch
from requests.exceptions import HTTPError

from canvas_sdk import client
from canvas_sdk.client import base
from canvas_sdk.exceptions import (
    SDKException, CanvasAPIError, InvalidOAuthTokenError)


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
        self.url = self.base_api_url + "/fake/path/to/method"
        self.session = mock.MagicMock(name='canvas-session')
        self.req_ctx = mock.MagicMock(name='request-context')
        self.req_ctx.base_api_url = self.base_api_url
        self.req_ctx.session = self.session
        self.req_ctx.max_retries = 0
        self.payload = {'foo': 'bar'}
        self.request_kwargs = {'headers': {'my': 'header'}, 'timeout': 30}

    def make_retry_call_with_error_code(self, http_error_code, max_retries=None,
                                        error_json=None, response_headers=None):
        """
        Makes a call that will raise an http error in order to potentially
        trigger the request being retried up to "max_retries" times.  Otherwise,
        an SDKException is expected to be raised by the underlying call method.
        Return the exception in order to do any additional assertions.
        """
        self.session.request.return_value.raise_for_status.side_effect = HTTPError()
        self.session.request.return_value.status_code = http_error_code
        self.session.request.return_value.json.return_value = error_json or {}
        # Response headers
        self.session.request.return_value.headers = response_headers or {}

        with self.assertRaises(SDKException) as canvas_error:
            base.call("GET", self.url, self.req_ctx, max_retries=max_retries)

        return canvas_error.exception

    def test_merge_or_create_key_value_for_dictionary_no_value(self):
        """
        Test that call to merge helper method with a value of None doesn't make
        any changes to the dictionary that was passed in.
        """
        dictionary = {'foo': {'key1': 'val1'}}
        key = 'foo'
        value = None
        base.merge_or_create_key_value_for_dictionary(dictionary, key, value)
        self.assertEqual(
            dictionary, {'foo': {'key1': 'val1'}},
            "Dictionary should remain unchanged if no value was passed in to merge helper")

    def test_merge_or_create_key_value_for_dictionary_key_that_does_not_exist(self):
        """
        Test that call to merge helper method for a key that does not already
        exist in the dictionary that was passed in modifies the dictionary with
        the given key-value pair.
        """
        dictionary = {'foo': {'key1': 'val1'}}
        key = 'baz'
        value = {'new': 'value'}
        base.merge_or_create_key_value_for_dictionary(dictionary, key, value)
        self.assertEqual(
            dictionary, {'foo': {'key1': 'val1'}, key: value},
            "Dictionary should contain new key-value pair")

    def test_merge_or_create_key_value_for_dictionary_key_that_exists(self):
        """
        Test that call to merge helper method for a key that already exists in
        the dictionary will merge the new value in with the existing value for
        that key.
        """
        dictionary = {'foo': {'key1': 'val1', 'new': 'blue'}}
        key = 'foo'
        value = {'new': 'value'}
        base.merge_or_create_key_value_for_dictionary(dictionary, key, value)
        self.assertEqual(
            dictionary, {'foo': {'key1': 'val1', 'new': 'value'}},
            "The value should have been merged into the existing key on the dictionary")

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_returns_call(self, call_mock, merge_mock):
        """
        Test that the call to get method returns the result of 'call'
        """
        result = client.get(self.req_ctx, self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'get' should return result of 'call' method")

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_merges_with_params_key(self, call_mock, merge_mock):
        """
        Test that the call to get method calls merge helper with 'params' as
        dictionary key (second positional parameter)
        """
        client.get(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, 'params', mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_merges_with_request_kwargs(self, call_mock, merge_mock):
        """
        Test that the call to get method calls merge helper with request_kwargs
        dictionary as first positional parameter
        """
        client.get(self.req_ctx, self.url, **self.request_kwargs)
        merge_mock.assert_called_once_with(self.request_kwargs, mock.ANY, mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_merges_no_payload(self, call_mock, merge_mock):
        """
        Test that the call to get method without a payload calls merge helper
        and passes in None as the value parameter.
        """
        client.get(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, None)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_merges_with_payload(self, call_mock, merge_mock):
        """
        Test that the call to get method with a payload calls merge helper and
        passes the payload as the value parameter.
        """
        client.get(self.req_ctx, self.url, self.payload)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, self.payload)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_makes_call_with_action_url_and_context(self, call_mock, merge_mock):
        """
        Test that the call to get method sends expected action, url, and request
        context.
        """
        client.get(self.req_ctx, self.url)
        call_mock.assert_called_once_with("GET", self.url, self.req_ctx)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_get_with_request_kwargs_and_payload(self, call_mock, merge_mock):
        """
        Test that the call to get method with a payload and request kwargs passes
        through properly.
        """
        client.get(self.req_ctx, self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_put_returns_call(self, call_mock):
        """
        Test that the call to put method returns the result of 'call'
        """
        result = client.put(self.req_ctx, self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'put' should return result of 'call' method")

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_merges_with_data_key(self, call_mock, merge_mock):
        """
        Test that the call to put method calls merge helper with 'data' as
        dictionary key (second positional parameter)
        """
        client.put(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, 'data', mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_merges_with_request_kwargs(self, call_mock, merge_mock):
        """
        Test that the call to put method calls merge helper with request_kwargs
        dictionary as first positional parameter
        """
        client.put(self.req_ctx, self.url, **self.request_kwargs)
        merge_mock.assert_called_once_with(
            self.request_kwargs, mock.ANY, mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_merges_no_payload(self, call_mock, merge_mock):
        """
        Test that the call to put method without a payload calls merge helper
        and passes in None as the value parameter.
        """
        client.put(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, None)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_merges_with_payload(self, call_mock, merge_mock):
        """
        Test that the call to put method with a payload calls merge helper and
        passes in the payload as the value parameter.
        """
        client.put(self.req_ctx, self.url, self.payload)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, self.payload)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_makes_call_with_action_url_and_context(self, call_mock, merge_mock):
        """
        Test that the call to get method sends expected action, url, and request
        context.
        """
        client.put(self.req_ctx, self.url)
        call_mock.assert_called_once_with("PUT", self.url, self.req_ctx)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_put_with_request_kwargs_and_payload(self, call_mock, merge_mock):
        """
        Test that the call to put method with payload and request kwargs passes
        through properly.
        """
        client.put(self.req_ctx, self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, **self.request_kwargs)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_returns_call(self, call_mock, merge_mock):
        """
        Test that the call to post method returns the result of 'call'
        """
        result = client.post(self.req_ctx, self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'post' should return result of 'call' method")

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_merges_with_data_key(self, call_mock, merge_mock):
        """
        Test that the call to post method calls merge helper with 'data' as
        dictionary key (second positional parameter)
        """
        client.post(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, 'data', mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_merges_with_request_kwargs(self, call_mock, merge_mock):
        """
        Test that the call to post method calls merge helper with request_kwargs
        dictionary as first positional parameter
        """
        client.post(self.req_ctx, self.url, **self.request_kwargs)
        merge_mock.assert_called_once_with(self.request_kwargs, mock.ANY, mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_merges_no_payload(self, call_mock, merge_mock):
        """
        Test that the call to post method without a payload calls merge helper
        and passes in None as the value parameter.
        """
        client.post(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, None)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_merges_with_payload(self, call_mock, merge_mock):
        """
        Test that the call to put method with a payload calls merge helper and
        passes in the payload as the value parameter.
        """
        client.post(self.req_ctx, self.url, self.payload)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, self.payload)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_makes_call_with_action_url_and_context(self, call_mock, merge_mock):
        """
        Test that the call to get method sends expected action, url, and request
        context.
        """
        client.post(self.req_ctx, self.url)
        call_mock.assert_called_once_with("POST", self.url, self.req_ctx)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_post_with_request_kwargs_and_payload(self, call_mock, merge_mock):
        """
        Test that the call to post method with payload and request kwargs passes
        through properly.
        """
        client.post(self.req_ctx, self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, **self.request_kwargs)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_returns_call(self, call_mock, merge_mock):
        """
        Test that the call to put method returns the result of 'call'
        """
        result = client.delete(self.req_ctx, self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'delete' should return result of 'call' method")

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_merges_with_data_key(self, call_mock, merge_mock):
        """
        Test that the call to delete method calls merge helper with 'data' as
        dictionary key (second positional parameter)
        """
        client.delete(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, 'data', mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_merges_with_request_kwargs(self, call_mock, merge_mock):
        """
        Test that the call to delete method calls merge helper with
        request_kwargs dictionary as first positional parameter
        """
        client.delete(self.req_ctx, self.url, **self.request_kwargs)
        merge_mock.assert_called_once_with(
            self.request_kwargs, mock.ANY, mock.ANY)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_merges_no_payload(self, call_mock, merge_mock):
        """
        Test that the call to delete method without a payload calls merge helper
        and passes in None as the value parameter.
        """
        client.delete(self.req_ctx, self.url)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, None)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_merges_with_payload(self, call_mock, merge_mock):
        """
        Test that the call to delete method with a payload calls merge helper
        and passes in the payload as the value parameter.
        """
        client.delete(self.req_ctx, self.url, self.payload)
        merge_mock.assert_called_once_with(mock.ANY, mock.ANY, self.payload)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_makes_call_with_action_url_and_context(self, call_mock, merge_mock):
        """
        Test that the call to delete method sends expected action, url, and
        request context.
        """
        client.delete(self.req_ctx, self.url)
        call_mock.assert_called_once_with("DELETE", self.url, self.req_ctx)

    @patch('canvas_sdk.client.base.merge_or_create_key_value_for_dictionary')
    @patch('canvas_sdk.client.base.call')
    def test_delete_with_request_kwargs_and_payload(self, call_mock, merge_mock):
        """
        Test that the call to delete method with payload and request kwargs
        passes through properly.
        """
        client.delete(self.req_ctx, self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            mock.ANY, mock.ANY, mock.ANY, **self.request_kwargs)

    def test_call_makes_request_with_required_parameters(self):
        """
        Test that the 'call' method makes a session request with required params
        and defaults for optional parameters.
        """
        base.call("GET", self.url, self.req_ctx)
        self.session.request.assert_called_once_with(
            "GET", self.url, auth=None, **self.OPTIONAL_REQUEST_ARGS)

    @patch('canvas_sdk.client.base.OAuth2Bearer')
    def test_call_makes_request_with_auth_token(self, authentication_bearer_mock):
        """
        Test that the 'call' method uses custom authentication bearer callable
        when making request.
        """
        auth_token = "my-oauth2-token"
        base.call("GET", self.url, self.req_ctx, auth_token=auth_token)
        # Make sure custom auth class was set up properly
        authentication_bearer_mock.assert_called_once_with(auth_token)
        self.session.request.assert_called_once_with(
            "GET", self.url, auth=authentication_bearer_mock.return_value,
            **self.OPTIONAL_REQUEST_ARGS)

    def test_call_makes_request_with_optional_request_params(self):
        """
        Test that 'call' function makes session request with optional parameter
        set.
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
        base.call("GET", self.url, self.req_ctx, **custom_kwargs)
        self.session.request.assert_called_once_with(
            "GET", self.url, auth=None, **custom_kwargs)

    def test_call_raises_status_on_result(self):
        """
        Test that 'call' method makes call to raise_for_status on result object
        """
        result = base.call("GET", self.url, self.req_ctx)
        result.raise_for_status.assert_called_once_with()

    def test_call_returns_value_of_session_request(self):
        """
        Test that 'call' method returns the result of session request
        """
        result = base.call("GET", self.url, self.req_ctx)
        self.assertEqual(
            result, self.session.request.return_value,
            "Session request should be returned")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_http_error_immediately_when_status_code_not_in_retry_list(self):
        """
        Test that 'call' method raises an HTTPError without retrying if status
        code is not in list of retry codes.
        """
        self.make_retry_call_with_error_code(404, max_retries=3)
        self.assertEqual(1, self.session.request.call_count,
                         "Request call should have been made only once")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_http_error_after_max_retries_when_status_code_in_retry_list(self):
        """
        Test that 'call' method retries an HTTPError with retriable status code
        up to max_retries times before re-raising
        """
        max_retries = 3
        self.make_retry_call_with_error_code(503, max_retries=max_retries)
        # Check that the request call was made max_retries + 1 times.  The +1 is
        # to account for the initial request call.
        self.assertEqual(max_retries + 1, self.session.request.call_count,
                         "Call should have been made 'max_retries' + 1 times")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_makes_request_once_when_max_retries_explicitly_none(self):
        """
        Test that the 'call' method makes a single session request when
        max_retries was set to none on the request_context and passed in as none
        (parameter default).
        """
        self.req_ctx.max_retries = None
        self.make_retry_call_with_error_code(503)
        self.assertEqual(
            1, self.session.request.call_count,
            "When max_retries is None, it should default to 0 and not trigger a retry")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_defaults_to_context_max_retries(self):
        """
        Test that the 'call' method retries session requests for retriable error
        codes based on the max_retries setting on the request_context object
        when no value is otherwise specified in the call.
        """
        max_retries = 5
        self.req_ctx.max_retries = max_retries
        self.make_retry_call_with_error_code(503)
        self.assertEqual(
            max_retries + 1, self.session.request.call_count,
            "The number of retries should have defaulted back to value in request context")

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_canvas_api_error_with_attributes_on_non_retry_status(self):
        """
        Test that the CanvasAPIError that gets raised when an HTTPError gets
        thrown contains the expected status code from the response.
        """
        error_json = {'This is some error in json format!'}
        error_status_code = 404
        canvas_error = self.make_retry_call_with_error_code(
            error_status_code, max_retries=1, error_json=error_json)

        self.assertIs(type(canvas_error), CanvasAPIError)
        self.assertEqual(canvas_error.status_code, error_status_code)
        self.assertEqual(canvas_error.error_json, error_json)
        self.assertEqual(canvas_error.error_msg, str(error_json))

    @patch('canvas_sdk.client.base.RETRY_ERROR_CODES', (503,))
    def test_call_raises_canvas_api_error_with_attributes_after_retries_exhausted(self):
        """
        Test that the CanvasAPIError that gets raised after retriable HTTPErrors
        are exhausted, and that the error contains the expected status code from
        the response.
        """
        max_retries = 3
        error_code = 503
        error_json = {'This is some error in json format!'}
        canvas_error = self.make_retry_call_with_error_code(
            error_code, max_retries=max_retries, error_json=error_json)

        self.assertIs(type(canvas_error), CanvasAPIError)
        self.assertEqual(canvas_error.status_code, error_code)
        self.assertEqual(canvas_error.error_json, error_json)
        self.assertEqual(canvas_error.error_msg, str(error_json))

    def test_call_raises_invalid_oauth_token_error_when_401_and_auth_header(self):
        """
        Test that an InvalidOAuthTokenError gets raised on 401 responses that
        also contain the auth header.
        """
        error_code = 401
        resp_headers = {'WWW-Authenticate': ''}
        canvas_error = self.make_retry_call_with_error_code(
            error_code, max_retries=1, response_headers=resp_headers)

        self.assertIs(type(canvas_error), InvalidOAuthTokenError)

    def test_call_raises_canvas_api_error_when_401_and_other_header(self):
        """
        Test that the CanvasAPIError gets raised for 401s that don't contain
        the auth header, but may contain other response headers.
        """
        error_code = 401
        resp_headers = {'Content': 'application/json'}
        canvas_error = self.make_retry_call_with_error_code(
            error_code, max_retries=1, response_headers=resp_headers)

        self.assertIs(type(canvas_error), CanvasAPIError)

    def test_call_raises_canvas_api_error_when_non_401_and_auth_header(self):
        """
        Test that the CanvasAPIError gets raised for other error codes
        where the response contains the auth header
        """
        error_code = 404
        resp_headers = {'WWW-Authenticate': ''}
        canvas_error = self.make_retry_call_with_error_code(
            error_code, max_retries=1, response_headers=resp_headers)

        self.assertIs(type(canvas_error), CanvasAPIError)
