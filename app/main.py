from app.fighting import Arena
from app.knights import Knight
from app.main_dictionary import KNIGHTS


def battle(knights: dict) -> dict:
    list_knights = []
    for key, value in knights.items():
        knight = Knight(value["name"], value["power"], value["hp"])
        knight.use_weapon(value["weapon"]["power"])
        knight.use_armour(value["armour"])
        knight.use_potion(value["potion"])
        list_knights.append(knight)

    fight_1 = Arena.fight(list_knights[0], list_knights[2])
    fight_2 = Arena.fight(list_knights[1], list_knights[3])

    return {
        "Lancelot": fight_1["Lancelot"],
        "Artur": fight_2["Artur"],
        "Mordred": fight_1["Mordred"],
        "Red Knight": fight_2["Red Knight"],
    }


print(battle(KNIGHTS))
