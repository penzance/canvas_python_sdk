import unittest
from mock import patch
from canvas_sdk import base_api_method
from canvas_sdk.methods.sections import ListCourseSections


class TestListCourseSections(unittest.TestCase):
    longMessage = True

    def setUp(self):
        course_id = '9999'
        self.api_method = ListCourseSections(course_id)
        self.test_course_id = course_id

    @patch.object(base_api_method.BaseAPIMethod, '__init__')
    def test_instance_setup_required_params(self, mock_super_init):
        ListCourseSections(self.test_course_id)
        mock_super_init.assert_called_once_with(course_id=self.test_course_id, include=None)

    @patch.object(base_api_method.BaseAPIMethod, '__init__')
    def test_instance_setup_optional_params(self, mock_super_init):
        include = 'foo'
        ListCourseSections(self.test_course_id, include)
        mock_super_init.assert_called_once_with(course_id=self.test_course_id, include=include)

    def test_get_action(self):
        action = self.api_method.get_action()
        self.assertEquals(action, ListCourseSections.ACTION,
                          "Result of get_action call should match class action attribute")

    def test_path_property(self):
        path = self.api_method.path
        self.assertEquals(path, ListCourseSections._path.format(course_id=self.test_course_id),
                          "path should be a formatted version of 'private' _path class variable with course_id substitution")

    def test_include_getter_setter_against_valid_values(self):
        for value in ListCourseSections.INCLUDE_TYPES:
            self.api_method.include = value
            self.assertEquals(value, self.api_method.include,
                              "Include property should match what was set for valid values")

    def test_include_getter_setter_with_none(self):
        self.api_method.include = None
        self.assertEquals(None, self.api_method.include,
                          "Include property should allow for value set to 'None'")

    def test_include_setter_with_invalid_value_raises_exception(self):
        with self.assertRaises(AttributeError):
            self.api_method.include = 'foo'
