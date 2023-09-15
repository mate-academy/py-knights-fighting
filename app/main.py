from typing import Dict, Any

from app.knights import Knight
from app.potions import Potion
from app.battle import perform_battle

KNIGHTS = {}


def initialize_knights(knights_config) -> dict[Any, Any]:
    knights = {}
    for key, config in knights_config.items():
        knights[key] = Knight(**config)
        knights[key].apply_armour()
        knights[key].apply_weapon()
        knights[key].apply_potion()
    return knights


def main() -> dict[Any, Any]:
    knights = initialize_knights(KNIGHTS)
    results = {}

    for knight1, knight2 in [("lancelot", "mordred"), ("arthur", "red_knight")]:
        hp1, hp2 = perform_battle(knights[knight1], knights[knight2])
        knights[knight1].hp = hp1
        knights[knight2].hp = hp2

    for name, knight in knights.items():
        results[knight.name.capitalize()] = knight.hp

    return results


if __name__ == "__main__":
    results = main()
    for name, hp in results.items():
        print(f"{name}: {hp}")
