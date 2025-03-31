from app.knights.knight import Knight
from app.battle.fight import Battle
from typing import Dict


def battle(knights_config: Dict) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    pairs = [
        (lancelot, mordred),
        (arthur, red_knight),
    ]

    battle_instance = Battle(pairs)
    return battle_instance.fight()
