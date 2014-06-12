import abc


class BaseAPIMethod(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    @abc.abstractproperty
    def path(self):
        """ The relative path to the API method
        """

    @abc.abstractmethod
    def get_action(self):
        """ The HTTP action - should be in GET/PUT/POST/DELETE
        """

    def as_payload(self):
        """ A dictionary representation of the method data
        that is used to make an API request
        """
        return self.__dict__
