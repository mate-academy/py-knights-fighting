from app.knights.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights: dict) -> dict:
    knights = {name: Knight(**details) for name, details in knights.items()}
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {k.name: k.hp for k in knights.values()}
