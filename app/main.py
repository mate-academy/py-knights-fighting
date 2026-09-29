from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    # 1. Створюємо екземпляри лицарів
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    # 2. Битва 1: Lancelot vs Mordred
    lancelot_initial_power = lancelot.power
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot_initial_power)

    # 3. Битва 2: Arthur vs Red Knight
    arthur_initial_power = arthur.power
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur_initial_power)

    # 4. Формуємо фінальний звіт результатів бою
    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
