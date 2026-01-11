from app.logics.knights import Knight


def conduct_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.take_hit(knight2.power)
    knight2.take_hit(knight1.power)


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    conduct_battle(knights["lancelot"], knights["mordred"])
    conduct_battle(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
