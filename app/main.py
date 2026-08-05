from app.knights.Knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, config in knights_config.items():
        knight = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config.get("weapon"),
            potion=config.get("potion")
        )
        knights[knight.name.lower()] = knight  # Використовуємо ім'я як ключ

    # Apply all items to knights
    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    battle_pairs = {
        "Lancelot": "Mordred",
        "Arthur": "Red Knight",
    }

    results = {}
    for knight1_name, knight2_name in battle_pairs.items():
        knight1 = knights.get(knight1_name.lower())
        knight2 = knights.get(knight2_name.lower())

        if knight1 and knight2:
            damage_to_knight1 = max(0, knight2.power - knight1.protection)
            damage_to_knight2 = max(0, knight1.power - knight2.protection)

            knight1.hp = max(0, knight1.hp - damage_to_knight1)
            knight2.hp = max(0, knight2.hp - damage_to_knight2)

            results[knight1.name] = knight1.hp
            results[knight2.name] = knight2.hp

    return results
