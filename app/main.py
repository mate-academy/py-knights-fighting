from typing import Any

from pycodestyle import python_3000_raise_comma

from app.helpers.battle import Battle
from app.helpers.knights_config import KNIGHTS
from app.knights.knights import Character
from app.helpers.battle_preparation import BattlePreparation


def battle(knights_config: dict[Any]) -> dict[str, int]:

    lancelot_prep = BattlePreparation("lancelot", knights_config)
    lancelot = lancelot_prep.create_character()

    arthur_prep = BattlePreparation("arthur", knights_config)
    arthur = arthur_prep.create_character()

    mordred_prep = BattlePreparation("mordred", knights_config)
    mordred = mordred_prep.create_character()

    red_knight_prep = BattlePreparation("red_knight", knights_config)
    red_knight = red_knight_prep.create_character()


    # 1 Lancelot vs Mordred:
    battle1 = Battle(character_one=lancelot,
                     character_two=mordred)
    battle1.calculate_battle()

    # 2 Arthur vs Red Knight:
    battle2 = Battle(character_one=arthur,
                     character_two=red_knight)
    battle2.calculate_battle()

    # Return battle results:
    return {
        lancelot.name.capitalize(): lancelot.hp,
        arthur.name.capitalize(): arthur.hp,
        mordred.name.capitalize(): mordred.hp,
        red_knight.name.capitalize(): red_knight.hp,
    }


print(battle(KNIGHTS))
