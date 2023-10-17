from app.knights import KNIGHTS
from app.battle_prepare import battle_preparation
from app.battle import knight_battle


def battle(knights_config: dict) -> dict:
    knights = {knight: knights_config[knight] for knight in ["lancelot",
                                                             "arthur",
                                                             "mordred",
                                                             "red_knight"]}
    for knight in knights.values():
        battle_preparation(knight)
    knight_battle(knights["lancelot"], knights["mordred"])
    knight_battle(knights["arthur"], knights["red_knight"])
    return {knight["name"]: knight["hp"] for knight in knights.values()}


print(battle(KNIGHTS))
