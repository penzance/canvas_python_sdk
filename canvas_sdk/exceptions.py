
class SDKException(Exception):
    """ Base class for exceptions in the canvas python sdk """
    pass


class CanvasAPIError(SDKException):
    """
    Error that gets returned from Canvas API calls via request library.  Contains the
    http status code and the raw response from the API request.
    """

    def __init__(self, status_code=500, msg=None, error_json=None):
        self.status_code = status_code
        self.error_msg = msg
        self.error_json = error_json

    def __str__(self):
        return '%s: %s' % (self.status_code, self.error_msg)
