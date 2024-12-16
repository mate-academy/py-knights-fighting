def fight(knight1: dict, knight2: dict) -> None:
    knight1_attack = knight1["power"] + knight1["weapon"]["power"]
    knight2_attack = knight2["power"] + knight2["weapon"]["power"]

    knight1_armour = sum(
        armour.get("protection", 0) for armour in knight1.get("armour", []))
    knight2_armour = sum(
        armour.get("protection", 0) for armour in knight2.get("armour", []))

    # Calculate damage
    knight2["hp"] -= max(knight1_attack - knight2_armour, 0)
    knight1["hp"] -= max(knight2_attack - knight1_armour, 0)

    # Ensure HP doesn't go below zero
    knight1["hp"] = max(knight1["hp"], 0)
    knight2["hp"] = max(knight2["hp"], 0)
