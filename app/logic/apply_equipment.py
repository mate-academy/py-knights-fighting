from app.models.knights import Knight
from app.models.equipment import Armour, Weapon, Potion


def prepare_to_battle(knights: dict) -> dict:
    ready_knights = {}

    for knight_name, characteristics in knights.items():
        redy_knight = Knight(
            characteristics["name"],
            characteristics["power"],
            characteristics["hp"]
        )

        knight_armour = []
        for armor_part in characteristics["armour"]:
            part = Armour(armor_part["part"], armor_part["protection"])
            knight_armour.append(part)

        weapon_data = characteristics["weapon"]
        knight_weapon = Weapon(weapon_data["name"], weapon_data["power"])

        knight_potion = None
        if characteristics["potion"]:
            potion_data = characteristics["potion"]
            knight_potion = Potion(potion_data["name"], potion_data["effect"])

        redy_knight.apply_equipment(
            knight_weapon,
            knight_armour,
            knight_potion
        )

        ready_knights[knight_name] = redy_knight

    return ready_knights
