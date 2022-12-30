from app.knights.constant import KNIGHTS
from app.knights.knight import Knights
from app.knights.duel import duel


def battle(knights_config: dict) -> dict:
    for knight, config in knights_config.items():
        Knights(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    duel(
        Knights.all_created_knights["Lancelot"],
        Knights.all_created_knights["Mordred"]
    )
    duel(
        Knights.all_created_knights["Artur"],
        Knights.all_created_knights["Red Knight"]
    )

    return {
        Knights.all_created_knights["Lancelot"]
        .name: Knights.all_created_knights["Lancelot"]
        .hp,
        Knights.all_created_knights["Artur"]
        .name: Knights.all_created_knights["Artur"]
        .hp,
        Knights.all_created_knights["Mordred"]
        .name: Knights.all_created_knights["Mordred"]
        .hp,
        Knights.all_created_knights["Red Knight"]
        .name: Knights.all_created_knights["Red Knight"]
        .hp,
    }


print(battle(KNIGHTS))
