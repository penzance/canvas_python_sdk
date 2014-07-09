import unittest
import mock
import requests
from mock import patch
from canvas_sdk import utils
from canvas_sdk.client import RequestContext


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.path = '/v1/accounts'
        self.req_ctx = mock.MagicMock(name='request-context', spec=RequestContext)

    def build_response_mock(self, links=None, json_data=None):
        """
        Build a MagicMock to imitate a requests.Response where the json call returns the input
        json_data in a list
        """
        response = mock.MagicMock(spec=requests.Response)
        response.links = links or {}  # Default to no header links
        response.json.return_value = json_data if json_data else mock.DEFAULT
        return response

    def test_validate_attr_is_acceptable_raises_attributeerror(self):
        """
        Assert that validate_attr_is_acceptable raises an AttributeError if the given
        value does not match an entry in the acceptable_values list
        """
        self.assertRaises(AttributeError, utils.validate_attr_is_acceptable, 'a', ['b', 'c'])

    def test_validate_attr_is_acceptable_raises_attributeerror_on_allow_none_false(self):
        """
        Assert that validate_attr_is_acceptable raises an AttributeError if the value is None
        and allow_none is False
        """
        self.assertRaises(
            AttributeError, utils.validate_attr_is_acceptable, None, ['b', 'c'], False)

    def test_validate_attr_is_acceptable_raises_attributeerror_on_allow_none_true(self):
        """
        Assert that validate_attr_is_acceptable does not raise an AttributeError if the value is None
        and allow_none is True
        """
        try:
            utils.validate_attr_is_acceptable(None, ['b', 'c'], True)
        except AttributeError:
            print 'assert None can be passed when allow_none=True failed'
            raise

    @patch('canvas_sdk.utils.client.get')
    def test_get_next_for_response_without_a_next_link_yields_nothing(self, mock_client_get):
        """
        Assert that call to get_next with a response that doesn't have any 'next' links doesn't iterate.
        """
        initial_response = self.build_response_mock()
        with self.assertRaises(StopIteration):
            next(utils.get_next(self.req_ctx, initial_response))
        self.assertTrue(not mock_client_get.called)

    @patch('canvas_sdk.utils.client.get')
    def test_get_next_for_response_with_a_next_link_calls_client_get_with_request_context(self, mock_client_get):
        """
        Assert that call to get_next with a response that has 'next' links (in this case one additional
        page) calls the client "get" method with the request context.
        """
        initial_response = self.build_response_mock({'next': {'url': 'http://next-url'}})

        next(utils.get_next(self.req_ctx, initial_response))
        mock_client_get.assert_called_once_with(self.req_ctx, mock.ANY)

    @patch('canvas_sdk.utils.client.get')
    def test_get_next_for_response_with_a_next_link_calls_client_get_with_url(self, mock_client_get):
        """
        Assert that call to get_next with a response that has 'next' links (in this case one additional
        page) calls the client "get" method with the next url.
        """
        next_url = 'http://next-url'
        initial_response = self.build_response_mock({'next': {'url': next_url}})

        next(utils.get_next(self.req_ctx, initial_response))
        mock_client_get.assert_called_once_with(mock.ANY, next_url)

    @patch('canvas_sdk.utils.client.get')
    def test_get_next_for_response_with_a_next_link_returns_next_response(self, mock_client_get):
        """
        Assert that call to get_next with a response that has a 'next' links returns the
        next response on first yield.
        """
        initial_response = self.build_response_mock({'next': {'url': 'http://next/url/1'}})
        second_response = self.build_response_mock()
        mock_client_get.return_value = second_response

        result = next(utils.get_next(self.req_ctx, initial_response))
        self.assertEqual(
            result, second_response, "Result of get_next should be return value of client.get")

    @patch('canvas_sdk.utils.client.get')
    def test_get_next_for_response_with_a_next_link_stops_iterating_after_first_call(self, mock_client_get):
        """
        Assert that call to get_next with a response that has a 'next' links stops iteration on second iteration
        """
        initial_response = self.build_response_mock({'next': {'url': 'http://next/url/1'}})
        second_response = self.build_response_mock()
        mock_client_get.return_value = second_response

        result = next(utils.get_next(self.req_ctx, initial_response))
        with self.assertRaises(StopIteration):
            next(utils.get_next(self.req_ctx, result))

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_calls_function_parameter_with_context_args_and_kwargs(self, mock_next):
        """
        Assert that call to get_all_list_data calls function parameter with context, args, and kwargs
        """
        mock_next.return_value = iter([])
        mock_function = mock.Mock(name='mock-function')
        arg1, arg2 = 'arg1', 'arg2'
        kwargs = {'kwarg1': 'val1', 'kwarg2': 'val2'}

        utils.get_all_list_data(self.req_ctx, mock_function, arg1, arg2, **kwargs)
        mock_function.assert_called_once_with(self.req_ctx, arg1, arg2, **kwargs)

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_calls_json_on_function_return_value(self, mock_next):
        """
        Assert that call to get_all_list_data makes call to json method on result of function call
        """
        mock_next.return_value = iter([])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock()
        mock_function.return_value = mock_response

        utils.get_all_list_data(self.req_ctx, mock_function)
        mock_response.json.assert_called_once_with()

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_calls_get_next_with_request_context_and_response(self, mock_next):
        """
        Assert that call to get_all_list_data makes a call to get_next with context and function response
        """
        mock_next.return_value = iter([])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock()
        mock_function.return_value = mock_response

        utils.get_all_list_data(self.req_ctx, mock_function)
        mock_next.assert_called_once_with(self.req_ctx, mock_response)

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_returns_initial_response_json_when_response_has_no_paged_results(self, mock_next):
        """
        Assert that result of call to get_all_list_data for a request that's not a list and has no paged results returns
        the json response as is.
        """
        expected_json = {'first': 'json'}
        mock_next.return_value = iter([])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock(json_data=expected_json)
        mock_function.return_value = mock_response

        results = utils.get_all_list_data(self.req_ctx, mock_function)
        self.assertEqual(
            results, expected_json, "The json data returned by get_all function should match up with expected_json")

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_returns_initial_response_list_json_when_response_has_no_paged_results(self, mock_next):
        """
        Assert that result of call to get_all_list_data for a request that's a list of data and has no paged results returns
        the json list.
        """
        expected_json = [{'first': 'json'}]
        mock_next.return_value = iter([])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock(json_data=expected_json)
        mock_function.return_value = mock_response

        results = utils.get_all_list_data(self.req_ctx, mock_function)
        self.assertEqual(
            results, expected_json, "The json data returned by get_all function should match up with expected_json list")

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_raises_attribute_error_on_paged_results_if_initial_result_not_a_list(self, mock_next):
        """
        Assert that call to get_all_list_data will raise an AttributeError in the event that the initial response is something
        other than a list (i.e., a json string or dict)
        """
        # Simulate an initial response with 3 additional pages
        mock_next.return_value = iter([
            self.build_response_mock(json_data=['test-data']),
        ])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock(json_data={'dict': 'data'})
        mock_function.return_value = mock_response

        with self.assertRaises(AttributeError):
            utils.get_all_list_data(self.req_ctx, mock_function)

    @patch('canvas_sdk.utils.get_next')
    def test_get_all_list_data_returns_concatenated_list_of_json_results(self, mock_next):
        """
        Assert that result of call to get_all_list_data is a single concatenated list of json data from
        series of "next" responses.
        """
        expected_json = [
            {'first': 'json'}, {'second': 'json'}, {'third': 'json'}, {'fourth': 'json'}]
        # Simulate an initial response with 3 additional pages
        mock_next.return_value = iter([
            self.build_response_mock(json_data=[expected_json[1]]),
            self.build_response_mock(json_data=[expected_json[2]]),
            self.build_response_mock(json_data=[expected_json[3]]),
        ])
        mock_function = mock.Mock(name='mock-function')
        mock_response = self.build_response_mock(json_data=[expected_json[0]])
        mock_function.return_value = mock_response

        results = utils.get_all_list_data(self.req_ctx, mock_function)
        self.assertEqual(
            results, expected_json, "The json list of data returned by get_all function should be the fully concatenated list of json")

    def test_masquerade_returns_function_response(self):
        """
        Assert that result of call to masquerade is the API function response.
        """
        mock_function = mock.Mock(name='mock-function')
        results = utils.masquerade(self.req_ctx, mock_function, "test-user-id")
        self.assertEqual(
            results, mock_function.return_value, "Masquerading should return result of API method call")

    def test_masquerade_makes_function_call_with_context(self):
        """
        Assert that masquerade calls the API function with the request_context.
        """
        mock_function = mock.Mock(name='mock-function')
        utils.masquerade(self.req_ctx, mock_function, "test-user-id")
        mock_function.assert_called_once_with(self.req_ctx, params=mock.ANY)

    def test_masquerade_makes_function_call_with_user_id_params_kwarg(self):
        """
        Assert that masquerade adds a "params" keyword argument containing the 'as_user_id' parameter.
        """
        as_user_id = "test-user-id"
        mock_function = mock.Mock(name='mock-function')
        utils.masquerade(self.req_ctx, mock_function, as_user_id)
        mock_function.assert_called_once_with(mock.ANY, params={'as_user_id': as_user_id})

    def test_masquerade_makes_function_call_with_merged_user_id_params_kwarg(self):
        """
        Assert that masquerade will merge the 'as_user_id' parameter into an existing "params" kwarg
        that was passed in to the call.
        """
        params_kwarg = {'params': {'foo': 'bar'}}
        as_user_id = "test-user-id"
        mock_function = mock.Mock(name='mock-function')
        utils.masquerade(self.req_ctx, mock_function, as_user_id, **params_kwarg)
        mock_function.assert_called_once_with(mock.ANY, params={'as_user_id': as_user_id, 'foo': 'bar'})
