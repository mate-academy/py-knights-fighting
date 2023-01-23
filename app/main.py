from __future__ import annotations
from app.knights import ready_to_battle


def battle(knight: dict) -> dict:
    lancelot = ready_to_battle(knight_param=knight["lancelot"])
    mordred = ready_to_battle(knight_param=knight["mordred"])
    artur = ready_to_battle(knight_param=knight["arthur"])
    red_knight = ready_to_battle(knight_param=knight["red_knight"])

    lancelot.fight(other=mordred)
    artur.fight(other=red_knight)

    return {
        lancelot.name: lancelot.hp,
        artur.name: artur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
