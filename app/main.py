from app.battle.preparation import apply_armour, apply_potion, apply_weapon
from app.battle.start import get_damage
from app.config import KNIGHTS
from app.knight.creation import Knight


def battle(knights_config: dict) -> dict:

    knights = {}

    for knight_name, knight_data in knights_config.items():
        apply_armour(knight_data)
        apply_potion(knight_data)
        apply_weapon(knight_data)
        knights[knight_name] = Knight(knight_data)

    get_damage(knights["lancelot"], knights["mordred"])
    get_damage(knights["arthur"], knights["red_knight"])

    return {
        knight_instance.name: knight_instance.hp
        for knight_instance in knights.values()
    }


print(battle(KNIGHTS))
