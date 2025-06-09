from app.knights.knights import Knights
from app.knights.knights_characteristics import knights_characteristics


def fight(knight1: Knights, knight2: Knights) -> dict:
    hp1 = knight1.sum_hp()
    hp2 = knight2.sum_hp()
    power1 = knight1.sum_power()
    power2 = knight2.sum_power()
    protection1 = knight1.sum_protection()
    protection2 = knight2.sum_protection()
    hp1 -= max(0, power2 - protection1)
    hp2 -= max(0, power1 - protection2)
    return {
        knight1.name: max(0, hp1),
        knight2.name: max(0, hp2)
    }


def battle(knights: list) -> dict:
    result = {}
    result.update(fight(knights[0], knights[2]))
    result.update(fight(knights[1], knights[3]))
    return result


knights = knights_characteristics()

print(battle(knights))
