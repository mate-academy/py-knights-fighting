from app.data_knights import KNIGHTS
from app.prepare import prepare
from app.fight import fight


def battle(knights_config: dict) -> dict:
    knights = {name: prepare(knight)
               for name, knight in knights_config.items()}

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for knight1, knight2 in battles:
        knights[knight1], knights[knight2] = (
            fight(knights[knight1], knights[knight2])
        )

    return {knight["name"]: knight["hp"] for knight in knights.values()}


print(battle(KNIGHTS))
