from app.knight import Knight, fight
from app.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_dict(knights_config["lancelot"])
    arthur = Knight.from_dict(knights_config["arthur"])
    mordred = Knight.from_dict(knights_config["mordred"])
    red_knight = Knight.from_dict(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
