from app.Knights import apply_effects


def knight_battle(knight1, knight2):
    # Knight1 attacks Knight2
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    # Knight2 attacks Knight1
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])

    # Make sure HP is non-negative
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knightsConfig):
    # Apply effects for each knight
    for knight in knightsConfig.values():
        apply_effects(knight)

    # Knight battles
    knight_battle(knightsConfig["lancelot"], knightsConfig["mordred"])
    knight_battle(knightsConfig["arthur"], knightsConfig["red_knight"])

    # Return battle results:
    return {knight["name"]: knight["hp"] for knight in knightsConfig.values()}
