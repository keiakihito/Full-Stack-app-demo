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
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PLAYERS_DATA_PATH = os.path.join(BASE_DIR, "raw_data", "players.json")

    with open(PLAYERS_DATA_PATH, "r") as f:
        players_data = json.load(f)

    for player in players_data:
        player_id = player.get('id')
        name = player.get('name', 'UNKNOWN')  # Default to 'UNKNOWN' if missing
        team_id = player.get('teamId')

        print(f"🔍 Processing Player: ID={player_id}, Name={name}, Team={team_id}")

        existing_player = Player.objects.filter(player_id=player_id).first()

        if not existing_player:
            Player.objects.create(player_id=player_id, name=name, team_id=team_id)
            print(f"✅ Player {name} inserted successfully.")
        else:
            # Force update the name in case it's missing
            if not existing_player.name:
                existing_player.name = name
                existing_player.save()
                print(f"🔄 Updated player {name} with missing name.")
            else:
                print(f"⚠️ Player {name} already exists.")

# Main function to run the script
def main():
    load_players()

if __name__ == "__main__":
    main()
