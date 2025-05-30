from .knights import Knight


def fight(knight1, knight2):
    """Провести бій між двома лицарами"""
    # Розрахунок пошкоджень для кожного лицаря
    damage_to_knight1 = max(0, knight2.power - knight1.protection)
    damage_to_knight2 = max(0, knight1.power - knight2.protection)

    # Застосування пошкоджень
    knight1.take_damage(damage_to_knight1)
    knight2.take_damage(damage_to_knight2)


def battle(knights_config):
    """Провести турнір між усіма лицарами"""
    # Створення об'єктів лицарів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Проведення битв за парами
    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # Повернення результатів турніру
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }