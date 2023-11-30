from app.utils import (
    make_fight,
    check_health,
    make_preparations
)


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    make_preparations(lancelot, arthur, mordred, red_knight)

    make_fight(lancelot, mordred)
    check_health(lancelot, mordred)

    make_fight(arthur, red_knight)
    check_health(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
