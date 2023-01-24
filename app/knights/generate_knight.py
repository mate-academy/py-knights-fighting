from app.knights.knight_constructor import KnightFighter


def generate_list_of_knights(knights_from_config: dict) -> dict:
    knights_ready = dict()
    for item in knights_from_config:
        knights_ready[item] = KnightFighter(
            knights_from_config[item]["name"],
            knights_from_config[item]["power"],
            knights_from_config[item]["hp"],
            knights_from_config[item]["armour"],
            knights_from_config[item]["weapon"],
            knights_from_config[item]["potion"]
        )
    return knights_ready
