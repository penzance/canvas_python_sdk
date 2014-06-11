from canvas_sdk.base_api_method import BaseAPIMethod


class ListCourseSections(BaseAPIMethod):
    _path = '/v1/courses/{course_id}/sections'
    ACTION = 'GET'
    INCLUDE_TYPES = ('students', 'avatar_url')

    def __init__(self, course_id, include=None):
        super(ListCourseSections, self).__init__(course_id=course_id, include=include)

    @classmethod
    def get_action(cls):
        return cls.ACTION

    @property
    def path(self):
        return self._path.format(course_id=self.course_id)

    @property
    def include(self):
        return self.__dict__.get('include', None)

    @include.setter
    def include(self, value):
        if value is not None and value not in self.INCLUDE_TYPES:
            raise AttributeError("%s must be one of %s" % (value, self.INCLUDE_TYPES))
        else:
            self.__dict__.update(include=value)
