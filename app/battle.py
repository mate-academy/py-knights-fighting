from typing import Dict
from app.models import Knight


def battle(knights: Dict[str, Knight]) -> Dict[str, int]:
    results = {}

    for knight_key in knights:
        knight = knights[knight_key]
        results[knight_key] = knight.prepare_for_battle()

    lancelot_hp = results["lancelot"]["hp"]
    mordred_hp = results["mordred"]["hp"]

    lancelot_damage = (
        max(results["mordred"]["power"] - results["lancelot"]["protection"], 0)
    )
    mordred_damage = (
        max(results["lancelot"]["power"] - results["mordred"]["protection"], 0)
    )

    lancelot_hp -= lancelot_damage
    mordred_hp -= mordred_damage

    results["lancelot"]["hp"] = max(lancelot_hp, 0)
    results["mordred"]["hp"] = max(mordred_hp, 0)

    arthur_hp = results["arthur"]["hp"]
    red_knight_hp = results["red_knight"]["hp"]

    arthur_damage = (
        max(results["red_knight"]["power"] -
            results["arthur"]["protection"], 0)
    )
    red_knight_damage = (
        max(results["arthur"]["power"] -
            results["red_knight"]["protection"], 0)
    )

    arthur_hp -= arthur_damage
    red_knight_hp -= red_knight_damage

    results["arthur"]["hp"] = max(arthur_hp, 0)
    results["red_knight"]["hp"] = max(red_knight_hp, 0)

    return {knights[knight_key].name: results[knight_key]["hp"]
            for knight_key in knights}
