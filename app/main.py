
from app.config import KNIGHTS
from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {}
    for name, data in knights_config.items():
        knight = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"]
        )
        knights[name] = knight
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.take_damage(mordred)
    mordred.take_damage(lancelot)

    arthur.take_damage(red_knight)
    red_knight.take_damage(arthur)

    results = {}
    for name, knight in knights.items():
        results[knight.name] = knight.hp

    return results


if __name__ == "__main__":
    print(battle(KNIGHTS))
