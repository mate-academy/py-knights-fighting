from typing import Dict, Any
from app.models.knight import Knight
from app.models.armour import Armour
from app.models.weapon import Weapon
from app.models.potion import Potion
from app.utils.battle import battle_knights


def create_knight(config: Dict[str, Any]) -> Knight:
    armour = []
    if "armour" in config:
        for index in config["armour"]:
            armour.append(Armour(index["part"], index["protection"]))
    weapon = Weapon(config["weapon"]["name"],
                    config["weapon"]["power"]) if "weapon" in config else None
    potion = Potion(config["potion"]["name"],
                    config["potion"]["effect"]
                    ) if config.get("potion") else None
    return Knight(config["name"],
                  config["power"],
                  config["hp"],
                  armour, weapon, potion
                  )


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:

    knights = {name: create_knight(config)
               for name, config in knights_config.items()}

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for knight1_name, knight2_name in battles:
        knight1 = knights[knight1_name]
        knight2 = knights[knight2_name]
        battle_knights(knight1, knight2)

    return {knight.name: knight.hp for knight in knights.values()}
