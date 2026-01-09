def prepare_knight(knight: dict) -> dict:
    knight = knight.copy()

    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value

    return knight


def calculate_damage(attacker: dict, defender: dict) -> int:
    return max(attacker["power"] - defender["protection"], 0)


def battle(knights_config: dict) -> dict:
    knights = {
        name: prepare_knight(config)
        for name, config in knights_config.items()
    }

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for attacker_name, defender_name in battles:
        attacker = knights[attacker_name]
        defender = knights[defender_name]

        defender["hp"] -= calculate_damage(attacker, defender)
        attacker["hp"] -= calculate_damage(defender, attacker)

    for knight in knights.values():
        if knight["hp"] < 0:
            knight["hp"] = 0

    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }
