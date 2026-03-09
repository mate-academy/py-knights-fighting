from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    pairs = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"])
    ]

    for knight_a, knight_b in pairs:
        power_a = knight_a.power
        power_b = knight_b.power

        knight_a.receive_damage(power_b)
        knight_b.receive_damage(power_a)

    return {
        k.name: k.hp for k in knights.values()
    }
