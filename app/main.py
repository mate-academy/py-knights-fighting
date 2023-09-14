from app.data.functions import knight_the_knight
from app.data.database import KNIGHTS


def battle(knight_config: dict) -> dict:
    knights_dict = {
        knight["name"]: knight_the_knight(knight)
        for knight in knight_config.values()
    }
    knights_dict["Lancelot"].duel(knights_dict["Mordred"])
    knights_dict["Arthur"].duel(knights_dict["Red Knight"])

    result = {knight.name: knight.hp for knight in knights_dict.values()}

    return result


print(battle(KNIGHTS))
