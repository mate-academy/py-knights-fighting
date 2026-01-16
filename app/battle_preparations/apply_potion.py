from app.battle_preparations.apply_weapon import apply_weapon
from app.battle_preparations.load_from_file import to_create_knight


def apply_potion(knights_dict: dict) -> list:
    knights = to_create_knight(knights_dict)
    knights_with_potion = apply_weapon(knights_dict)

    for index, knight in enumerate(knights):
        if knight["potion"]:
            for effect in knight["potion"]["effect"]:
                potion_effect = (getattr(knights_with_potion[index], effect)
                                 + knight["potion"]["effect"][effect])
                setattr(knights_with_potion[index], effect, potion_effect)
    return knights_with_potion
