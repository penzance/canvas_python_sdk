import unittest
from mock import patch
from canvas_sdk.methods.sections import list_course_sections

MAX_RESULTS = 60  # used for setting the per_page and LIMIT_PER_PAGE values
COURSE_ID = 5956  # set a fake course id for the tests


class TestSections(unittest.TestCase):

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.get')
    def test_sections_list_course_sections(self, client_mock, mock_util):
        """
        Assert that list_course_sections returned the dictionary object defined in the client mock
        """
        client_mock.return_value = {'ok'}
        results = list_course_sections(COURSE_ID)
        self.assertEquals(results, {'ok'}, 'The client call did not return the correct result.')

    @patch('canvas_sdk.utils.build_url')
    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.get')
    def test_sections_list_course_sections_client_called_with_include_value(self, client_mock, mock_util, build_mock):
        """
        Assert that list_course_sections called the client with user specified values
        for include and per_page
        """
        list_course_sections(COURSE_ID, include='students', per_page=MAX_RESULTS)
        client_mock.assert_called_once_with(
            build_mock.return_value, {'include': 'students', 'per_page': MAX_RESULTS})

    @patch('canvas_sdk.utils.build_url')
    @patch('canvas_sdk.client.get')
    def test_sections_list_course_sections_build_url_called_with(self, client_mock, build_mock):
        """
        Assert that build_url is called with the expected parameters
        """
        list_course_sections(COURSE_ID)
        build_mock.assert_called_once_with('/v1/courses/%d/sections' % COURSE_ID)

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.get')
    def test_sections_list_course_sections_validate_attr_called_with(self, client_mock, validate_mock):
        """
        Assert that validate_attr_is_acceptable is called with the expected parameters
        """
        list_course_sections(COURSE_ID)
        validate_mock.assert_called_once_with(None, ('students', 'avatar_url'))

