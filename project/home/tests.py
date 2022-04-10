from unittest import mock
from unittest.mock import Mock

from django.test import TestCase


class HomeTestCase(TestCase):

    @mock.patch('home.tasks.run_task.delay')
    def test_home_response(self, mocked_run_task):
        # Given.
        task_response = Mock()
        task_response.get.return_value = 'Hey! You!'
        mocked_run_task.return_value = task_response

        # When.
        response = self.client.get("/")

        # Then.
        self.assertEqual(response.json(), {"msg": "Home is where your heart is.",
                                           "response": "Hey! You!"})
        mocked_run_task.assert_called()
        task_response.get.assert_called()

        # @NOTE: I tested if the response is ok, and if testing worked.
        # The last two assertions tell about the limit of unit testing:
        #   they don't proof that the system as a whole works.
        # Functional testing with selenium or at least manual testing
        #   remains relevant.
