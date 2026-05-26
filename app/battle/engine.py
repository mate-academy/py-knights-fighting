def fight(attacker: dict, defender: dict) -> None:
    damage_to_a = max(0, defender["power"] - attacker["protection"])
    damage_to_b = max(0, attacker["power"] - defender["protection"])

    attacker["hp"] = max(0, attacker["hp"] - damage_to_a)
    defender["hp"] = max(0, defender["hp"] - damage_to_b)
