from unittest import mock
import random
import unittest
import uuid

from canvas_sdk.client import RequestContext
from canvas_sdk.methods import modules


class TestModules(unittest.TestCase):
    '''
    Exercises all hand-edited methods in the modules module, specifically
    the parts that needed hand-editing in the first place.
    '''
    def setUp(self):
        self.base_api_url = 'http://example.org/api/{}'.format(uuid.uuid4().hex)
        self.request_context = mock.MagicMock(spec=RequestContext,
                                              base_api_url=self.base_api_url)
        self.content_id = uuid.uuid4().hex
        self.course_id = uuid.uuid4().hex
        self.min_score = random.randint(0,100)
        self.module_id = uuid.uuid4().hex
        self.position = random.randint(0,100)
        self.title = uuid.uuid4().hex
        self.url = 'http://example.org/{}'.format(uuid.uuid4().hex)

    @mock.patch('canvas_sdk.methods.modules.client.post')
    def test_create_module_item_external_tool(self, mock_client_post):
        ''' arguments taken from tlt-1641 '''
        response = modules.create_module_item(
                       self.request_context, self.course_id,
                       self.module_id, 'ExternalTool', self.content_id,
                       module_item_external_url=self.url,
                       module_item_title=self.title,
                       module_item_position=self.position)
        self.assertTrue(mock_client_post.called)
        self.assertDictContainsSubset(
            {'module_item[completion_requirement][type]': None,
             'module_item[completion_requirement][min_score]': None},
            mock_client_post.call_args[1]['payload'])

    @mock.patch('canvas_sdk.methods.modules.client.post')
    def test_create_module_item_assignment(self, mock_client_post):
        ''' arguments taken from tlt-1641 '''
        response = modules.create_module_item(
                       self.request_context, self.course_id,
                       self.module_id, 'Assignment', self.content_id,
                       module_item_title=self.title,
                       module_item_position=self.position)
        self.assertTrue(mock_client_post.called)
        self.assertDictContainsSubset(
            {'module_item[completion_requirement][type]': None,
             'module_item[completion_requirement][min_score]': None},
            mock_client_post.call_args[1]['payload'])

    @mock.patch('canvas_sdk.methods.modules.client.post')
    def test_create_module_item_completion_requirement_type_is_min_score(self, mock_client_post):
        ''' verifies that completion_requirement_type=min_score is usable '''
        response = modules.create_module_item(
                       self.request_context, self.course_id,
                       self.module_id, 'ExternalTool', self.content_id,
                       module_item_completion_requirement_min_score=self.min_score,
                       module_item_completion_requirement_type='min_score',
                       module_item_external_url=self.url,
                       module_item_position=self.position,
                       module_item_title=self.title)
        self.assertTrue(mock_client_post.called)
        self.assertDictContainsSubset(
            {'module_item[completion_requirement][type]': 'min_score',
             'module_item[completion_requirement][min_score]': self.min_score},
            mock_client_post.call_args[1]['payload'])

    def test_create_module_item_external_url_required(self):
        ''' module_item_external_url is required if type='ExternalTool' '''
        with self.assertRaises(ValueError):
            response = modules.create_module_item(
                           self.request_context, self.course_id,
                           self.module_id, 'ExternalTool', self.content_id,
                           module_item_title=self.title,
                           module_item_position=self.position)

    def test_create_module_item_min_score_required(self):
        ''' module_item_completion_requirement_min_score is required if
            module_item_completion_requirement_type='ExternalTool' '''
        with self.assertRaises(ValueError):
            response = modules.create_module_item(
                           self.request_context, self.course_id,
                           self.module_id, 'ExternalTool', self.content_id,
                           module_item_completion_requirement_type='min_score',
                           module_item_external_url=self.url,
                           module_item_position=self.position,
                           module_item_title=self.title)
