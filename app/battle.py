from typing import Dict
from app.knight import Knight


def battle(
        knights_config: Dict[str, dict]
) -> Dict[str, int]:
    knights = {name: Knight(**info) for name, info in knights_config.items()}

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # Battle
    battle_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    # Battle
    for attacker, defender in battle_pairs:
        knights[defender].hp -= (
            knights[attacker].power - knights[defender].protection
        )

        knights[attacker].hp -= (
            knights[defender].power - knights[attacker].protection
        )

    # Check if someone fell in battle
    for knight in knights.values():
        if knight.hp <= 0:
            knight.hp = 0

    return {knight.name: knight.hp for knight in knights.values()}
