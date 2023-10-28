from knights import Knights


def lets_fight(knights: callable) -> dict:
    """
    create instances class, add new properties and run fight between them
    :param knights: Knight
    :return: list with instances
    """
    lancelot = Knights("Lancelot", 35, 100, 50)
    arthur = Knights("Arthur", 45, 75, 55)
    mordred = Knights("Mordred", 30, 90, 60)
    red_knight = Knights("Red Knight", 40, 70, 45)

    for fighter in knights.all_knights:
        Knights.get_protection(fighter)
        Knights.get_potion(fighter)

    lancelot.__sub__(mordred)
    mordred.__sub__(lancelot)
    arthur.__sub__(red_knight)
    red_knight.__sub__(arthur)

    return Knights.result


print(lets_fight(Knights))
