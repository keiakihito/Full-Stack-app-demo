from app.classes.CustomEntity import CustomEntity
from app.classes.CustomGame import CustomGame


class PlayerSummaryResponse(CustomEntity):
    def __init__(self, name, custom_games=None):
        self.name = name
        # Initialize with custom_games if provided
        self.games = custom_games if custom_games is not None else []


    def add_sub_entity(self,custom_games):
        """Assig    n game data to PlayerSummaryResponse object"""
        if all(isinstance(game, CustomGame) for game in custom_games):
            self.games.extend(custom_games)
        else:
            raise ValueError("All items in custom_games must be instances of CustomGame.")

    def to_dict(self):
        return {
            'name': self.name,
            'games': [game.to_dict() for game in self.games]  # Convert games to dictionary
        }