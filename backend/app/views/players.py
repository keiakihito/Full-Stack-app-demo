# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
# Calling importing PlaherHandler to handle backend logic
from app.handler.player_handler import PlayerHandler

LOGGER = logging.getLogger('django')


class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data"""
        # Instantiate the PlayerHandler
        handler = PlayerHandler()

        # Fetch player summary using the handler
        player_summary = handler.get_player_summary(playerID)

        # Return the response as a JSON object
        return Response(player_summary)







