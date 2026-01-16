from app.knights import Knight
from app.equipment import Weapon, Armour, Potion
from app.battle import battle_round


def dict_to_knight(data: dict) -> Knight:
    weapon = Weapon(**data["weapon"]) if data.get("weapon") else None
    armour = [
        Armour(
            name=armour_part.get("name", armour_part.get("part", "")),
            protection=armour_part["protection"]
        )
        for armour_part in data.get("armour", [])
    ]
    potion = Potion(**data["potion"]) if data.get("potion") else None
    return Knight(
        name=data["name"],
        hp=data["hp"],
        base_power=data["power"],
        base_protection=0,
        weapon=weapon,
        armour=armour,
        potion=potion
    )


def battle(knights_config: dict) -> dict:
    knights = {
        name: dict_to_knight(data)
        for name, data in knights_config.items()
    }
    for knight in knights.values():
        knight.apply_equipment()
    results = battle_round(
        knights["lancelot"],
        knights["mordred"],
        knights["arthur"],
        knights["red_knight"]
    )
    return {name: stats["hp"] for name, stats in results.items()}
