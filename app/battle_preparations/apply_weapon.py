from app.battle_preparations.load_from_file import to_create_knight
from app.battle_preparations.apply_armour import apply_armour


def apply_weapon(knights_dict: dict) -> list:
    knights = to_create_knight(knights_dict)
    knights_with_weapons = apply_armour(knights_dict)
    for index, knight in enumerate(knights):
        knights_with_weapons[index].power += knight["weapon"]["power"]

    return knights_with_weapons
