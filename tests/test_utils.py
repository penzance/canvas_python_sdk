import unittest
import mock
from mock import patch
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

    @patch('canvas_sdk.utils.config.BASE_API_URL', HOSTNAME)
    def test_build_url_base_api_url_default_used(self):
        """
        Assert that the default BASE_API_URL is used when none is passed.
        Above we patch config.BASE_API_URL but this wont make it to the 
        method initialization. We need to patch the method defaults to used
        the mocked value. 
        """
        with patch.object(utils.build_url, '__defaults__', (utils.config.BASE_API_URL,)):
            url = utils.build_url(PATH)
            
        self.assertEquals(url, HOSTNAME + PATH, 'The urls are not equal, the BASE_API_URL in config may not be set.')

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

    def test_validate_attr_is_acceptable_raises_attributeerror_on_allow_none_true(self):
        """
        Assert that validate_attr_is_acceptable does not raise an AttributeError if the value is None
        and allow_none is True
        """
        try:
            utils.validate_attr_is_acceptable(None, ['b', 'c'], True)
        except AttributeError:
            print 'assert None can be passed when allow_none=True failed'
            raise
