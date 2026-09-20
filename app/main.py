from app.battle_prep import BattleReady


# BATTLE:
def battle(knights: dict) -> None:

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    lancelot_ready = BattleReady(lancelot)
    arthur_ready = BattleReady(arthur)
    mordred_ready = BattleReady(mordred)
    red_knight_ready = BattleReady(red_knight)

    # 1 Lancelot vs Mordred:
    lancelot_ready.knight["hp"] -= (
        mordred_ready.knight["power"] - lancelot_ready.knight["protection"]
    )

    mordred_ready.knight["hp"] -= (
        lancelot_ready.knight["power"] - mordred_ready.knight["protection"]
    )

    if lancelot_ready.knight["hp"] <= 0:
        lancelot_ready.knight["hp"] = 0

    if mordred_ready.knight["hp"] <= 0:
        mordred_ready.knight["hp"] = 0

    # 2 Arthur vs Red_Knight:
    arthur_ready.knight["hp"] -= (
        red_knight_ready.knight["power"] - arthur_ready.knight["protection"]
    )

    red_knight_ready.knight["hp"] -= (
        arthur_ready.knight["power"] - red_knight_ready.knight["protection"]
    )

    if arthur_ready.knight["hp"] <= 0:
        arthur_ready.knight["hp"] = 0

    if red_knight_ready.knight["hp"] <= 0:
        red_knight_ready.knight["hp"] = 0

    # Return battle results
    return {
        lancelot_ready.knight["name"]: lancelot_ready.knight["hp"],
        mordred_ready.knight["name"]: mordred_ready.knight["hp"],
        arthur_ready.knight["name"]: arthur_ready.knight["hp"],
        red_knight_ready.knight["name"]: red_knight_ready.knight["hp"]
    }
