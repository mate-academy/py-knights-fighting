from app.knights import KNIGHTS
import app.preparation as preparation
import app.fight as fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    prepared_knights = preparation.battle_preparation(knights_config)
    lancelot = prepared_knights["lancelot"]
    mordred = prepared_knights["mordred"]
    arthur = prepared_knights["arthur"]
    red_knight = prepared_knights["red_knight"]
    # -------------------------------------------------------------------------------
    # BATTLE:

    return fight.rounds(lancelot, mordred, arthur, red_knight)


print(battle(KNIGHTS))
