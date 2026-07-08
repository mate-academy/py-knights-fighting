from app.preparation.potion import get_potion_effect


def calculate_hp(knights: dict, knitght_name: str) -> int:
    knight = knights[knitght_name]
    return knight["hp"] + get_potion_effect(knight, "hp")
