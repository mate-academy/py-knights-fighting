from app.config.config import battle_queue
from app.game.knight import Knight
from app.game.battle import Battle


def battle(knights_config: dict) -> dict:

    knights_recalculated = {
        label: Knight(obj)
        for label, obj in knights_config.items()
    }

    result: dict = {}  # result dict for merge here

    for label1, label2 in battle_queue:
        # participant 1
        knight1 = knights_recalculated[label1]
        # participant 2
        knight2 = knights_recalculated[label2]

        # === Battle === #
        battle_result = Battle(knight1, knight2).fight()

        # merging to common result dict
        result = result | battle_result

    return result
