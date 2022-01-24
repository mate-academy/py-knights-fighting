from app.knights import KNIGHTS
from app.preparation_to_battle.preparation import Preparation
from app.battle.battle import Battle


def battle():
    # BATTLE PREPARATIONS:
    prepare = Preparation(KNIGHTS)

    lancelot = prepare.set_characteristics()
    arthur = prepare.set_characteristics()
    mordred = prepare.set_characteristics()
    red_knight = prepare.set_characteristics()

    # -------------------------------------------------------------------------------
    # BATTLE:
    first_battle = Battle.fight(lancelot, mordred)
    second_battle = Battle.fight(arthur, red_knight)

    result = first_battle.copy()
    result.update(second_battle)

    return result


print(battle())
