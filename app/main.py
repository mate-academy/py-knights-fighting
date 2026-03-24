from app.knight import Knight


def conduct_fight(k1: Knight, k2: Knight) -> None:
    k1_power = k1.power
    k2_power = k2.power

    k1.take_damage(k2_power)
    k2.take_damage(k1_power)


def battle(knights_config: dict) -> dict:
    # Створюємо об'єкти лицарів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])
    conduct_fight(lancelot, mordred)
    conduct_fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
