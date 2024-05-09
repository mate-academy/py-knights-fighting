from typing import Dict, Any
from .armour import Armour
from .knights import Knight
from .potion import Potion
from .weapon import Weapon


def create_knight(knight_data: Dict[str, Any]) -> Knight:
    armour = [Armour(piece["part"], piece["protection"]) for piece in knight_data.get("armour", [])]  # noqa: E501
    weapon = Weapon(knight_data["weapon"]["name"], knight_data["weapon"]["power"])  # noqa: E501
    potion_data = knight_data.get("potion")
    potion = None
    if potion_data:
        potion = Potion(potion_data["name"], potion_data["effect"])
    return Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion
    )


def battle(knights_config: dict) -> dict:
    knights = {}

    for name, config in knights_config.items():
        knight = Knight(name=config["name"],
                        power=config["power"],
                        hp=config["hp"],
                        armour=config["armour"],
                        weapon=config["weapon"],
                        potion=config["potion"])
        knight.prepare_for_battle()
        knights[name] = knight

    knights["lancelot"].hp -= max(0, knights["mordred"].power
                                  - knights["lancelot"].protection)
    knights["mordred"].hp -= max(0, knights["lancelot"].power
                                 - knights["mordred"].protection)

    knights["arthur"].hp -= max(0, knights["red_knight"].power
                                - knights["arthur"].protection)
    knights["red_knight"].hp -= max(0, knights["arthur"].power
                                    - knights["red_knight"].protection)
    for knight in knights.values():
        if knight.hp < 0:
            knight.hp = 0
    return {knight.name: knight.hp for knight in knights.values()}
