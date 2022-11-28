from app.battle.battle_preparations import Knight


def battle(knights_config: dict) -> dict:

    arthur = knights_config["arthur"]
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    arthur_ready = Knight(knight=arthur)
    arthur_ready.get_ready()

    lancelot_ready = Knight(knight=lancelot)
    lancelot_ready.get_ready()

    mordred_ready = Knight(knight=mordred)
    mordred_ready.get_ready()

    red_knight_ready = Knight(knight=red_knight)
    red_knight_ready.get_ready()

    lancelot_ready.battle_start(mordred_ready)
    arthur_ready.battle_start(red_knight_ready)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
