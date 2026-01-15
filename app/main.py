from app.knight import Knight
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
