from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    # 1. Initialization
    knights = {
        key: Knight(value) for key, value in knights_config.items()
    }

    # 2. Define Matchups
    # Format: (Attacker, Defender)
    matchups = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"])
    ]

    # 3. Execute Combat
    for k1, k2 in matchups:
        # Simultaneous strike logic
        k1_final_power = k1.power
        k2_final_power = k2.power

        k1.take_damage(k2_final_power)
        k2.take_damage(k1_final_power)

    # 4. Return Results
    return {knight.name: knight.hp for knight in knights.values()}
