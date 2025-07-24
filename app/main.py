from app.battle.preparation import Preparation
from app.battle.battle import Battle


def battle(knights: dict) -> dict:
    lancelot = Preparation.set_knight(name="lancelot", knights=knights)
    arthur = Preparation.set_knight(name="arthur", knights=knights)
    mordred = Preparation.set_knight(name="mordred", knights=knights)
    red_knight = Preparation.set_knight(name="red_knight", knights=knights)

    new_battle = Battle()

    new_battle.set_pair(knight1=lancelot, knight2=mordred)
    new_battle.set_pair(knight1=arthur, knight2=red_knight)

    new_battle.fight()
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
