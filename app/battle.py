from app.knight import Knight


def create_knights_from_config(knights_config):
    """Перетворює конфігурацію лицарів у список об'єктів Knight"""
    knights = []
    for knight_name, knight_data in knights_config.items():
        knight = Knight(
            name=knight_data["name"],
            power=knight_data["weapon"]["power"],
            hp=knight_data["hp"],
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data.get("potion")  # Якщо potion є, передаємо його
        )
        knights.append(knight)
    return knights


def battle(knights_config) -> dict:
    # Створюємо список об'єктів лицарів з конфігурації
    knights_list = create_knights_from_config(knights_config)

    results = {}

    # Battle pairs
    battle_pairs = [
        ("Arthur", "Red Knight"),
        ("Lancelot", "Mordred"),
    ]

    # Convert knights_list to a dict for easier lookup by name
    knights_dict = {knight.name: knight for knight in knights_list}

    # Process battle logic
    for attacker_name, defender_name in battle_pairs:
        attacker = knights_dict[attacker_name]
        defender = knights_dict[defender_name]

        # Обчислюємо залишкове HP захисника після бою
        defender_hp_after_battle = defender.get_hp() - (attacker.get_power() - defender.get_protection())

        # Перевіряємо, чи не впав лицар
        if defender_hp_after_battle < 0:
            defender_hp_after_battle = 0

        # Зберігаємо результат
        results[defender.name] = defender_hp_after_battle

    return results  # Повертаємо словник з результатами бою
