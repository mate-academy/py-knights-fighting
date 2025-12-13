from typing import Dict

from .knights.battle import prepare_knights, duel


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """Run battles and return final hp of all knights."""
    knights = prepare_knights(knights_config)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    # Zwracamy słownik {nazwa_rycerza: jego_hp_po_bitwie}
    return {knight.name: knight.hp for knight in knights.values()}
