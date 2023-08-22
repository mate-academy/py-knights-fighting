from app.battle_preparations.apply_weapon import apply_weapon
from app.battle_preparations.load_from_file import to_create_knight


def apply_potion(knights_dict: dict) -> list:
    knights = to_create_knight(knights_dict)
    knights_with_potion = apply_weapon(knights_dict)
    for index, knight in enumerate(knights):
        if knight["potion"]:
            if "power" in knight["potion"]["effect"]:
                knights_with_potion[index].power = (
                    knights_with_potion[index].power
                    + knight["potion"]["effect"]["power"]
                )
            if "protection" in knight["potion"]["effect"]:
                knights_with_potion[index].protection = (
                    knights_with_potion[index].protection
                    + knight["potion"]["effect"]["protection"]
                )
            if "hp" in knight["potion"]["effect"]:
                knights_with_potion[index].hp = (
                    knights_with_potion[index].hp
                    + knight["potion"]["effect"]["hp"]
                )
    return knights_with_potion
