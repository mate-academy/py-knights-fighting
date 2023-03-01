from app.knights import knights
import app.battle_preparation as b_p
import app.battle as bat


def battle(knights_config):

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    b_p.battle_preparation(red_knight, lancelot, arthur, mordred)
    bat.duel(lancelot, mordred)
    bat.duel(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights))
