import unittest
from canvas_sdk import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.path = '/v1/accounts'

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
