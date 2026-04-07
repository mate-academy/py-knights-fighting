from app.models import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    k1_power = knight1.power
    k2_power = knight2.power

    knight1.get_damage(k2_power)
    knight2.get_damage(k1_power)


def battle(knights_config: dict) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        knight.name: knight.hp
        for knight in [lancelot, arthur, mordred, red_knight]
    }
