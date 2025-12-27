from app.knights.character import Knight
from app.battle import Battle
from app.knights.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    battle1 = Battle(lancelot, mordred).simulate()
    battle2 = Battle(arthur, red_knight).simulate()

    return {**battle1, **battle2}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
