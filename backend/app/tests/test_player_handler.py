import unittest
from unittest.mock import patch, MagicMock
from app.handler.player_handler import PlayerHandler


class PlayerHandlerTest(unittest.TestCase):

    def setUp(self):
        # Set up the handler instance
        self.handler = PlayerHandler()

        # Mock data to simulate what DataLoader would return
        self.mock_player_data = [{
            'player_id': 1,
            'name': 'Michael Jordan',
            'team_id': 23
        }]
        self.mock_player_stats_data = [
            {'player_stats_id': 101, 'minutes': 38, 'points': 28, 'assists': 6, 'game_id': 201}
        ]
        self.mock_game_data = [{'game_id': 201, 'date': '2022-12-19', 'home_team_id': 23, 'away_team_id': 24}]
        self.mock_shots_data = [{'isMake': True, 'locationX': -22.4, 'locationY': 11.5}]

    @patch('app.handler.player_handler.DataLoader')
    def test_get_player_summary(self, MockDataLoader):
        # Set up the mock DataLoader
        mock_loader = MockDataLoader.return_value
        mock_loader.get_player_data.return_value = self.mock_player_data
        mock_loader.get_player_stats_data.return_value = self.mock_player_stats_data
        mock_loader.get_participated_game.return_value = self.mock_game_data
        mock_loader.get_player_shots_in_a_game.return_value = self.mock_shots_data

        # Call the method under test
        result = self.handler.get_player_summary(1)

        # Assertions
        self.assertEqual(result['name'], 'Michael Jordan')
        self.assertEqual(result['player_id'], 1)
        self.assertEqual(len(result['games']), 1)
        self.assertEqual(result['games'][0]['player_stats'][0]['points'], 28)


if __name__ == '__main__':
    unittest.main()
