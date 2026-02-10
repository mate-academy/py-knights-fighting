from app.knights.knight import Knight


def prepare_knights(knights_info: dict) -> dict:
    knights = {}
    for key, data in knights_info.items():
        knights[key] = Knight(**data)
    return knights
