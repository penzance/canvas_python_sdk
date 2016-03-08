import unittest
from canvas_sdk.exceptions import CanvasAPIError


class TestExceptions(unittest.TestCase):
    longMessage = True

    def setUp(self):
        self.default_api_error = CanvasAPIError()

    def test_default_status_for_canvas_api_error(self):
        """ Test expected default status for instance of CanvasAPIError """
        self.assertEqual(self.default_api_error.status_code, 500)

    def test_default_message_for_canvas_api_error(self):
        """ Test expected default msg attribute for instance of CanvasAPIError """
        self.assertIsNone(self.default_api_error.error_msg)

    def test_default_error_json_for_canvas_api_error(self):
        """ Test expected default error_json attribute for instance of CanvasAPIError """
        self.assertIsNone(self.default_api_error.error_json)

    def test_default_str_for_canvas_api_error(self):
        """ Test default CanvasAPIError instance represented as a str """
        self.assertEqual('500', str(self.default_api_error))

    def test_default_unicode_for_canvas_api_error(self):
        """ Test default CanvasAPIError instance represented as unicode """
        self.assertEqual(u'500', unicode(self.default_api_error))

    def test_instance_str_for_canvas_api_error(self):
        """ Test string representation of CanvasAPIError with custom attributes """
        status = 404
        error_msg = 'This is a test message'
        error_json = {'Some error json'}

        api_error = CanvasAPIError(status_code=status, msg=error_msg, error_json=error_json)
        self.assertEqual('%d: %s' % (status, error_msg), str(api_error))
