from app.knight import Knight


def battle(base_knights_config):
    # Створюємо словник лицарів на основі їх параметрів
    knights = {name: Knight(**config) for name, config in base_knights_config.items()}
    results = {}

    # Пари боїв
    battle_pairs = [
        ("arthur", "red_knight"),
        ("lancelot", "mordred"),
    ]

    for attacker_name, defender_name in battle_pairs:
        attacker = knights[attacker_name]
        defender = knights[defender_name]
        attacker_hp = attacker.get_hp
        # Атакує attacker
        defender_hp = max(0, defender.get_hp() - (attacker.get_power() - defender.get_protection()))
        if defender_hp <= 0:
            defender_hp = 0  # Defender вибуває, тому він не атакує

        else:
            # Якщо defender ще живий, він атакує у відповідь
            attacker_hp = max(0, attacker.get_hp() - (defender.get_power() - attacker.get_protection()))
            if attacker_hp <= 0:
                attacker_hp = 0  # Attacker вибуває

        # Записуємо результати
        results[attacker.name] = attacker_hp
        results[defender.name] = defender_hp

    return results
