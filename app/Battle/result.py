from __future__ import annotations
from app.Battle.Battle import Battle
from app.Knights.Knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    battle_instance_1 = Battle(lancelot, mordred)
    battle_instance_2 = Battle(arthur, red_knight)

    battle_instance_1.conduct_battle()
    battle_instance_2.conduct_battle()

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
