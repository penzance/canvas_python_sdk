import unittest
import mock
from mock import patch
from canvas_sdk.client import session
import time

MAX_RETRIES = 10  # A default value used for testing get_canvas_session calls
AUTH_TOKEN = 'testAuthToken'  # Bogus auth token used to get call
DEFAULT_SESSION_PATCHES = {'MAX_RETRIES': MAX_RETRIES, '_session': None, '_session_create_time': 0,
                           'HTTPAdapter': mock.DEFAULT}


class TestSession(unittest.TestCase):
    longMessage = True

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_updates_global_session_variable(self, mock_request_session, HTTPAdapter):
        """
        Test that global session variable is set when new session is created.
        """
        result = session.get_canvas_session()
        self.assertEqual(session._session, result,
                         "When retrieving canvas session, if a new session is created the global _session variable should be set as well.")

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_for_new_session_updates_session_create_time(self, mock_request_session, HTTPAdapter):
        """
        Test that global session creation time variable is set when new session is created.
        """
        session.get_canvas_session()
        now = int(time.time())
        self.assertTrue(0 < session._session_create_time <= now,
                        "Session creation time module variable should be set to a positive value that is <= now")

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_when_session_var_is_none_creates_new_session(self, mock_request_session, HTTPAdapter):
        """
        Test that a new session object is created when global session variable is None.
        """
        session.get_canvas_session()
        mock_request_session.assert_called_once_with()

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_for_new_session_creates_adapter_with_retries(self, mock_request_session, HTTPAdapter):
        """
        Test that a new session object initializes an HTTPAdapter with expected max_retries
        """
        session.get_canvas_session()
        HTTPAdapter.assert_called_once_with(max_retries=MAX_RETRIES)

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_for_new_session_mounts_http_and_https(self, mock_request_session, HTTPAdapter):
        """
        Test that a new session object mounts both http:// and https:// calls
        """
        result = session.get_canvas_session()
        calls = [mock.call('http://', HTTPAdapter.return_value),
                 mock.call('https://', HTTPAdapter.return_value)]
        result.mount.assert_has_calls(calls, any_order=True)

    @patch('canvas_sdk.client.session.requests.Session')
    @patch.multiple('canvas_sdk.client.session', **DEFAULT_SESSION_PATCHES)
    def test_get_canvas_session_for_new_session_disables_streaming(self, mock_request_session, HTTPAdapter):
        """
        Test that a new session object has streaming disabled.
        """
        result = session.get_canvas_session()
        self.assertEqual(result.stream, False, "Streaming should be disabled for http responses")

    @patch('canvas_sdk.client.session.requests.Session')
    @patch('canvas_sdk.client.session.config.SESSION_EXPIRATION_TIME_SECS', 0)
    @patch.multiple('canvas_sdk.client.session', **dict(DEFAULT_SESSION_PATCHES.items() + [('_session', mock.DEFAULT)]))
    def test_get_canvas_session_creates_new_session_when_expired(self, mock_request_session, _session, HTTPAdapter):
        """
        Test that a new session object is created when session expiration time (based off of creation time) has passed
        """
        result = session.get_canvas_session()
        self.assertNotEqual(
            result, _session, "When session time has expired, a new session object should be created and returned")

    @patch('canvas_sdk.client.session.requests.Session')
    @patch('canvas_sdk.client.session.config.SESSION_EXPIRATION_TIME_SECS', 999999)
    @patch.multiple('canvas_sdk.client.session', _session=mock.DEFAULT, _session_create_time=int(time.time()))
    def test_get_canvas_session_returns_existing_session_when_not_expired(self, mock_request_session, _session):
        """
        Test that if the session was previously set and has not expired, the existing session should be returned.  Set expiration time
        to a very large number and creation time to "now" so that expiration logic will be False.
        """
        result = session.get_canvas_session()
        self.assertEqual(
            result, _session, "If session was previously set and has not expired, it should be returned without modification")
