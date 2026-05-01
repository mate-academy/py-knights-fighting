from app.knights_presenting import knights
from app.knights_preparing import knights_preparing
from app.knights_fighting import knights_fighting


def battle(knights_config: dict) -> dict:

    for knight in list(knights_config.values()):
        knights_preparing(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    knights_fighting(lancelot, mordred)
    knights_fighting(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights))
