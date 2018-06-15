
from flask import request
from flask_api import status

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

def curse_players():
    return status.HTTP_200_OK
