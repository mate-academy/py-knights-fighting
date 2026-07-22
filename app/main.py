from app.data import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_config(knights_config["lancelot"])
    arthur = Knight.from_config(knights_config["arthur"])
    mordred = Knight.from_config(knights_config["mordred"])
    red_knight = Knight.from_config(knights_config["red_knight"])

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
