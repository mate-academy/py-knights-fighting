from app.knight import Knight
from app.battle import knights_battle


def battle(config: dict) -> dict:
    knights = [Knight(cfg) for cfg in config.values()]
    return knights_battle(knights)
