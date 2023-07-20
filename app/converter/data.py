from app.item.armor import Armor
from app.item.weapon import Weapon
from app.person.knight import Knight
from app.item.potion import PotionEffect, Potion


def convert_data_to_knights(data: dict) -> list[Knight]:
    knights = []
    for knight in data.values():
        knights.append(convert_knight(knight))

    return knights


def convert_knight(knight: dict) -> Knight:
    armour = convert_armour(knight["armour"])
    weapon = convert_weapon(knight["weapon"])
    potion = convert_potion(knight["potion"])

    return Knight(
        knight["name"],
        knight["power"],
        knight["hp"],
        armour,
        weapon,
        potion
    )


def convert_weapon(weapon: dict) -> Weapon:
    return Weapon(weapon["name"], weapon["power"])


def convert_armour(armour: list[dict]) -> list[Armor]:
    armour_list = []
    for armor in armour:
        armour_list.append(Armor(armor["part"], armor["protection"]))

    return armour_list


def convert_potion(potion: dict) -> Potion:
    if potion is not None:
        return Potion(
            potion["name"],
            convert_potion_effect(potion["effect"])
        )


def convert_potion_effect(effects: dict) -> PotionEffect:
    hp = effects.get("hp")
    power = effects.get("power")
    protection = effects.get("protection")
    return PotionEffect(
        hp if hp is not None else 0,
        power if power is not None else 0,
        protection if protection is not None else 0,
    )
