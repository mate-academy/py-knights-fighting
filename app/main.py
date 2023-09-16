from app.knights.class_Knights import Knight
from app.knights.knights import KNIGHTS


def battle(knights: dict) -> dict:
    for knight_name, knight_data in knights.items():
        Knight(knight_name, knight_data)

    lancelot = Knight.instances.get("lancelot")
    mordred = Knight.instances.get("mordred")
    arthur = Knight.instances.get("arthur")
    red_knight = Knight.instances.get("red_knight")

    lancelot.prepare()
    mordred.prepare()
    arthur.prepare()
    red_knight.prepare()

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


print(battle(KNIGHTS))
