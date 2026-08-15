def prepare_knight(knight: dict) -> None:
    # Battle preparations

    knight["protection"] = 0

    for i in knight["armour"]:
        knight["protection"] += i["protection"]

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if it exists
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]


def fight(knight1: dict, knight2: dict) -> None:
    # Fight logic
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # Check if someone fell in battle
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0


def battle(knightsconfig: dict) -> dict:
    for knight in knightsconfig.values():
        prepare_knight(knight)

    # Get individual knights
    lancelot = knightsconfig["lancelot"]
    arthur = knightsconfig["arthur"]
    mordred = knightsconfig["mordred"]
    red_knight = knightsconfig["red_knight"]

    # Battle:

    # 1. Lancelot vs Mordred
    fight(lancelot, mordred)

    # 2. Arthur vs Red Knight
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
