
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
    
    """
    NOTE: this method of fully defining unicode and having str call upon it is referenced
    in official pydocs (https://docs.python.org/2/howto/pyporting.html) and other porting
    libraries (like Django utils).  If we move to Python 3, we'd rewrite this to just have
    a __str__ method and use futures and mixins to play nice with Python 2.
    """
    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __unicode__(self):
        return u'%s: %s' % (self.status_code, self.error_msg)
