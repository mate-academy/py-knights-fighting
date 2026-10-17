from app.knights.knight import Knight


def create_all_knights(knights_config: dict) -> dict[str, Knight]:
    return {
        knight_id: Knight.create_knight(data)
        for knight_id, data in knights_config.items()
    }
