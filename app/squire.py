from app.battle.item import Weapon, Armor, Potion
from app.battle.knight import Knight
from typing import Dict


def create_knight_from_config(name: str,
                              config: Dict) -> Knight:
    weapon_data = config.get("weapon")
    weapon = Weapon(weapon_data["name"],
                    weapon_data["power"]) if weapon_data else None

    armor_data = config.get("armor")
    armor_list = [Armor(f"{a["part"]} armor",
                        a["part"], a["protection"])
                  for a in armor_data] if armor_data else []

    potion_data = config.get("potion")
    potion = Potion(potion_data["name"],
                    potion_data.get("effect")) if potion_data else None

    return Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"],
        armor=armor_list,
        weapon=weapon,
        potion=potion,
    )
