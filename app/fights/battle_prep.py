from app.knights.knight import Knight


def prepare_knights(knights_config: dict) -> dict:
    knights = {}
    for key, data in knights_config.items():
        knights[key] = Knight(**data)
    return knights
