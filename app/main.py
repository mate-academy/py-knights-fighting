from app.knights.knights_basic import Knight


def battle(knights: dict) -> dict:
    knights_config = {
        "lancelot": Knight(knights["lancelot"]),
        "arthur": Knight(knights["arthur"]),
        "mordred": Knight(knights["mordred"]),
        "red_knight": Knight(knights["red_knight"]),
    }
    attack_one = Knight.attack(knights_config["lancelot"],
                               knights_config["mordred"])
    attack_two = Knight.attack(knights_config["arthur"],
                               knights_config["red_knight"])
    result = {**attack_one, **attack_two}
    return result
