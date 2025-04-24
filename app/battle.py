from app.models import Knight

def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Lancelot vs Mordred
    lancelot.hp -= max(0, mordred.power - lancelot.protection)
    mordred.hp -= max(0, lancelot.power - mordred.protection)

    # Arthur vs Red Knight
    arthur.hp -= max(0, red_knight.power - arthur.protection)
    red_knight.hp -= max(0, arthur.power - red_knight.protection)

    # Не допускаємо від'ємного hp
    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.hp = max(0, knight.hp)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
