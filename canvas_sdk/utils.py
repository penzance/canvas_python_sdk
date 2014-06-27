"""
The util module contains helper methods for the SDK
"""


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
