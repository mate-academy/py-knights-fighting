from typing import Tuple


def perform_battle(knight1, knight2) -> tuple[int, int]:
    hp1 = knight1.hp
    hp2 = knight2.hp
    power1 = knight1.power
    power2 = knight2.power
    protection1 = knight1.protection
    protection2 = knight2.protection

    hp1 -= power2 - protection1
    hp2 -= power1 - protection2

    if hp1 <= 0:
        hp1 = 0
    if hp2 <= 0:
        hp2 = 0

    return hp1, hp2
