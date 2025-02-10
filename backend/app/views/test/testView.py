#For test
from app.loaders.dataloader import DataLoader
from app.dbmodels.models import Player
from app.classes.PlayerSummaryResponse import PlayerSummaryResponse
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response

from app.handler.player_handler import PlayerHandler

# class PlayerDataTestView(APIView):
#     def get(self, request, playerID):
#         # Instantiate the handler
#         handler = PlayerHandler()
#
#         # Fetch player summary using the PlayerHandler
#         player_summary = handler.get_player_summary(playerID)
#
#         # Prepare the data for the response (convert player object to dictionary)
#         player_data = {
#             'player_id': player_summary.player_id,
#             'name': player_summary.name,
#             'team_id': player_summary.team_id,
#             'games': []
#         }
#
#         # Add games and associated stats/shots to the player data
#         for game in player_summary.games:
#             game_data = {
#                 'game_id': game.game_id,
#                 'date': game.date,
#                 'home_team_id': game.home_team_id,
#                 'away_team_id': game.away_team_id,
#                 'player_stats': []
#             }
#
#             # Add player stats for each game
#             for stats in game.player_stats:
#                 stats_data = {
#                     'is_starter': stats.is_starter,
#                     'minutes': stats.minutes,
#                     'points': stats.points,
#                     'assists': stats.assists,
#                     'offensive_rebounds': stats.offensive_rebounds,
#                     'defensive_rebounds': stats.defensive_rebounds,
#                     'steals': stats.steals,
#                     'blocks': stats.blocks,
#                     'turnovers': stats.turnovers,
#                     'defensive_fouls': stats.defensive_fouls,
#                     'offensive_fouls': stats.offensive_fouls,
#                     'free_throws_made': stats.free_throws_made,
#                     'free_throws_attempted': stats.free_throws_attempted,
#                     'two_pointers_made': stats.two_pointers_made,
#                     'two_pointers_attempted': stats.two_pointers_attempted,
#                     'three_pointers_made': stats.three_pointers_made,
#                     'three_pointers_attempted': stats.three_pointers_attempted,
#                     'shots': []
#                 }
#
#                 # Add shots for each player stats
#                 for shot in stats.shots:
#                     shot_data = {
#                         'is_make': shot.is_make,
#                         'location_x': shot.location_x,
#                         'location_y': shot.location_y
#                     }
#                     stats_data['shots'].append(shot_data)
#
#                 game_data['player_stats'].append(stats_data)
#
#             player_data['games'].append(game_data)
#
#         # Return the player data as a JSON response
#         return Response(player_data)



class PlayerDataTestView(APIView):
    def get(self, request, playerID):
        # Instantiate the handler
        handler = PlayerHandler()

        # Fetch player summary using the PlayerHandler
        player_summary = handler.get_player_summary(playerID)

        # Return the player summary as a JSON response
        return Response(player_summary)