def apply_armour(knight: dict) -> None:
    knight["protection"] = sum(
        piece.get("protection", 0) for piece in knight.get("armour", [])
    )


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight.get("weapon", {}).get("power", 0)


def apply_potion(knight: dict) -> None:
    potion = knight.get("potion")
    if not potion:
        return
    for stat, delta in potion.get("effect", {}).items():
        knight[stat] = knight.get(stat, 0) + delta


def hit(attacker: dict, defender: dict) -> None:
    damage = max(0, attacker["power"] - defender.get("protection", 0))
    defender["hp"] = max(0, defender["hp"] - damage)
