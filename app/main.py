from app.championship_of_knights.creation_of_knights import creation_of_knights
from app.championship_of_knights.knights_battle import knights_battle


def battle(knights_config: dict) -> dict:
    knights = creation_of_knights(knights_config)

    return {
        **knights_battle(knights["lancelot"], knights["mordred"]),
        **knights_battle(knights["arthur"], knights["red_knight"])
    }
