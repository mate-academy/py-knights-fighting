from app.knight import Knight


def battle(base_knights_config: dict) -> dict:
    # Створюємо словник лицарів на основі їх параметрів
    knights = {name: Knight(**config)
               for name, config in base_knights_config.items()}
    results = {}

    # Пари боїв
    battle_pairs = [
        ("arthur", "red_knight"),
        ("lancelot", "mordred"),
    ]

    for attacker_name, defender_name in battle_pairs:
        attacker = knights[attacker_name]
        defender = knights[defender_name]
        # Атакує attacker
        defender_hp = max(0, defender.get_hp()
                          - (attacker.get_power()
                             - defender.get_protection()))
        attacker_hp = max(0, attacker.get_hp()
                          - (defender.get_power()
                             - attacker.get_protection()))

        # Записуємо результати
        results[attacker.name] = attacker_hp
        results[defender.name] = defender_hp

    return results
