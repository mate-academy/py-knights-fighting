from app.character.character_builds import apply_upgrades


def run_round(k1: dict, k2: dict) -> None:
    dmg_to_k1 = k2["power"] - k1["protection"]
    dmg_to_k2 = k1["power"] - k2["protection"]
    k1["hp"] -= dmg_to_k1
    k2["hp"] -= dmg_to_k2


def battle(knights: dict) -> dict:
    # Apply upgrades
    for knight in knights.values():
        apply_upgrades(knight)

    # Define battle pairs
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    # Run battles
    for k1_name, k2_name in pairs:
        run_round(knights[k1_name], knights[k2_name])

    # Clamp HPs
    for knight in knights.values():
        knight["hp"] = max(0, knight["hp"])

    # Return results
    return {k["name"]: k["hp"] for k in knights.values()}
