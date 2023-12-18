from app.knight import Knight


def battle(knights: dict) -> dict:
    """Simulate a battle between two knights."""
    knight1 = Knight(**knights["lancelot"])
    knight2 = Knight(**knights["mordred"])
    knight3 = Knight(**knights["arthur"])
    knight4 = Knight(**knights["red_knight"])

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp < 1:
        knight1.hp = 0

    if knight2.hp < 1:
        knight2.hp = 0

    knight3.hp -= knight4.power - knight3.protection
    knight4.hp -= knight3.power - knight4.protection

    if knight3.hp < 1:
        knight3.hp = 0

    if knight4.hp < 1:
        knight4.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
        knight3.name: knight3.hp,
        knight4.name: knight4.hp,
    }
