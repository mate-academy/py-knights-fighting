from app.apply_stuff.apply_armour import apply_armour
from app.apply_stuff.apply_weapon import apply_weapon
from app.apply_stuff.apply_potion import apply_potion


def battle(knights_config: dict) -> dict:
    lancelot = knights_config.get("lancelot")
    arthur = knights_config.get("arthur")
    mordred = knights_config.get("mordred")
    red_knight = knights_config.get("red_knight")

    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knights:
        if knight.get("hp") <= 0:
            knight["hp"] = 0

    return {
        knight.get("name"): knight.get("hp") for knight in knights
    }
