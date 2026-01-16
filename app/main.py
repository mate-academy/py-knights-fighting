from app.knight import Knight

def battle(knightsConfig: dict) -> dict:
    # Підготувати лицарів
    lancelot = Knight(knightsConfig["lancelot"])
    arthur = Knight(knightsConfig["arthur"])
    mordred = Knight(knightsConfig["mordred"])
    red_knight = Knight(knightsConfig["red_knight"])

    # Битви:
    # 1. Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # 2. Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Повертаємо результати битви
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
