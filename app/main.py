from app.program_data.constant import KNIGHTS
from app.program_data.knight import Knight
from app.program_data.duel import duel

all_created_knights = {}


def battle(knights_config: dict) -> dict:

    for knight, config in knights_config.items():
        all_created_knights[config["name"]] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    duel(
        all_created_knights["Lancelot"],
        all_created_knights["Mordred"]
    )
    duel(
        all_created_knights["Artur"],
        all_created_knights["Red Knight"]
    )

    return {instance.name: instance.hp
            for instance in all_created_knights.values()}


print(battle(KNIGHTS))
