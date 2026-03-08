from typing import Dict, Any
from app.knight.config import KNIGHTS
from app.knight.models import Knight, Armour, Weapon, Potion
from app.knight.battle import fight


def build_knight_from_config(data: Dict[str, Any]) -> Knight:
    armour = [Armour(
        a["part"],
        a["protection"]) for a in data.get("armour", [])]

    weapon_data = data.get("weapon")
    weapon = Weapon(
        weapon_data["name"],
        weapon_data["power"]) if weapon_data else None

    potion_data = data.get("potion")
    potion = Potion(
        potion_data["name"],
        potion_data["effect"]) if potion_data else None

    return Knight(
        name=data["name"],
        base_hp=data["hp"],
        base_power=data["power"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot = build_knight_from_config(knights_config["lancelot"])
    mordred = build_knight_from_config(knights_config["mordred"])
    arthur = build_knight_from_config(knights_config["arthur"])
    red_knight = build_knight_from_config(knights_config["red_knight"])

    result = {}
    result.update(fight(lancelot, mordred))
    result.update(fight(arthur, red_knight))

    return result


if __name__ == "__main__":
    print(battle(KNIGHTS))
