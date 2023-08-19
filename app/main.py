from app.store import KNIGHTS
from app.khights_batle.knights_constructor import knights_constructor


def battle(knights: {dict}) -> dict:
    result = {}
    knights_dict = knights_constructor(knights)
    fight1 = knights_dict["Lancelot"].knights_battle(knights_dict["Mordred"])
    fight2 = knights_dict["Arthur"].knights_battle(knights_dict["Red Knight"])
    result.update(**fight2, **fight1)
    return result


print(battle(KNIGHTS))
