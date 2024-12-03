from app.battle.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    battle1 = fight(lancelot, mordred)
    battle2 = fight(arthur, red_knight)

    return {
        **battle1,
        **battle2,
    }


def fight(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.hp -= max(0, second_knight.power - first_knight.protection)
    second_knight.hp -= max(0, first_knight.power - second_knight.protection)

    if first_knight.hp <= 0:
        first_knight.hp = 0
    if second_knight.hp <= 0:
        second_knight.hp = 0

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp,
    }
