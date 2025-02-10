from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse

class PlayerDataTestViewTest(TestCase):

    @patch('app.views.test.testView.PlayerHandler')
    def test_player_data_view(self, MockPlayerHandler):
        # Setup mock player data response
        mock_handler = MockPlayerHandler.return_value
        mock_handler.get_player_summary.return_value = {
            'player_id': 1,
            'name': 'Michael Jordan',
            'team_id': 23,
            'games': []
        }

        # Perform GET request to the view
        response = self.client.get(reverse('player-data-test', kwargs={'playerID': 1}))

        # Verify the response status and content
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            'player_id': 1,
            'name': 'Michael Jordan',
            'team_id': 23,
            'games': []
        })

