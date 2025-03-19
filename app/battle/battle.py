from typing import Dict, Any
from app.knights.knight import Knight


def battle(knight1: Knight, knight2: Knight) -> None:
    damage_to_knight1 = max(0, knight2.final_power - knight1.final_armour)
    damage_to_knight2 = max(0, knight1.final_power - knight2.final_armour)
    knight1.final_hp -= damage_to_knight1
    knight1.final_hp = max(0, knight1.final_hp)
    knight2.final_hp -= damage_to_knight2
    knight2.final_hp = max(0, knight2.final_hp)

    if knight1.final_hp <= 0 and knight2.final_hp <= 0:
        print("draw")
    elif knight1.final_hp <= 0:
        print(f"Knight: {knight2.name} won")
    elif knight2.final_hp <= 0:
        print(f"Knight: {knight1.name} won")
    else:
        print("both Knights survived")

    print(f"{knight1.name} HP: {knight1.final_hp}")
    print(f"{knight2.name} HP: {knight2.final_hp}")


def run_battle(knights_config: Dict[str, Dict[str, Any]]) -> None:
    lancelot = Knight("Lancelot", knights_config["lancelot"])
    mordred = Knight("Mordred", knights_config["mordred"])
    arthur = Knight("Arthur", knights_config["arthur"])
    red_knight = Knight("Red Knight", knights_config["red_knight"])

    for knight in (lancelot, mordred, arthur, red_knight):
        knight.calculate_stats()
        knight.calculate_armour()
        knight.final_stats()

    # Używaj funkcji battle(), NIE manualnych odjęć
    battle(lancelot, mordred)
    battle(arthur, red_knight)

    return {
        "Lancelot": lancelot.final_hp,
        "Arthur": arthur.final_hp,
        "Mordred": mordred.final_hp,
        "Red Knight": red_knight.final_hp,
    }
