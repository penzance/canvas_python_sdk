import unittest
from canvas_sdk.base_api_method import BaseAPIMethod


# Mock concrete implementation for testing
class MockAPIMethod(BaseAPIMethod):
    def path(self):
        return '/path/to/method'

    def get_action(self):
        return 'GET'


class TestBaseApiMethod(unittest.TestCase):
    longMessage = True

    def test_initialization_kwargs(self):
        kwargs = {'key1': 'val1', 'key2': 'val2'}
        api_method = MockAPIMethod(**kwargs)
        for key, value in kwargs.iteritems():
            self.assertEquals(getattr(api_method, key), value,
                              "Initializer should have set instance attribute for all kwargs")

    def test_payload_no_args(self):
        payload = MockAPIMethod().as_payload()
        self.assertEquals(
            len(payload), 0, "Payload when no arguments are passed should be an empty dict")

    def test_payload_with_args(self):
        api_method = MockAPIMethod(foo='bar', bar='foo')
        self.assertEquals(api_method.as_payload(), api_method.__dict__,
                          "By default, payload should represent API method's __dict__")
