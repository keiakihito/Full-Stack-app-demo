from django.core.cache import cache
from app.dbmodels.models import Player as DjangoPlayer, PlayerStats, Shot, Game
from app.loaders.dataloader import DataLoaderPool
from app.classes import PlayerSummaryResponse, CustomGame, CustomShot

class PlayerHandler:
    CACHE_TIMEOUT = 60 * 15  # 15 minutes

    def get_player_summary(self, playerID):
        debug = False

        # Check if data is in cache
        cached_data = self._check_cache(playerID)
        if cached_data:
            return cached_data

        # Cache miss, proceed to load data from DataLoader
        if debug:
            print(f"Cache miss for playerID: {playerID}. Loading from database.")

        # Instantiate the DataLoader to fetch data
        data_loader = DataLoaderPool.get_loader()

        try:
            # Fetch basic player data (from the database using Django model)
            player_data = data_loader.get_player_data(playerID)[0]  # Fetch first player entry

            if debug:
                print(f"Player Name: {player_data['name']}")

            # Create CustomGame instances with player stats and shots
            player_games = self._create_player_games(playerID, data_loader)

            # Create the player summary response
            # player_summary = PlayerSummaryResponse(player_data['name'], player_games)
            player_summary = PlayerSummaryResponse(player_data['name'])
            player_summary.add_sub_entity(player_games)

            # Convert the player summary response to a dictionary
            response_dict = player_summary.to_dict()

            # Store the result in cache before returning it
            cache_key = f"player_summary_{playerID}"
            cache.set(cache_key, response_dict, timeout=self.CACHE_TIMEOUT)

            if debug:
                print(f"Cached Response Dict: {response_dict}")

            return response_dict
        finally:
            # Return DataLoader to the pool after use
            DataLoaderPool.return_loader(data_loader)

    def _check_cache(self, playerID):
        """
        Check if the player summary is in the cache.
        """
        debug = False
        cache_key = f"player_summary_{playerID}"
        cached_data = cache.get(cache_key)
        if cached_data:
            if debug:
                print(f"Cache hit for playerID: {playerID}")
            return cached_data
        return None

    def _create_player_games(self, playerID, data_loader):
        """
        Fetch player stats and create CustomGame objects for each game the player participated in.
        """
        # Fetch player stats (from the database)
        player_stats = data_loader.get_player_stats_data(playerID)

        # Create CustomGame instances with player stats and shots
        player_games = []
        for stats in player_stats:
            game_id = stats.get('game_id')

            # Fetch game data using game_id
            game_data = data_loader.get_participated_game(game_id)[0]

            # Create a game object and add shots
            custom_game = self._create_game(game_data.get('date'), stats, data_loader)
            player_games.append(custom_game)

        return player_games

    def _create_game(self, date, stats, data_loader):
        """
        Create a CustomGame object and add the associated shot data.
        """
        debug = False

        # Create a CustomGame object
        custom_game = CustomGame(
            date=date,  # Game date is passed as a parameter
            player_stats=stats  # Player stats passed to the CustomGame constructor
        )

        # Fetch shots for the game
        shots = data_loader.get_player_shots_in_a_game(stats['player_stats_id'])
        if debug:
            print(f"Shots data being processed: {shots}")

        # Add shots to the game object
        custom_game.add_sub_entity([CustomShot(shot) for shot in shots])

        return custom_game
