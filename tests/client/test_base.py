import unittest
import mock
from mock import patch
from canvas_sdk.client import base
from requests.exceptions import HTTPError


class TestBase(unittest.TestCase):
    longMessage = True

    def setUp(self):
        self.url = "http://test.url"
        self.payload = {'foo': 'bar'}
        self.request_kwargs = {'headers': {'my': 'header'}, 'auth': ('user', 'pass')}

    @patch('canvas_sdk.client.base.call')
    def test_get_returns_call(self, call_mock):
        """
        Test that the call to get helper method returns the result of 'call'
        """
        result = base.get(self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'get' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_get_with_defaults(self, call_mock):
        """
        Test that the call to get helper method with defaults passes url and action
        """
        base.get(self.url)
        call_mock.assert_called_once_with("GET", self.url, params=None)

    @patch('canvas_sdk.client.base.call')
    def test_get_with_payload(self, call_mock):
        """
        Test that the call to get helper method with a payload passes it into params
        """
        base.get(self.url, self.payload)
        call_mock.assert_called_once_with("GET", self.url, params=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_get_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to get helper method with a payload passes it into params
        """
        base.get(self.url, **self.request_kwargs)
        call_mock.assert_called_once_with("GET", self.url, params=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_get_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to get helper method with a payload passes it into params
        """
        base.get(self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            "GET", self.url, params=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_put_returns_call(self, call_mock):
        """
        Test that the call to put helper method returns the result of 'call'
        """
        result = base.put(self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'put' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_put_with_defaults(self, call_mock):
        """
        Test that the call to put helper method with defaults passes url and action
        """
        base.put(self.url)
        call_mock.assert_called_once_with("PUT", self.url, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_payload(self, call_mock):
        """
        Test that the call to put helper method with a payload passes it into params
        """
        base.put(self.url, self.payload)
        call_mock.assert_called_once_with("PUT", self.url, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to put helper method with a payload passes it into params
        """
        base.put(self.url, **self.request_kwargs)
        call_mock.assert_called_once_with("PUT", self.url, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_put_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to put helper method with a payload passes it into params
        """
        base.put(self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with("PUT", self.url, data=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_post_returns_call(self, call_mock):
        """
        Test that the call to post helper method returns the result of 'call'
        """
        result = base.post(self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'post' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_post_with_defaults(self, call_mock):
        """
        Test that the call to post helper method with defaults passes url and action
        """
        base.post(self.url)
        call_mock.assert_called_once_with("POST", self.url, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_payload(self, call_mock):
        """
        Test that the call to post helper method with a payload passes it into params
        """
        base.post(self.url, self.payload)
        call_mock.assert_called_once_with("POST", self.url, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to post helper method with a payload passes it into params
        """
        base.post(self.url, **self.request_kwargs)
        call_mock.assert_called_once_with("POST", self.url, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_post_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to post helper method with a payload passes it into params
        """
        base.post(self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            "POST", self.url, data=self.payload, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_delete_returns_call(self, call_mock):
        """
        Test that the call to put helper method returns the result of 'call'
        """
        result = base.delete(self.url)
        self.assertEqual(result, call_mock.return_value,
                         "Call to 'delete' should return result of 'call' method")

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_defaults(self, call_mock):
        """
        Test that the call to delete helper method with defaults passes url and action
        """
        base.delete(self.url)
        call_mock.assert_called_once_with("DELETE", self.url, data=None)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_payload(self, call_mock):
        """
        Test that the call to delete helper method with a payload passes it into params
        """
        base.delete(self.url, self.payload)
        call_mock.assert_called_once_with("DELETE", self.url, data=self.payload)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_request_kwargs_and_no_payload(self, call_mock):
        """
        Test that the call to delete helper method with a payload passes it into params
        """
        base.delete(self.url, **self.request_kwargs)
        call_mock.assert_called_once_with("DELETE", self.url, data=None, **self.request_kwargs)

    @patch('canvas_sdk.client.base.call')
    def test_delete_with_request_kwargs_and_payload(self, call_mock):
        """
        Test that the call to delete helper method with a payload passes it into params
        """
        base.delete(self.url, self.payload, **self.request_kwargs)
        call_mock.assert_called_once_with(
            "DELETE", self.url, data=self.payload, **self.request_kwargs)

    @patch.multiple('canvas_sdk.client.base', MAX_RETRIES=1, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_retrieves_session_object(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that the 'call' method uses canvas session
        """
        base.call("GET", self.url)
        get_canvas_session.assert_called_once_with()

    @patch.multiple('canvas_sdk.client.base', MAX_RETRIES=1, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_updates_kwargs_with_helper_method(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method updates kwargs based on defaults and any kwargs passed in
        """
        base.call("GET", self.url, **self.request_kwargs)
        set_default_request_params_for_kwargs.assert_called_once_with(self.request_kwargs)

    @patch.multiple('canvas_sdk.client.base', MAX_RETRIES=1, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_makes_request_on_session(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method makes session request with expected parameters
        """
        base.call("GET", self.url, **self.request_kwargs)
        get_canvas_session.return_value.request.assert_called_once_with(
            "GET", self.url, **self.request_kwargs)

    @patch.multiple('canvas_sdk.client.base', MAX_RETRIES=1, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_raises_status_on_result(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method makes call to raise_for_status on result object
        """
        result = base.call("GET", self.url, **self.request_kwargs)
        result.raise_for_status.assert_called_once_with()

    @patch.multiple('canvas_sdk.client.base', MAX_RETRIES=1, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_returns_value_of_session_request(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method returns the result of session request
        """
        result = base.call("GET", self.url, **self.request_kwargs)
        self.assertEqual(result, get_canvas_session.return_value.request.return_value)

    @patch.multiple('canvas_sdk.client.base', RETRY_ERROR_CODES=(503,), MAX_RETRIES=2, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_raises_http_error_immediately_when_status_code_not_in_retry_list(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method raises an HTTPError without retrying if status code is not in list of retry codes
        """
        get_canvas_session.return_value.request.return_value.raise_for_status.side_effect = HTTPError(
            response=mock.MagicMock(status_code=404))
        with self.assertRaises(HTTPError):
            base.call("GET", self.url, **self.request_kwargs)
        # Check that the request call was made only once
        self.assertEqual(1, get_canvas_session.return_value.request.call_count)

    @patch.multiple('canvas_sdk.client.base', RETRY_ERROR_CODES=(503,), MAX_RETRIES=2, get_canvas_session=mock.DEFAULT, set_default_request_params_for_kwargs=mock.DEFAULT)
    def test_call_raises_http_error_after_max_retries_when_status_code_in_retry_list(self, get_canvas_session, set_default_request_params_for_kwargs):
        """
        Test that 'call' method retries an HTTPError with retriable status code up to MAX_RETRIES times before re-raising
        """
        get_canvas_session.return_value.request.return_value.raise_for_status.side_effect = HTTPError(
            response=mock.MagicMock(status_code=503))
        with self.assertRaises(HTTPError):
            base.call("GET", self.url, **self.request_kwargs)
        # Check that the request call was made MAX_RETRIES + 1 times.  The +1 is to account for the
        # initial request call
        self.assertEqual(base.MAX_RETRIES + 1, get_canvas_session.return_value.request.call_count)
