from app.knight import Knight


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    knights = {name: Knight(config) for name, config in knights_config.items()}

    for knight in knights.values():
        knight.prepare_for_battle()

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for attacker_key, defender_key in pairs:
        attacker = knights[attacker_key]
        defender = knights[defender_key]

        attacker.take_damage(defender.power)
        defender.take_damage(attacker.power)

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    from app.knights_data import KNIGHTS

    print(battle(KNIGHTS))
