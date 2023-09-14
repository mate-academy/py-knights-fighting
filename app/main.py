from app.knights.config import KNIGHTS
from app.knights.knights_constuctor import knights_constructor


def battle(knights: {dict}) -> dict:
    result = {}
    knights_dict = knights_constructor(knights)
    fight1 = knights_dict["Lancelot"].knights_battle(knights_dict["Mordred"])
    fight2 = knights_dict["Arthur"].knights_battle(knights_dict["Red Knight"])
    result.update(**fight1, **fight2)
    return result


print(battle(KNIGHTS))
