from app.camelot.configs import KNIGHTS
from app.camelot.knight import Knight


def battle(config: dict) -> dict:
    lancelot = Knight(config["lancelot"])
    arthur = Knight(config["arthur"])
    mordred = Knight(config["mordred"])
    red_knight = Knight(config["red_knight"])

    lancelot_vs_mordred_battle = lancelot.battle(mordred)
    arthur_vs_red_knight_battle = arthur.battle(red_knight)

    return {
        **lancelot_vs_mordred_battle,
        **arthur_vs_red_knight_battle
    }


print(battle(KNIGHTS))
