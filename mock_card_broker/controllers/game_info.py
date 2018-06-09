from flask import request

def get_player_state(playerId):
    pass

def check_card_supply(gameId, cardId):

    if (cardId % 2) > 0:
        return {'cardId': cardId, 'gameId': 1337, 'supply': 10 }
    else:
        return {'cardId': cardId, 'gameId': 1337, 'supply': 0 }

def get_game_cards(gameId):
    """
    retrieve and return card state for given gameId
    """
    pass

def get_game_trash():
    pass
