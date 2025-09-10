from __future__ import annotations
from app.knights.knight_prototype import Knight
from app.buffs.armour import Armour
from app.buffs.weapon import Weapon
from app.buffs.potion import Potion


def dict_to_knight(knight_dict: dict) -> Knight:
    armour = [
        Armour(armour_config["part"], armour_config["protection"])
        for armour_config in knight_dict.get("armour", [])
    ]
    weapon = Weapon(
        knight_dict["weapon"]["name"],
        knight_dict["weapon"]["power"]
    )
    potion = None
    if knight_dict.get("potion"):
        effect = knight_dict["potion"]["effect"]
        potion = Potion(
            name=knight_dict["potion"]["name"],
            power=effect.get("power", 0),
            protection=effect.get("protection", 0),
            hp=effect.get("hp", 0)
        )
    return Knight(
        name=knight_dict["name"],
        power=knight_dict["power"],
        hp=knight_dict["hp"],
        weapon=weapon,
        armour=armour,
        potion=potion
    )
