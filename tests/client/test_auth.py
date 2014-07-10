import unittest
import mock
from canvas_sdk.client import auth

AUTH_TOKEN = 'testAuthToken'  # Bogus auth token used to get call


class TestAuth(unittest.TestCase):
    longMessage = True

    def test_initialize_oauth2_bearer_no_token_raises_exception(self):
        """
        Test that global session variable is set when new session is created.
        """
        with self.assertRaises(AttributeError):
            auth.OAuth2Bearer(None)

    def test_initialize_oauth2_bearer_empty_token_raises_exception(self):
        """
        Test that global session variable is set when new session is created.
        """
        with self.assertRaises(AttributeError):
            auth.OAuth2Bearer('')

    def test_initialize_oauth2_bearer_with_token_sets_attribute(self):
        """
        Test that global session variable is set when new session is created.
        """
        result = auth.OAuth2Bearer(AUTH_TOKEN)
        self.assertEqual(result.oauth2_token, AUTH_TOKEN, "Initializing OAuth2Bearer class should set oauth2_token instance attribute")

    def test_calling_oauth2_bearer_sets_authorization_header(self):
        """
        Test that global session variable is set when new session is created.
        """
        auth_bearer = auth.OAuth2Bearer(AUTH_TOKEN)
        request_mock = mock.MagicMock(headers={})
        response = auth_bearer(request_mock)
        self.assertEqual(response.headers['Authorization'], 'Bearer %s' % AUTH_TOKEN)
