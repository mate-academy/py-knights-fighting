from app.knights.class_Knights import KnightInstances
from app.knights.knights import KNIGHTS


def battle(knights: dict) -> dict:
    for knight_name, knight_data in knights.items():
        KnightInstances(knight_name, knight_data)

    lancelot = KnightInstances.instances.get("lancelot")
    mordred = KnightInstances.instances.get("mordred")
    arthur = KnightInstances.instances.get("arthur")
    red_knight = KnightInstances.instances.get("red_knight")

    lancelot.enter_method()
    mordred.enter_method()
    arthur.enter_method()
    red_knight.enter_method()

    lancelot.vs(mordred)
    mordred.vs(lancelot)
    arthur.vs(red_knight)
    red_knight.vs(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
