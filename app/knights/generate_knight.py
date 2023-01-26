from app.knights.knight_constructor import KnightFighter


def generate_list_of_knights(knights_from_config: dict) -> dict:
    knights_ready = dict()
    for name, knight_data in knights_from_config.items():
        knights_ready[name] = KnightFighter(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"],
            knight_data["armour"],
            knight_data["weapon"],
            knight_data["potion"]
        )
    return knights_ready
