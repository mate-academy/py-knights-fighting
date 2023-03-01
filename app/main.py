from app.knights import KNIGHTS
from app.preparation_to_battle.preparation import Preparation
from app.battle.battle import Battle


def battle():
    # BATTLE PREPARATIONS:
    prepare = Preparation(KNIGHTS)
    # set_characteristics = iter(prepare)

    lancelot = next(prepare)
    arthur = next(prepare)
    mordred = next(prepare)
    red_knight = next(prepare)

    # -------------------------------------------------------------------------------
    # BATTLE:
    first_battle = Battle.fight(lancelot, mordred)
    second_battle = Battle.fight(arthur, red_knight)

    result = first_battle.copy()
    result.update(second_battle)

    return result


print(battle())
