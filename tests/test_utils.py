import unittest

from canvas_sdk import utils

HOSTNAME = 'http://hostname/api'
BAD_HOSTNAME = '//somehostname'
PATH = '/v1/accounts'


class TestUtils(unittest.TestCase):

    def test_util_build_url(self):
        """
        Assert that build_url build a url string from the given parameters
        """
        url = utils.build_url(PATH, HOSTNAME)
        self.assertEquals(url, HOSTNAME + PATH)

    def test_util_build_url_raises_attributeerror(self):
        """
        Assert that build_url build a url string from the given parameters
        """
        self.assertRaises(AttributeError, utils.build_url, PATH, BAD_HOSTNAME)

    def test_validate_attr_is_acceptable_raises_attributeerror(self):
        """
        Assert that validate_attr_is_acceptable raises an AttributeError if the given
        value does not match an entry in the acceptable_values list
        """
        self.assertRaises(AttributeError, utils.validate_attr_is_acceptable, 'a', ['b', 'c'])

    def test_validate_attr_is_acceptable_raises_attributeerror_on_allow_none_false(self):
        """
        Assert that validate_attr_is_acceptable raises an AttributeError if the value is None
        and allow_none is False
        """
        self.assertRaises(
            AttributeError, utils.validate_attr_is_acceptable, None, ['b', 'c'], False)

