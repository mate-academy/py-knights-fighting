from app.model.knight import Knight
from app.model.battle import battle_between_knights


def battle(knights_config: dict) -> dict:
    knights_instance = {}
    for key, value in knights_config.items():
        knights_instance[key] = Knight.prepare_knight(value)
    battle_between_knights(
        knights_instance["lancelot"],
        knights_instance["mordred"]
    )
    battle_between_knights(
        knights_instance["arthur"],
        knights_instance["red_knight"]
    )
    return {
        knights_instance["lancelot"].name: knights_instance["lancelot"].hp,
        knights_instance["mordred"].name: knights_instance["mordred"].hp,
        knights_instance["arthur"].name: knights_instance["arthur"].hp,
        knights_instance["red_knight"].name: knights_instance["red_knight"].hp,
    }
