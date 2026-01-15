from app.functions.apply_atributes import apply_attributes
from app.functions.combat import combat


def battle(knights: dict) -> dict:
    for knight_name, knight in knights.items():
        apply_attributes(knight)
    combat(knights["mordred"], knights["lancelot"])
    combat(knights["lancelot"], knights["mordred"])
    combat(knights["red_knight"], knights["arthur"])
    combat(knights["arthur"], knights["red_knight"])
    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["arthur"]["name"]: knights["arthur"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
        knights["red_knight"]["name"]: knights["red_knight"]["hp"],
    }
