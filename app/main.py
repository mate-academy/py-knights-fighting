from app.battle.battle import BATTLE
from app.KNIGHTS.KNIGHTS import KNIGHTS

battle_system = BATTLE()
battle = battle_system.battle


def result_battle(
        lancelot: dict | BATTLE,
        mordred: dict | BATTLE,
        arthur: dict | BATTLE,
        red_knight: dict | BATTLE
) -> dict | BATTLE:
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
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


battle_system = BATTLE()
result = battle_system.battle(KNIGHTS)
print(result)
