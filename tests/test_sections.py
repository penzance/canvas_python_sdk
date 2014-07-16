import unittest
import mock
from mock import patch
from canvas_sdk.client import RequestContext
from canvas_sdk.methods import sections


class TestSections(unittest.TestCase):

    def setUp(self):
        self.section_id = 1234
        self.course_id = 9999  # set a fake course id for the tests
        self.course_name = 'Fake Course'
        self.test_request_kwargs = {'headers': {'my': 'header'}, 'cert': 'my-cert'}
        # Set up the request context
        self.req_ctx = mock.MagicMock(name='request-context', spec=RequestContext)
        self.req_ctx.base_api_url = 'http://base/url/api'
        self.req_ctx.per_page = 10

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_get_called_with_request_context(self, mock_client_get, mock_validate):
        """
        Assert that request_context is passed to client 'get' call
        """
        sections.list_course_sections(self.req_ctx, self.course_id)
        mock_client_get.assert_called_once_with(
            self.req_ctx, mock.ANY, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_get_called_with_absolute_url(self, mock_client_get, mock_validate):
        """
        Assert that an absolute url made of base_api_url from context and method path is passed to client 'get' call
        """
        sections.list_course_sections(self.req_ctx, self.course_id)
        mock_client_get.assert_called_once_with(
            mock.ANY, self.req_ctx.base_api_url + '/v1/courses/%s/sections' % self.course_id, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_calls_validate_attributes(self, mock_client_get, mock_validate):
        """
        Assert that validate_attr_is_acceptable called for include
        """
        include = 'students'
        sections.list_course_sections(self.req_ctx, self.course_id, include)
        mock_validate.assert_called_once_with(include, ('students', 'avatar_url'))

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_get_called_with_default_values(self, mock_client_get, mock_validate):
        """
        Assert that client 'get' called with default values for payload data
        """
        # Per page should default to request_context's per_page value
        per_page_default = self.req_ctx.per_page
        sections.list_course_sections(self.req_ctx, self.course_id)
        mock_client_get.assert_called_once_with(
            mock.ANY, mock.ANY, payload={'include': None, 'per_page': per_page_default})

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_get_called_with_user_arg_values(self, mock_client_get, mock_validate):
        """
        Assert that client 'get' called with user defined arg values for payload data
        """
        include = 'students'
        per_page = 60
        sections.list_course_sections(self.req_ctx, self.course_id, include, per_page)
        mock_client_get.assert_called_once_with(
            mock.ANY, mock.ANY, payload={'include': include, 'per_page': per_page})

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_get_called_with_request_kwargs(self, mock_client_get, mock_validate):
        """
        Assert that client 'get' called with kwargs as additional parameters
        """
        sections.list_course_sections(self.req_ctx, self.course_id, **self.test_request_kwargs)
        mock_client_get.assert_called_once_with(
            mock.ANY, mock.ANY, payload=mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.methods.sections.utils.validate_attr_is_acceptable')
    @patch('canvas_sdk.methods.sections.client.get')
    def test_list_course_sections_returns_result_from_get(self, mock_client_get, mock_validate):
        """
        Assert that method returned the result of client 'get' call
        """
        results = sections.list_course_sections(self.req_ctx, self.course_id)
        self.assertEquals(results, mock_client_get.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_sections_post_called_with_request_context(self, mock_client_post):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.create_course_section(self.req_ctx, self.course_id, self.course_name)
        mock_client_post.assert_called_once_with(
            self.req_ctx, mock.ANY, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_sections_post_called_with_absolute_url(self, mock_client_post):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.create_course_section(self.req_ctx, self.course_id, self.course_name)
        mock_client_post.assert_called_once_with(
            mock.ANY, self.req_ctx.base_api_url + '/v1/courses/%s/sections' % self.course_id, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_sections_post_called_with_default_values(self, mock_client_post):
        """
        Assert that client 'post' called with default values for payload data
        """
        sections.create_course_section(self.req_ctx, self.course_id, self.course_name)
        mock_client_post.assert_called_once_with(
            mock.ANY, mock.ANY, payload={
                'course_section[name]': self.course_name,
                'course_section[sis_section_id]': None,
                'course_section[start_at]': None,
                'course_section[end_at]': None}
        )

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_sections_post_called_with_user_arg_values(self, mock_client_post):
        """
        Assert that client 'post' called with user's arg values for payload data
        """
        sis_section_id = '123ABCD'
        start_at = '2011-01-01T01:00Z'
        end_at = '2011-02-01T01:00Z'
        sections.create_course_section(self.req_ctx, self.course_id, self.course_name, sis_section_id, start_at, end_at)
        mock_client_post.assert_called_once_with(
            mock.ANY, mock.ANY, payload={
                'course_section[name]': self.course_name,
                'course_section[sis_section_id]': sis_section_id,
                'course_section[start_at]': start_at,
                'course_section[end_at]': end_at}
        )

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_section_post_called_with_request_kwargs(self, mock_client_post):
        """
        Assert that client 'post' called with kwargs as additional parameters
        """
        sections.create_course_section(self.req_ctx, self.course_id, self.course_name, **self.test_request_kwargs)
        mock_client_post.assert_called_once_with(
            mock.ANY, mock.ANY, payload=mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.methods.sections.client.post')
    def test_create_course_section_returns_result_from_post(self, mock_client_post):
        """
        Assert that method returned the result of client 'post' call
        """
        results = sections.create_course_section(self.req_ctx, self.course_id, self.course_name)
        self.assertEquals(results, mock_client_post.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.methods.sections.client.put')
    def test_edit_section_put_called_called_with_request_context(self, mock_client_put):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.edit_section(self.req_ctx, self.section_id)
        mock_client_put.assert_called_once_with(self.req_ctx, mock.ANY, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.client.put')
    def test_edit_section_put_called_called_with_absolute_url(self, mock_client_put):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.edit_section(self.req_ctx, self.section_id)
        mock_client_put.assert_called_once_with(
            mock.ANY, self.req_ctx.base_api_url + '/v1/sections/%s' % self.section_id, payload=mock.ANY)

    @patch('canvas_sdk.methods.sections.client.put')
    def test_edit_section_put_called_with_user_arg_values(self, mock_client_put):
        """
        Assert that client 'put' called with user's arg values for payload data
        """
        sis_section_id = '123ABCD'
        start_at = '2011-01-01T01:00Z'
        end_at = '2011-02-01T01:00Z'
        sections.edit_section(self.req_ctx, self.section_id, self.course_name, sis_section_id, start_at, end_at)
        mock_client_put.assert_called_once_with(
            mock.ANY, mock.ANY, payload={
                'course_section[name]': self.course_name,
                'course_section[sis_section_id]': sis_section_id,
                'course_section[start_at]': start_at,
                'course_section[end_at]': end_at}
        )

    @patch('canvas_sdk.methods.sections.client.put')
    def test_edit_section_put_called_with_request_kwargs(self, mock_client_put):
        """
        Assert that client 'put' called with kwargs as additional parameters
        """
        sections.edit_section(self.req_ctx, self.section_id, **self.test_request_kwargs)
        mock_client_put.assert_called_once_with(
            mock.ANY, mock.ANY, payload=mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.methods.sections.client.put')
    def test_edit_section_returns_result_from_put(self, mock_client_put):
        """
        Assert that method returned the result of client 'delete' call
        """
        results = sections.edit_section(self.req_ctx, self.section_id)
        self.assertEquals(results, mock_client_put.return_value, 'The client call did not return the correct result.')

    @patch('canvas_sdk.methods.sections.client.delete')
    def test_delete_section_delete_called_called_with_request_context(self, mock_client_delete):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.delete_section(self.req_ctx, self.section_id)
        mock_client_delete.assert_called_once_with(self.req_ctx, mock.ANY)

    @patch('canvas_sdk.methods.sections.client.delete')
    def test_delete_section_delete_called_called_with_absolute_url(self, mock_client_delete):
        """
        Assert that request_context.per_page is called when no user value passed in
        """
        sections.delete_section(self.req_ctx, self.section_id)
        mock_client_delete.assert_called_once_with(
            mock.ANY, self.req_ctx.base_api_url + '/v1/sections/%s' % self.section_id)

    @patch('canvas_sdk.methods.sections.client.delete')
    def test_delete_section_delete_called_with_request_kwargs(self, mock_client_delete):
        """
        Assert that client 'delete' called with kwargs as additional parameters
        """
        sections.delete_section(self.req_ctx, self.section_id, **self.test_request_kwargs)
        mock_client_delete.assert_called_once_with(
            mock.ANY, mock.ANY, **self.test_request_kwargs)

    @patch('canvas_sdk.methods.sections.client.delete')
    def test_delete_section_returns_result_from_delete(self, mock_client_delete):
        """
        Assert that method returned the result of client 'delete' call
        """
        results = sections.delete_section(self.req_ctx, self.section_id)
        self.assertEquals(results, mock_client_delete.return_value, 'The client call did not return the correct result.')
