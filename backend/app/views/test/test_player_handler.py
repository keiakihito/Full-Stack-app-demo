import unittest
from unittest.mock import patch, MagicMock
from app.handler.player_handler import PlayerHandler
from app.classes.Player import Player
from app.classes.Game import Game
from app.classes.PlayerStats import PlayerStats
from app.classes.Shot import Shot

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
            {'player_stats_id': 101, 'isStarter': True, 'minutes': 38, 'points': 28, 'assists': 6,
             'offensive_rebounds': 0, 'defensive_rebounds': 3, 'steals': 1, 'blocks': 0, 'turnovers': 4,
             'defensive_fouls': 4, 'offensive_fouls': 0, 'free_throws_made': 4, 'free_throws_attempted': 4,
             'two_pointers_made': 3, 'two_pointers_attempted': 5, 'three_pointers_made': 6, 'three_pointers_attempted': 12,
             'game_id': 201}
        ]

        self.mock_game_data = [{
            'game_id': 201, 'date': '2022-12-19', 'home_team_id': 23, 'away_team_id': 24
        }]

        self.mock_shots_data = [
            {'is_make': True, 'location_x': -22.4, 'location_y': 11.5},
            {'is_make': False, 'location_x': 1.0, 'location_y': -0.8}
        ]

    def print_player_summary(player):
        print(f"Player: {player.name}, Team: {player.team}, Games: {len(player.games)}")

        for game in player.games:
            print(f"\nGame ID: {game.game_id}, Date: {game.date}, Home: {game.home_team_id}, Away: {game.away_team_id}")
            print(f"Player Stats for the Game (Total: {len(game.player_stats)}):")

            for stats in game.player_stats:
                print(
                    f"  Stats ID: {stats.player_stats_id}, Points: {stats.points}, Assists: {stats.assists}, Minutes: {stats.minutes}")
                print(f"  Shots (Total: {len(stats.shots)}):")
                for shot in stats.shots:
                    print(
                        f"    Shot: {'Made' if shot.is_make else 'Missed'}, Location: ({shot.location_x}, {shot.location_y})")

    @patch('app.handler.player_handler.DataLoader')  # Mock DataLoader in PlayerHandler
    def test_get_player_summary(self, MockDataLoader):
        debug =False
        # Set up the mock DataLoader
        mock_loader = MockDataLoader.return_value
        mock_loader.get_player_data.return_value = self.mock_player_data
        mock_loader.get_player_stats_data.return_value = self.mock_player_stats_data
        mock_loader.get_participated_game.return_value = self.mock_game_data
        mock_loader.get_player_shots_in_a_game.return_value = self.mock_shots_data

        # Call the method under test
        result = self.handler.get_player_summary(1)
        if(debug):
            print(result)

        # Assertions to verify behavior
        self.assertEqual(result.name, 'Michael Jordan')
        self.assertEqual(result.player_id, 1)
        self.assertEqual(len(result.games), 1)

        # Check that the game has the right date
        game = result.games[0]
        self.assertEqual(game.date, '2022-12-19')
        self.assertEqual(len(game.player_stats), 1)

        # Check player stats
        player_stats = game.player_stats[0]
        self.assertEqual(player_stats.points, 28)
        self.assertEqual(player_stats.assists, 6)
        self.assertEqual(len(player_stats.shots), 2)

        # Check the shots
        shot = player_stats.shots[0]
        self.assertTrue(shot.is_make)
        self.assertEqual(shot.location_x, -22.4)
        self.assertEqual(shot.location_y, 11.5)

        # Ensure DataLoader methods were called the correct number of times
        mock_loader.get_player_data.assert_called_once_with(1)
        mock_loader.get_player_stats_data.assert_called_once_with(1)
        mock_loader.get_participated_game.assert_called_once_with(201)
        mock_loader.get_player_shots_in_a_game.assert_called_once_with(101)

    @patch('app.handler.player_handler.DataLoader')  # Mock DataLoader in PlayerHandler
    def test_cache_functionality(self, MockDataLoader):
        debug = False

        # Set up the mock DataLoader
        mock_loader = MockDataLoader.return_value
        mock_loader.get_player_data.return_value = self.mock_player_data
        mock_loader.get_player_stats_data.return_value = self.mock_player_stats_data
        mock_loader.get_participated_game.return_value = self.mock_game_data
        mock_loader.get_player_shots_in_a_game.return_value = self.mock_shots_data

        # Call the method once to cache the result
        self.handler.get_player_summary(1)

        # Call the method again to ensure it retrieves from cache
        result = self.handler.get_player_summary(1)


        # Ensure DataLoader methods were only called once
        mock_loader.get_player_data.assert_called_once()
        mock_loader.get_player_stats_data.assert_called_once()
        mock_loader.get_participated_game.assert_called_once()
        mock_loader.get_player_shots_in_a_game.assert_called_once()

        # Verify the result still matches the expected structure
        self.assertEqual(result.name, 'Michael Jordan')
        self.assertEqual(len(result.games), 1)




if __name__ == '__main__':
    unittest.main()
