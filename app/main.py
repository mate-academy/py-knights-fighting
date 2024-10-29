from app.battle.battle import knights_battle
from app.battle.preparation import battle_preparation
from app.constants.knights import KNIGHTS


def battle(knights: dict) -> dict:
    # lancelot
    lancelot = knights["lancelot"]
    battle_preparation(lancelot)

    # arthur
    arthur = knights["arthur"]
    battle_preparation(arthur)

    # mordred
    mordred = knights["mordred"]
    battle_preparation(mordred)

    # red_knight
    red_knight = knights["red_knight"]
    battle_preparation(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_mordred = knights_battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    arthur_red_knight = knights_battle(arthur, red_knight)

    return {
        **lancelot_mordred,
        **arthur_red_knight
    }


print(battle(KNIGHTS))
