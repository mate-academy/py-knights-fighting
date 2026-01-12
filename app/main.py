from app.config import KNIGHTS
from app.models import Knight, Armour, Weapon, Potion


def battle(knights_config: dict) -> dict:
    knights = {}

    for name, data in knights_config.items():
        armour_list = [
            Armour(part=a["part"], protection=a["protection"])
            for a in data["armour"]
        ]

        weapon = Weapon(name=data["weapon"]["name"],
                        power=data["weapon"]["power"]
                        )

        potion = None
        if data["potion"]:
            potion = Potion(name=data["potion"]["name"],
                            effect=data["potion"]["effect"])

        knights[name] = Knight(
            name=data["name"],
            base_power=data["power"],
            hp=data["hp"],
            armour=armour_list,
            weapon=weapon,
            potion=potion
        )

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    lancelot.fight(mordred)
    mordred.fight(lancelot)

    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
