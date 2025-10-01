from __future__ import annotations


from app.data.index import KNIGHTS
from app.knight.prepare import PrepareKnight
from app.battle.battle import knight_battle


def battle(knights_config: dict) -> dict:
    knight_instance = PrepareKnight(knights_config)

    lancelot = knight_instance.get_prepared_knight(knight_name="lancelot")
    arthur = knight_instance.get_prepared_knight(knight_name="arthur")
    mordred = knight_instance.get_prepared_knight(knight_name="mordred")
    red_knight = knight_instance.get_prepared_knight(knight_name="red_knight")

    knight_battle(first_knight=lancelot, second_knight=mordred)
    knight_battle(first_knight=arthur, second_knight=red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
