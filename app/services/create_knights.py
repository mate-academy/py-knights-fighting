from app.models.knight import Knight


def create_knights(knights_config: dict[str, dict]) -> dict[str, Knight]:
    knights = {}
    for key, config in knights_config.items():
        knight = Knight(**config)
        knight.prepare_for_battle()
        knights[key] = knight
    return knights
