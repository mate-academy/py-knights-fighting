from app.people.KNIGHTS import KNIGHTS
from app.transform import transform_knights


def battle(knights: dict) -> dict:
    list_of_knights = transform_knights(knights)
    lancelot = list_of_knights[0].equip()
    arthur = list_of_knights[1].equip()
    mordred = list_of_knights[2].equip()
    red_knight = list_of_knights[3].equip()
    lancelot.fight(mordred)
    arthur.fight(red_knight)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
