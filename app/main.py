from app.battle import fight
from app.config import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


if __name__ == "__main__":
    result = battle(KNIGHTS)
    for name, hp in result.items():
        status = f"{hp} hp" if hp > 0 else "DEFEATED"
        print(f"{name}: {status}")
