def combat(attacker: dict, target: dict) -> None:
    damage = attacker["power"] - target["protection"]
    target["hp"] = max(0, target["hp"] - max(0, damage))
