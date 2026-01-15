from __future__ import annotations
from app.knights import Knights


def battle(knights_dict: dict = None) -> dict:
    lancelot = (Knights(**knights_dict["lancelot"]))
    mordred = (Knights(**knights_dict["mordred"]))
    arthur = (Knights(**knights_dict["arthur"]))
    red_knight = (Knights(**knights_dict["red_knight"]))

    lancelot.battle_against(mordred)
    arthur.battle_against(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
