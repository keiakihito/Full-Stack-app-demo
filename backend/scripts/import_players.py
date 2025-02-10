import json
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.dbmodels.models import Player  # Import Player model

def load_players():
    """Load players from the players.json file and insert them into the database."""
    with open("../raw_data/players.json", "r") as f:
        players_data = json.load(f)

    for player in players_data:
        player_id = player['id']
        name = player['name']

        # Check if the player already exists
        existing_player = Player.objects.filter(player_id=player_id).first()

        if not existing_player:
            # Create new player if not already in the database
            Player.objects.create(player_id=player_id, name=name)
            print(f"Player {name} inserted successfully.")
        else:
            print(f"Player {name} already exists.")

# Main function to run the script
def main():
    load_players()

if __name__ == "__main__":
    main()
