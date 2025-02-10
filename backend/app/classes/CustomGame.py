# from app.classes import CustomShot # this path does not work I don't know why
from app.classes.CustomEntity import CustomEntity
from app.classes.CustomShot import CustomShot # It works even though, I set up __it__.py in classes direct correctly.

class CustomGame(CustomEntity):
    def __init__(self, date, player_stats):
        self.date = date
        self.is_starter = player_stats.get('is_starter', False)  # Using .get() to handle missing fields gracefully
        self.minutes = player_stats.get('minutes', 0)
        self.points = player_stats.get('points', 0)
        self.assists = player_stats.get('assists', 0)
        self.offensive_rebounds = player_stats.get('offensive_rebounds', 0)
        self.defensive_rebounds = player_stats.get('defensive_rebounds', 0)
        self.steals = player_stats.get('steals', 0)
        self.blocks = player_stats.get('blocks', 0)
        self.turnovers = player_stats.get('turnovers', 0)
        self.defensive_fouls = player_stats.get('defensive_fouls', 0)
        self.offensive_fouls = player_stats.get('offensive_fouls', 0)
        self.free_throws_made = player_stats.get('free_throws_made', 0)
        self.free_throws_attempted = player_stats.get('free_throws_attempted', 0)
        self.two_pointers_made = player_stats.get('two_pointers_made', 0)
        self.two_pointers_attempted = player_stats.get('two_pointers_attempted', 0)
        self.three_pointers_made = player_stats.get('three_pointers_made', 0)
        self.three_pointers_attempted = player_stats.get('three_pointers_attempted', 0)
        self.shots = []  # The custom shots will be added later via another method

    def add_sub_entity(self, custom_shots):

        # Explicitly check if all elements in custom_shots are instances of CustomShot
        try:
            if all(isinstance(shot, CustomShot) for shot in custom_shots):
                self.shots.extend(custom_shots)
                print(f"After extend, self.shots: {self.shots}")  # Check if the shots were added
            else:
                raise ValueError("All items in custom_shots must be instances of CustomShot.")
        except Exception as e:
            print(f"Error in validation: {e}")





    def to_dict(self):
        """ Convert the CustomGame object to a dictionary """
        return {
            'date': self.date,
            'is_starter': self.is_starter,
            'minutes': self.minutes,
            'points': self.points,
            'assists': self.assists,
            'offensive_rebounds': self.offensive_rebounds,
            'defensive_rebounds': self.defensive_rebounds,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'defensive_fouls': self.defensive_fouls,
            'offensive_fouls': self.offensive_fouls,
            'free_throws_made': self.free_throws_made,
            'free_throws_attempted': self.free_throws_attempted,
            'two_pointers_made': self.two_pointers_made,
            'two_pointers_attempted': self.two_pointers_attempted,
            'three_pointers_made': self.three_pointers_made,
            'three_pointers_attempted': self.three_pointers_attempted,
            'shots': [shot.to_dict() for shot in self.shots]  # Assuming `shots` are instances of a `CustomShot` class
        }
