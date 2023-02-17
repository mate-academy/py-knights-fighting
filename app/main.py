from app.config import KNIGHTS
from app.fight.knight import Knight
from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


def battle(knights_config: dict) -> dict:
    knights = {}

    for knight_data in knights_config.values():
        name = knight_data.get("name")
        hp = knight_data.get("hp")
        power = knight_data.get("power")
        all_armour = [
            Armour(armour["part"], armour["protection"])
            for armour in knight_data.get("armour")
        ]
        weapon = knight_data.get("weapon")
        potion = knight_data.get("potion")

        params = [
            name,
            hp,
            power,
            all_armour,
        ]

        if weapon is not None:
            params.append(Weapon(weapon["name"], weapon["power"]))

        if potion is not None:
            params.append(Potion(potion["name"], potion["effect"]))

        new_knight = Knight(*params)
        knights[name] = new_knight

    lancelot = knights.get("Lancelot")
    arthur = knights.get("Artur")
    mordred = knights.get("Mordred")
    red_knight = knights.get("Red Knight")

    Knight.fight(lancelot, mordred)
    Knight.fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
