from app.preparation.potion import get_potion_effect


def apply_armour(
    knights: dict,
    knight_name: str,
) -> int:
    knight = knights[knight_name]
    protection = sum(part["protection"] for part in knight["armour"])
    return protection + get_potion_effect(knight, "protection")
