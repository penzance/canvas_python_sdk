import unittest
import mock
from mock import patch
from canvas_sdk import client
import time


MAX_RETRIES = 10


class TestClient(unittest.TestCase):
    longMessage = True

    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_when_session_var_is_none_creates_new_session(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        client.get_canvas_session()
        mock_request_session.assert_called_once_with()

    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_creates_adapter_with_retries(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        client.get_canvas_session()
        HTTPAdapter.assert_called_once_with(max_retries=MAX_RETRIES)
 
    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_calls_default_headers(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        client.get_canvas_session()
        get_default_headers.assert_called_once_with()
 
    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_mounts_http_and_https(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        result = client.get_canvas_session()
        calls = [mock.call('http://', HTTPAdapter.return_value), mock.call('https://', HTTPAdapter.return_value)]
        result.mount.assert_has_calls(calls, any_order=True)

    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_updates_headers_with_default_headers(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        result = client.get_canvas_session()
        result.headers.update.assert_called_once_with(get_default_headers.return_value)

    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_disables_streaming(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        result = client.get_canvas_session()
        self.assertEquals(result.stream, False, "Streaming should be disabled for http responses")

    @patch('canvas_sdk.client.requests.Session')
    @patch.multiple('canvas_sdk.client', MAX_RETRIES=MAX_RETRIES, _session=None, _session_create_time=0, get_default_headers=mock.DEFAULT, HTTPAdapter=mock.DEFAULT)
    def test_get_canvas_session_for_new_session_updates_session_create_time(self, mock_request_session, get_default_headers, HTTPAdapter):
        """
        Test that initialize populates kwargs
        """
        client.get_canvas_session()
        now = int(time.time())
        self.assertTrue(0 < client._session_create_time <= now, "Session creation time module variable should be set to a positive value that is <= now")
