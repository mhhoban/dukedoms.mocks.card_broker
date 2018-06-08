import logging

from flask import request
from flask_api import status
from sqlalchemy.exc import SQLAlchemyError

from card_broker.models.game_state import GameState
from card_broker.models.player_state import PlayerState

from card_broker.shared.card_operations.initial_game_state import (
    create_initial_game_state,
    create_initial_player_state
)
from card_broker.shared.db import get_new_db_session
from card_broker.shared.card_service_calls import get_card_list

logger = logging.getLogger('card_broker')

def new_game():
    """
    handles request to create new game
    """
    request_data = request.get_json()
    game_id = request_data['gameId']

    card_list = get_card_list(game_id)

    initial_state = create_initial_game_state(card_list)

    new_game = GameState(game_id=game_id, card_state=initial_state)

    new_players = [
        PlayerState(
            player_id=player,
            game_id=game_id,
            card_state=create_initial_player_state(card_list)
        ) for player in request_data['players']
    ]

    session = get_new_db_session()
    session.add(new_game)

    for player in new_players:
        session.add(player)


    try:
        session.commit()
        logger.debug(
            'successfully created new game state for game id {}'.format(
                game_id
            )
        )
        return status.HTTP_200_OK
    except SQLAlchemyError:
        logger.error(
            'SQLAlchemyError while attempting game state creation for game id {}'.format(
                game_id
            )
        )
        return status.HTTP_500_INTERNAL_SERVER_ERROR

    finally:
        session.close()
