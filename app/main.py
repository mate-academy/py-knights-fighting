from app.models.knight import Knight
from app.fighting.battle import fight
from typing import Any


def battle(knights_config: dict[str, dict[str, Any]]) -> dict[str, int]:
    knights: dict[str, Knight] = {}
    for key, config in knights_config.items():
        knights[key] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config.get("weapon"),
            potion=config.get("potion")
        )

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    battle1_results = fight(lancelot, mordred)
    battle2_results = fight(arthur, red_knight)

    return {**battle1_results, **battle2_results}
