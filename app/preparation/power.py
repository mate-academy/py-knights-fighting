from app.preparation.potion import get_potion_effect


def get_power(knights: dict, knight_name: str) -> int:
    knight = knights[knight_name]
    return (
        knight["power"]
        + knight["weapon"]["power"]
        + get_potion_effect(knight, "power")
    )
