from app.utils.knight_utils import (apply_armour, apply_weapon, apply_potion,
                                    hit)


def battle(knights: dict) -> dict:
    lancelot_knight = knights["lancelot"]
    mordred_knight = knights["mordred"]
    arthur_knight = knights["arthur"]
    red_knight = knights["red_knight"]

    for knight in (lancelot_knight, mordred_knight, arthur_knight, red_knight):
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    hit(lancelot_knight, mordred_knight)
    hit(mordred_knight, lancelot_knight)
    hit(arthur_knight, red_knight)
    hit(red_knight, arthur_knight)

    return {
        "Lancelot": lancelot_knight["hp"],
        "Arthur": arthur_knight["hp"],
        "Mordred": mordred_knight["hp"],
        "Red Knight": red_knight["hp"],
    }
