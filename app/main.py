from app.knights import KNIGHTS
from app.preparation import prepare_knights


def fight(knight1: dict, knight2: dict) -> None:
    knight1["hp"] = max(
        0,
        knight1["hp"] - (knight2["power"] - knight1["protection"])
    )

    knight2["hp"] = max(
        0,
        knight2["hp"] - (knight1["power"] - knight2["protection"])
    )


def battle(knights_config: dict) -> dict:
    prepare_knights(knights_config)

    fight(
        knights_config["lancelot"],
        knights_config["mordred"]
    )

    fight(
        knights_config["arthur"],
        knights_config["red_knight"]
    )

    return {
        knight["name"]: knight["hp"]
        for knight in knights_config.values()
    }


print(battle(KNIGHTS))
