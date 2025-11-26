from typing import Dict

from .knights.battle import prepare_knights, duel


def battle(knightsconfig: Dict[str, Dict]) -> Dict[str, int]:
    """
    Przyjmuje config rycerzy (jak KNIGHTS) i zwraca wynik walki:
    {name: hp_after_battle}
    """
    knights = prepare_knights(knightsconfig)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # 1. Lancelot vs Mordred
    duel(lancelot, mordred)

    # 2. Arthur vs Red Knight
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
