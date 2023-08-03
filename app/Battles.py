from app.Knights import apply_effects


def knight_battle(knight1: dict, knight2: dict) -> None:
    # Knight1 attacks Knight2
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    # Knight2 attacks Knight1
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])

    # Make sure HP is non-negative
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knights_config: dict) -> dict:
    # Apply effects for each knight
    for knight in knights_config.values():
        apply_effects(knight)

    # Knight battles
    knight_battle(knights_config["lancelot"], knights_config["mordred"])
    knight_battle(knights_config["arthur"], knights_config["red_knight"])

    # Return battle results:
    return {knight["name"]: knight["hp"] for knight in knights_config.values()}
