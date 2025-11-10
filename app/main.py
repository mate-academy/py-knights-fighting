from .knights_data import KNIGHTS
from .battle import Knight


def battle(knights_config: dict) -> None:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])
    lancelot.duel(mordred)
    arthur.duel(red_knight)

    results = {k.name: k.hp for k in [lancelot, arthur, mordred, red_knight]}
    return results


if __name__ == "__main__":
    print(battle(KNIGHTS))
