import unittest
import mock
from mock import patch
from canvas_sdk.methods import sections

MAX_RESULTS = 60  # used for setting the per_page and LIMIT_PER_PAGE values


@patch('canvas_sdk.methods.sections.config.LIMIT_PER_PAGE', MAX_RESULTS)
@patch('canvas_sdk.utils.build_url')
class TestSections(unittest.TestCase):

    def setUp(self):
        self.section_id = 1234
        self.course_id = 9999  # set a fake course id for the tests
        self.course_name = 'Fake Course'
        self.test_request_kwargs = {'headers': {'my': 'header'}, 'cert': 'my-cert'}

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_build_url_called(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that build_url is called with the expected parameters
        """
        sections.list_course_sections(self.course_id)
        mock_build_url.assert_called_once_with('/v1/courses/%d/sections' % self.course_id)

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_validate_attributes_called(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that validate_attr_is_acceptable called for include
        """
        include = 'students'
        sections.list_course_sections(self.course_id, include)
        mock_validate.assert_called_once_with(include, ('students', 'avatar_url'))

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_get_called_with_default_values(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that client 'get' called with default values for payload data
        """
        sections.list_course_sections(self.course_id)
        mock_client_get.assert_called_once_with(
            mock_build_url.return_value, payload={'include': None, 'per_page': MAX_RESULTS})

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_get_called_with_user_arg_values(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that client 'get' called with user defined arg values for payload data
        """
        include = 'students'
        per_page = MAX_RESULTS * 2
        sections.list_course_sections(self.course_id, include, per_page)
        mock_client_get.assert_called_once_with(
            mock_build_url.return_value, payload={'include': include, 'per_page': per_page})

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_get_called_with_request_kwargs(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that client 'get' called with kwargs as additional parameters
        """
        sections.list_course_sections(self.course_id, **self.test_request_kwargs)
        mock_client_get.assert_called_once_with(
            mock_build_url.return_value, payload=mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.client.base.get')
    def test_list_course_sections_returns_result_from_get(self, mock_client_get, mock_validate, mock_build_url):
        """
        Assert that method returned the result of client 'get' call
        """
        results = sections.list_course_sections(self.course_id)
        self.assertEquals(results, mock_client_get.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.client.base.post')
    def test_create_course_section_build_url_called(self, mock_client_get, mock_build_url):
        """
        Assert that build_url is called with the expected parameters
        """
        sections.create_course_section(self.course_id, self.course_name)
        mock_build_url.assert_called_once_with('/v1/courses/%d/sections' % self.course_id)

    @patch('canvas_sdk.client.base.post')
    def test_create_course_sections_post_called_with_default_values(self, mock_client_post, mock_build_url):
        """
        Assert that client 'post' called with default values for payload data
        """
        sections.create_course_section(self.course_id, self.course_name)
        mock_client_post.assert_called_once_with(
            mock_build_url.return_value, payload={'course_section[name]': self.course_name, 'course_section[sis_section_id]': None, 'course_section[start_at]': None, 'course_section[end_at]': None})

    @patch('canvas_sdk.client.base.post')
    def test_create_course_sections_post_called_with_user_arg_values(self, mock_client_post, mock_build_url):
        """
        Assert that client 'post' called with user's arg values for payload data
        """
        sis_section_id = '123ABCD'
        start_at = '2011-01-01T01:00Z'
        end_at = '2011-02-01T01:00Z'
        sections.create_course_section(self.course_id, self.course_name, sis_section_id, start_at, end_at)
        mock_client_post.assert_called_once_with(
            mock_build_url.return_value, payload={'course_section[name]': self.course_name, 'course_section[sis_section_id]': sis_section_id, 'course_section[start_at]': start_at, 'course_section[end_at]': end_at})

    @patch('canvas_sdk.client.base.post')
    def test_create_course_section_post_called_with_request_kwargs(self, mock_client_post, mock_build_url):
        """
        Assert that client 'post' called with kwargs as additional parameters
        """
        sections.create_course_section(self.course_id, self.course_name, **self.test_request_kwargs)
        mock_client_post.assert_called_once_with(
            mock_build_url.return_value, payload=mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.client.base.post')
    def test_create_course_section_returns_result_from_post(self, mock_client_post, mock_build_url):
        """
        Assert that method returned the result of client 'post' call
        """
        results = sections.create_course_section(self.course_id, self.course_name)
        self.assertEquals(results, mock_client_post.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.client.base.put')
    def test_edit_section_build_url_called(self, mock_client_put, mock_build_url):
        """
        Assert that build_url is called with the expected parameters
        """
        sections.edit_section(self.section_id)
        mock_build_url.assert_called_once_with('/v1/sections/%d' % self.section_id)

    @patch('canvas_sdk.client.base.put')
    def test_edit_section_put_called_with_default_values(self, mock_client_put, mock_build_url):
        """
        Assert that client 'put' called with default values for payload data
        """
        sections.edit_section(self.section_id)
        mock_client_put.assert_called_once_with(mock_build_url.return_value)

    @patch('canvas_sdk.client.base.put')
    def test_edit_section_put_called_with_request_kwargs(self, mock_client_put, mock_build_url):
        """
        Assert that client 'put' called with kwargs as additional parameters
        """
        sections.edit_section(self.section_id, **self.test_request_kwargs)
        mock_client_put.assert_called_once_with(
            mock_build_url.return_value, **self.test_request_kwargs)

    @patch('canvas_sdk.client.base.put')
    def test_edit_section_returns_result_from_put(self, mock_client_put, mock_build_url):
        """
        Assert that method returned the result of client 'delete' call
        """
        results = sections.edit_section(self.section_id)
        self.assertEquals(results, mock_client_put.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.client.base.delete')
    def test_delete_section_build_url_called(self, mock_client_delete, mock_build_url):
        """
        Assert that build_url is called with the expected parameters
        """
        sections.delete_section(self.section_id)
        mock_build_url.assert_called_once_with('/v1/sections/%d' % self.section_id)

    @patch('canvas_sdk.client.base.delete')
    def test_delete_section_delete_called_with_default_values(self, mock_client_delete, mock_build_url):
        """
        Assert that client 'delete' called with default values for payload data
        """
        sections.delete_section(self.section_id)
        mock_client_delete.assert_called_once_with(mock_build_url.return_value)

    @patch('canvas_sdk.client.base.delete')
    def test_delete_section_delete_called_with_request_kwargs(self, mock_client_delete, mock_build_url):
        """
        Assert that client 'delete' called with kwargs as additional parameters
        """
        sections.delete_section(self.section_id, **self.test_request_kwargs)
        mock_client_delete.assert_called_once_with(
            mock_build_url.return_value, **self.test_request_kwargs)

    @patch('canvas_sdk.client.base.delete')
    def test_delete_section_returns_result_from_delete(self, mock_client_delete, mock_build_url):
        """
        Assert that method returned the result of client 'delete' call
        """
        results = sections.delete_section(self.section_id)
        self.assertEquals(results, mock_client_delete.return_value, 'The client call did not return the correct result.')

