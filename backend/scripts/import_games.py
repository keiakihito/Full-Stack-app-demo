import json
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.dbmodels.models import Game, Team, Player, PlayerStats, Shot  # Import the relevant models


# Function to insert games and player stats from JSON
def load_games():
    with open("../raw_data/games.json", "r") as f:
        games_data = json.load(f)

    for game_data in games_data:
        game_id = game_data['id']
        home_team_id = game_data['homeTeam']['id']
        away_team_id = game_data['awayTeam']['id']
        date = game_data['date']

        # Get or create the home and away teams
        home_team, created = Team.objects.get_or_create(team_id=home_team_id)
        away_team, created = Team.objects.get_or_create(team_id=away_team_id)

        # Insert game into the database using Django ORM
        game, created = Game.objects.get_or_create(
            game_id=game_id,
            home_team=home_team,
            away_team=away_team,
            date=date
        )

        # Insert player stats for the home team
        for player_data in game_data['homeTeam']['players']:
            insert_player_stats(player_data, game, home_team)

        # Insert player stats for the away team
        for player_data in game_data['awayTeam']['players']:
            insert_player_stats(player_data, game, away_team)

    print("Game, player stats, and shots imported successfully.")


# Insert Player Stats Data using Django ORM
def insert_player_stats(player_data, game, team):
    player_id = player_data['id']

    # Get or create the player, but don't overwrite existing names if they are present
    player, created = Player.objects.get_or_create(player_id=player_id)

    # Update player's team if not assigned or if the current team is different
    if player.team != team:
        player.team = team
        player.save()

    # Insert player stats into the database using Django ORM
    player_stats, created = PlayerStats.objects.get_or_create(
        player=player,
        game=game,
        is_starter=player_data['isStarter'],
        minutes=player_data['minutes'],
        points=player_data['points'],
        assists=player_data['assists'],
        offensive_rebounds=player_data['offensiveRebounds'],
        defensive_rebounds=player_data['defensiveRebounds'],
        steals=player_data['steals'],
        blocks=player_data['blocks'],
        turnovers=player_data['turnovers'],
        defensive_fouls=player_data['defensiveFouls'],
        offensive_fouls=player_data['offensiveFouls'],
        free_throws_made=player_data['freeThrowsMade'],
        free_throws_attempted=player_data['freeThrowsAttempted'],
        two_pointers_made=player_data['twoPointersMade'],
        two_pointers_attempted=player_data['twoPointersAttempted'],
        three_pointers_made=player_data['threePointersMade'],
        three_pointers_attempted=player_data['threePointersAttempted'],
    )

    # Insert shots if any
    if 'shots' in player_data:
        insert_shots(player_data['shots'], player, player_stats)


# Insert Shot Data using Django ORM
def insert_shots(shots_data, player, player_stats):
    for shot_data in shots_data:
        Shot.objects.create(
            player_stats=player_stats,
            is_make=shot_data['isMake'],
            location_x=shot_data['locationX'],
            location_y=shot_data['locationY'],
        )


# Main function to run the script
def main():
    load_games()


if __name__ == "__main__":
    main()
