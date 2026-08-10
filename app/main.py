from app.models.knight import Knight


def fight(knight1: dict, knight2: dict) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    mordred = Knight(**knights_config["mordred"])
    arthur = Knight(**knights_config["arthur"])
    red_knight = Knight(**knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
