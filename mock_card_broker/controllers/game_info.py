from flask import request

def get_player_state(playerId):
    pass

def check_card_supply():

    request_data = request.get_json()
    if request_data['cardId'] % 2 > 0:
        return {'cardId': request_data['cardId'], 'gameId': 1337, 'suppply': 10 }
    else:
        return {'cardId': request_data['cardId'], 'gameId': 1337, 'suppply': 0 }

def get_game_cards(gameId):
    """
    retrieve and return card state for given gameId
    """
    pass
