from app.items.armour import get_total_protection
from app.items.weapon import apply_weapon
from app.items.potion import apply_potion


def prepare_knight(knight: dict) -> dict:
    result = knight.copy()

    result["protection"] = get_total_protection(result["armour"])
    result["power"] = apply_weapon(result["power"], result["weapon"])

    result = apply_potion(result, result["potion"])

    return result
