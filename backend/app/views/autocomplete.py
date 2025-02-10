# autocomplete.py
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from app.handler.autocomplete_handler import AutocompleteHandler

LOGGER = logging.getLogger('django')

class Autocomplete(APIView):
    logger = LOGGER

    def get(self, request, query):
        """Controller for handling autocomplete requests."""
        handler = AutocompleteHandler()
        suggestions = handler.get_player_suggestions(query)
        self.logger.debug(f"Fetched autocomplete suggestions for query '{query}': {suggestions}")
        return Response(suggestions)
