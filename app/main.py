from app.Knights.knight import KNIGHTS
from app.battle_preparation.lancelot import lancelot_preparation
from app.battle_preparation.arthur import arthur_preparation
from app.battle_preparation.mordred import preparation_mordred
from app.battle_preparation.red_knight import preparation_red_knight
from app.battle.battle_all import battle_all_knights


def battle(knight_config: dict) -> dict:
    lancelot = lancelot_preparation(knight_config)

    arthur = arthur_preparation(knight_config)

    mordred = preparation_mordred(knight_config)

    red_knight = preparation_red_knight(knight_config)

    battle_all_knights(lancelot, mordred, arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
