"""
The util module contains helper methods for the SDK
"""
import config


def build_url(path, base_url=None):
    """ Return the given path appended to a base url (defaults to config setting). """

    if base_url is None:
        base_url = config.BASE_API_URL  # Try to set to config value if not passed in

    if 'http' not in base_url:
        raise AttributeError(
            'base_url ' + base_url + ' is not a URL. It may be that BASE_API_URL is not set in config.py, please update this value with the url to you canvas instance')

    return base_url + path


def validate_attr_is_acceptable(value, acceptable_values=[], allow_none=True):
    """
    Test an input value against a list of acceptable values.  A value of None may or may
    not be considered valid.  If the input is not valid, an Attribute error is raised, otherwise
    nothing is returned.
    """
    if value not in acceptable_values:
        # We know the value is not one of the acceptable values, but we need to also make sure
        # that the value is not None and that None is not an allowable value before raising
        # an exception
        if value is not None or not allow_none:
            raise AttributeError("%s must be one of %s" % (value, acceptable_values))
