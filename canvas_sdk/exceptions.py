from __future__ import unicode_literals
from future.utils import python_2_unicode_compatible


class SDKException(Exception):

    """ Base class for exceptions in the canvas python sdk """
    pass


class InvalidOAuthTokenError(SDKException):
    """ Indicates that an invalid access token made the request """
    pass

@python_2_unicode_compatible
class CanvasAPIError(SDKException):

    """
    Error that gets returned from Canvas API calls via request library.  Contains the
    http status code and the raw json response from the API request.  Note that the
    structure of the json sent back by Canvas can vary depending on the type of error.
    """

    def __init__(self, status_code=500, msg=None, error_json=None):
        self.status_code = status_code
        self.error_msg = msg
        self.error_json = error_json

    """
    NOTE: this method of fully defining unicode and having str call upon it is referenced
    in official pydocs (https://docs.python.org/2/howto/pyporting.html) and other porting
    libraries (like Django utils).  If we move to Python 3, we'd rewrite this to just have
    a __str__ method and use futures and mixins to play nice with Python 2.
    """

    def __str__(self):
        if self.error_msg:
            return '%s: %s' % (self.status_code, self.error_msg)
        else:
            return '%s' % self.status_code
