# dataloader.py
from app.dbmodels.models import Player, PlayerStats, Shot, Game

class DataLoader:
    def get_player_data(self, playerID):
        # Query the database for player info
        return Player.objects.filter(player_id=playerID).values()  # Use `id` if `player_id` does not exist

    def get_player_stats_data(self, playerID):
        # Query the database for player stats
        return PlayerStats.objects.filter(player_id=playerID).values()

    def get_player_shots_in_a_game(self, playerStatsID):
        # Query the database for shots in a specific game for a single player
        return Shot.objects.filter(player_stats_id=playerStatsID).values()

    def get_participated_game(self, gameID):
        # Query the database for game in which a single player participated
        return Game.objects.filter(game_id=gameID).values()
