from app.knights.knights_list import KNIGHTS
from app.prepering_to_battle import build_knight


def battle(knights_config: dict) -> dict:
    fighters = {
        knight: build_knight(knight, knights_config)
        for knight in ["lancelot", "mordred", "arthur", "red_knight"]
    }
    for knight in fighters.values():
        knight.preparing_to_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:
    fights = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for a_key, b_key in fights:
        attacker = fighters[a_key]
        defender = fighters[b_key]
        attacker.duel(defender)
    # Return battle results:
    return {knight.name: knight.hp for knight in fighters.values()}


print(battle(KNIGHTS))
