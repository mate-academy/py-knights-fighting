from app.knight_config import KNIGHTS
from app.knight import Knight


def battle(knights_config):
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Fight 1: Lancelot vs Mordred
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # Fight 2: Arthur vs Red Knight
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
