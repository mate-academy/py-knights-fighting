from app.knights.config import KNIGHTS
from app.knights.knight import Knight
from app.battle.battle import Battle


def battle(knight_config: dict) -> dict:

    knight_dict = {}

    for name, value in knight_config.items():
        knight = Knight(**value)
        knight_dict[name] = knight

    Battle.battle(knight_dict["lancelot"], knight_dict["mordred"])
    Battle.battle(knight_dict["arthur"], knight_dict["red_knight"])

    # Return battle results:
    return {
        value.name: value.hp for value in knight_dict.values()
    }


print(battle(KNIGHTS))
