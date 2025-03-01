from app.knights.apply_stuff import apply_stuff
from app.battle.battle_base import Battle


def battle(knights_config: dict) -> dict:
    knights = apply_stuff(knights_config)
    Battle.battle_moves(knights["lancelot"], knights["mordred"])
    Battle.battle_moves(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
