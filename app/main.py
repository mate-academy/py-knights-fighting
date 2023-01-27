from app.knights.data_knights import knights
from app.knights.ready_knights import create_knight


def battle(knights: dict) -> dict:

    # створимо кожного з лицарів та спорядимо їх до бою:

    lancelot = create_knight("lancelot", knights)
    mordred = create_knight("mordred", knights)
    arthur = create_knight("arthur", knights)
    red_knight = create_knight("red_knight", knights)

    lancelot.gear_up()
    mordred.gear_up()
    arthur.gear_up()
    red_knight.gear_up()

    # проведемо двобої та виведемо їх результати:

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
