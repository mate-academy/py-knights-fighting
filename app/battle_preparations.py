from app.class_knight import Knight


def preparations_for_battle(knights_config: dict) -> None:
    make_knights = []
    for knight in knights_config.values():
        make_knights.append(Knight(knight["name"],
                                   knight).config_preparations())
