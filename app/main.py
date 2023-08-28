from app.battle.knights import KNIGHTS
from app.battle.knights_gear import knights_gear


def battle(knights: dict) -> dict:
    result = {}
    knights_dict = knights_gear(knights)
    fight1 = knights_dict["Lancelot"].battle_prep(knights_dict["Mordred"])
    fight2 = knights_dict["Arthur"].battle_prep(knights_dict["Red Knight"])
    result.update(**fight2, **fight1)
    return result


print(battle(KNIGHTS))
