from app.config.knights import KNIGHTS
from app.services.battle import fight
from app.services.preparation import prepare_knight


def battle(knights_config: dict) -> dict:
    # Prepare all knights
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    # Lancelot vs Mordred
    fight(lancelot, mordred)

    # Arthur vs Red Knight
    fight(arthur, red_knight)

    # Return battle results
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
