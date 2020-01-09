from unittest import mock
import random
import unittest
import uuid

from canvas_sdk.client import RequestContext
from canvas_sdk.methods import assignments


class TestAssignments(unittest.TestCase):
    '''
    Exercises all hand-edited methods in the assignments module, specifically
    the parts that needed hand-editing in the first place.
    '''
    def setUp(self):
        self.base_api_url = 'http://example.org/api/{}'.format(uuid.uuid4().hex)
        self.request_context = mock.MagicMock(spec=RequestContext,
                                              base_api_url=self.base_api_url)
        self.assignment_name = uuid.uuid4().hex
        self.course_id = uuid.uuid4().hex
        self.integration_id = uuid.uuid4().hex
        self.points_possible = random.randint(1,100)
        self.url = 'http://example.org/{}'.format(uuid.uuid4().hex)

    @mock.patch('canvas_sdk.methods.assignments.client.post')
    def test_create_assignment_external_tool(self, mock_client_post):
        response = assignments.create_assignment(
                       self.request_context, self.course_id,
                       self.assignment_name, 'external_tool',
                       assignment_external_tool_tag_attributes = {
                           'url': self.url},
                       assignment_integration_id=self.integration_id,
                       assignment_points_possible=self.points_possible)
        self.assertTrue(mock_client_post.called)
        assert (
            set({
                'assignment[external_tool_tag_attributes][url]': self.url,
                'assignment[submission_types][]': 'external_tool'
            }.items()) <=
            set(mock_client_post.call_args[1]['payload'].items())
        )
