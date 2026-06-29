from app.battle_preparing import create_knights_dict, Battle


def battle(knights_config: dict) -> dict:
    knights = create_knights_dict(knights_config)
    Battle.battle_moves(knights["lancelot"], knights["mordred"])
    Battle.battle_moves(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
