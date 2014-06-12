import unittest
from canvas_sdk.base_api_method import BaseAPIMethod


# Stub out concrete implementation for testing
class StubAPIMethod(BaseAPIMethod):

    def path(self):
        return '/path/to/method'

    def get_action(self):
        return 'GET'


class TestBaseApiMethod(unittest.TestCase):
    longMessage = True

    def test_initialization_kwargs(self):
        """
        Test that initialize populates kwargs
        """
        kwargs = {'key1': 'val1', 'key2': 'val2'}
        api_method = StubAPIMethod(**kwargs)
        for key, value in kwargs.iteritems():
            self.assertEquals(getattr(api_method, key), value,
                              "Initializer should have set instance attribute for all kwargs")

    def test_payload_no_args(self):
        """
        Test as_payload method result with no params returns empty dict
        """
        payload = StubAPIMethod().as_payload()
        self.assertEquals(
            len(payload), 0, "Payload when no arguments are passed should be an empty dict")

    def test_payload_with_args(self):
        """
        Test as_payload method result with params return dict with params
        """
        api_method = StubAPIMethod(foo='bar', bar='foo')
        self.assertEquals(api_method.as_payload(), api_method.__dict__,
                          "By default, payload should represent API method's __dict__")
