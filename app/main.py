from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    # 1. Инициализация (вся грязная работа теперь внутри классов)
    knights = {
        key: Knight(config) for key, config in knights_config.items()
    }

    # 2. Описание сражений
    matchups = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"])
    ]

    # 3. Проведение боя
    for k1, k2 in matchups:
        k1_power, k2_power = k1.power, k2.power
        k1.take_damage(k2_power)
        k2.take_damage(k1_power)

    # 4. Результат
    return {knight.name: knight.hp for knight in knights.values()}
