from app.fighters.knight import Knight
from app.tournament.battle import Battle


def battle(knights_config: dict) -> dict:

    # knights = [lancelot, arthur, mordred, red_knight]
    knights = [Knight(knight) for knight in knights_config.values()]

    # Lancelot vs Mordred
    Battle.update_hp(knights[0], knights[2])
    # Arthur vs Red Knight
    Battle.update_hp(knights[1], knights[3])

    return Battle.battle_result(knights)
