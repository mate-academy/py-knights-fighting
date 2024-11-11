def apply_armor(knight: dict) -> int:
    return sum(piece["protection"] for piece in knight["armour"])


def apply_weapon(knight: dict) -> int:
    return knight["power"] + knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        if "power" in effects:
            knight["power"] += effects["power"]
        if "protection" in effects:
            knight["protection"] += effects["protection"]
        if "hp" in effects:
            knight["hp"] += effects["hp"]


def prepare_knight(knight: dict) -> None:
    knight["protection"] = apply_armor(knight)
    knight["power"] = apply_weapon(knight)
    apply_potion(knight)


def battle(knights_config: dict) -> dict:
    # Prepare each knight
    for knight_name in knights_config:
        prepare_knight(knights_config[knight_name])

    # Lancelot vs Mordred
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
    mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

    lancelot["hp"] = max(0, lancelot["hp"])
    mordred["hp"] = max(0, mordred["hp"])

    # Arthur vs Red Knight
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]
    arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

    arthur["hp"] = max(0, arthur["hp"])
    red_knight["hp"] = max(0, red_knight["hp"])

    # Return battle results
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
