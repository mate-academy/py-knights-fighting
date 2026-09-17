from app.knights.fight import fight
from app.knights.preparation import apply_knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knight_keys = ["lancelot", "arthur", "mordred", "red_knight"]

    for key in knight_keys:
        apply_knight(knights_config[key])

    fight(knights_config["lancelot"], knights_config["mordred"])
    fight(knights_config["arthur"], knights_config["red_knight"])

    # Return battle results:
    return {
        knights_config[knight_key]["name"]: knights_config[knight_key]["hp"]
        for knight_key in knight_keys
    }
