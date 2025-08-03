from .models import Knight


def duel(knight1: Knight, knight2: Knight):
    knight1.prepare_for_battle()
    knight2.prepare_for_battle()

    knight1.receive_damage(knight2.power)
    knight2.receive_damage(knight1.power)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }


def battle(knights_config: dict):
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    result1 = duel(lancelot, mordred)
    result2 = duel(arthur, red_knight)

    return {**result1, **result2}
