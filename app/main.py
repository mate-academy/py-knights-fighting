from app.data import KNIGHTS
from app.participants.knight import Knight
from app.battle.battle_preparation import prepare_the_knight
from app.battle.battle import battle


def tournament(knights_config: dict) -> dict:
    participants = {}
    # create knights
    for knight in knights_config:
        participants[knight] = Knight(knights_config[knight])
    # preparing knights to the battle
    for knight in participants.values():
        prepare_the_knight(knight)
    # battles
    battle([participants["lancelot"], participants["mordred"]],
           [participants["arthur"], participants["red_knight"]])

    return {participant.name: participant.hp
            for participant in participants.values()}


print(tournament(KNIGHTS))
