import logging

from flask import request
from flask_api import status

from card_broker.exceptions.card_broker_exceptions import GameDeckEmpty
from card_broker.models.game_state_proxy import GameStateProxy
from card_broker.models.player_state_proxy import PlayerStateProxy

logger = logging.getLogger('card_broker')

def acquire_card():
    return status.HTTP_200_OK

def discard_player_hand():
    return status.HTTP_200_OK

def draw_player_hand():
    return status.HTTP_200_OK

def draw_player_card(playerId):
    return status.HTTP_200_OK

def discard_player_card():
    return status.HTTP_200_OK
def trash_player_card():
    return status.HTTP_200_OK
