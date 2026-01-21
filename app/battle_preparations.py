from app.class_knight import Knight


def preparations_for_battle(knights_config: dict) -> None:
    for knight in knights_config.values():
        Knight(knight["name"], knight).config_preparations()
