import app.knights.base_class as base_class
import app.items.armour as armour
import app.items.potions as potions
import app.items.weapons as weapons


def preparation(knight_config: dict) -> dict:
    prepared_knights = {}

    for knight, info in knight_config.items():
        current_armour = armour.Armour(info["armour"])
        current_knight = base_class.Knight(info)
        current_potion = potions.Potion(info["potion"])
        current_weapon = weapons.Weapon(info["weapon"])

        current_knight.apply_equipment(current_weapon, current_armour)
        current_knight.apply_potion(current_potion)

        prepared_knights[knight] = current_knight

    return prepared_knights
