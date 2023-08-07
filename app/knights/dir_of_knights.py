from app.knights.knight import Knight


def make_dir_of_knights(knights_config: dict) -> dict:
    return {name: Knight(knight) for name, knight in knights_config.items()}
