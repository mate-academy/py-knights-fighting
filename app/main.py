from app.knights.knights_basic import Knights


def battle(knights: dict) -> dict:
    knights_config = {
        "lancelot": Knights(knights["lancelot"]),
        "arthur": Knights(knights["arthur"]),
        "mordred": Knights(knights["mordred"]),
        "red_knight": Knights(knights["red_knight"]),
    }
    attack_one = Knights.attack(knights_config["lancelot"],
                                knights_config["mordred"])
    attack_two = Knights.attack(knights_config["arthur"],
                                knights_config["red_knight"])
    result = {**attack_one, **attack_two}
    return result
