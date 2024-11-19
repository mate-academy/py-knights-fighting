from app.preparation.armour import Armor
from app.preparation.weapon import Weapon
from app.preparation.potion import Potion


def prepare_knight(knight: dict) -> None:
    Armor(knight).put_on_armour()
    Weapon(knight).tool_up()
    Potion(knight).use_potion()


def battle(knights: dict) -> dict:
    for knight in knights.values():
        prepare_knight(knight)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
