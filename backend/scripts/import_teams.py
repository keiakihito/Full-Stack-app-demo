import json
import os
import sys

import django

# Add the project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from app.dbmodels.models import Team

# Load teams from JSON file
def load_teams():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Gets the backend/ directory
    TEAMS_DATA_PATH = os.path.join(BASE_DIR, "raw_data", "teams.json")

    print("📂 Looking for file at:", TEAMS_DATA_PATH)  # Debugging
    with open(TEAMS_DATA_PATH, "r") as f:
        teams_data = json.load(f)

    for team in teams_data:
        team_id = team['id']
        name = team['name']

        # Check if the team already exists in the database to avoid duplicates
        existing_team = Team.objects.filter(team_id=team_id).first()

        if not existing_team:
            # Create new team
            Team.objects.create(team_id=team_id, name=name)
            print(f"Team {name} inserted successfully.")
        else:
            print(f"Team {name} already exists.")

# Main function
if __name__ == "__main__":
    load_teams()