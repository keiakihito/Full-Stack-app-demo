# dataloader.py
from app.dbmodels.models import Player, PlayerStats, Shot, Game

class DataLoader:
    def get_player_data(self, playerID):
        """Fetch player data by player ID."""
        return Player.objects.filter(player_id=playerID).values()

    def get_player_stats_data(self, playerID):
        """Fetch player stats using the correct foreign key lookup."""
        return PlayerStats.objects.filter(player__player_id=playerID).values()

    def get_player_shots_in_a_game(self, playerStatsID):
        """Fetch shots using the correct foreign key lookup."""
        return Shot.objects.filter(player_stats__player_stats_id=playerStatsID).values()

    def get_participated_game(self, gameID):
        """Fetch game details."""
        return Game.objects.filter(game_id=gameID).values()


class DataLoaderPool:
    """Manages a pool of reusable DataLoader objects to optimize performance."""

    _pool = []

    @classmethod
    def get_loader(cls):
        """Retrieve a DataLoader instance from the pool or create a new one."""
        # _pool is shared list
        return cls._pool.pop() if cls._pool else DataLoader()

    @classmethod
    def return_loader(cls, loader):
        """Return a DataLoader instance to the pool for reuse."""
        cls._pool.append(loader)