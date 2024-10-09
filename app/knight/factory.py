from app.entities import Armour, Weapon, Potion
from .knight import Knight


def create_armour(armour_data: list) -> list:
    return [Armour(arm["part"], arm["protection"]) for arm in armour_data]


def create_weapon(weapon_data: dict) -> Weapon:
    return Weapon(weapon_data["name"], weapon_data["power"])


def create_potion(potion_data: dict) -> Potion:
    if potion_data is None:
        return None
    return Potion(potion_data["name"], potion_data["effect"])


def create_knight(knight_data: dict) -> Knight:
    armour = create_armour(knight_data["armour"])
    weapon = create_weapon(knight_data["weapon"])
    potion = create_potion(knight_data.get("potion"))
    return Knight(
        name=knight_data["name"],
        base_power=knight_data["power"],
        hp=knight_data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def get_knights(knights_config: dict) -> list:
    return [
        create_knight(knight_data) for knight_data in knights_config.values()
    ]
