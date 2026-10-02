def fight(knight_a: dict, knight_b: dict) -> None:
    """Runs a battle between two knights and updates their hp in place."""
    knight_a["hp"] -= knight_b["power"] - knight_a["protection"]
    knight_b["hp"] -= knight_a["power"] - knight_b["protection"]

    if knight_a["hp"] <= 0:
        knight_a["hp"] = 0

    if knight_b["hp"] <= 0:
        knight_b["hp"] = 0
