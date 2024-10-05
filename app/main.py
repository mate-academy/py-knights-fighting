from app.battle import Battle
from app.knights.input_characters import KNIGHTS
from app.knights.knights import Knight
from app.preparation.armour import Armour
from app.preparation.potion import Potion
from app.preparation.weapon import Weapon


"""
The KNIGHTS constant has been moved to a separate module with the
possibility of further expansion.
A preparation package has been created with modules related to battle
preparation moved there.
@staticmethod is used in classes to calculate changed characteristics.
* In main.py, 2 separate list comprehensions are used at the beginning of
the function to ensure that tests work correctly.
"""


def battle(knights_config: dict) -> dict:

    knights = [Knight(value) for value in knights_config.values()]

    for knight in knights:
        Armour.get_armour(knight, knight.armour)
        Weapon.get_weapon(knight, knight.weapon)
        Potion.get_potion(knight, knight.potion)

    Battle.start_battle(knights)

    lancelot, arthur, mordred, red_knight = knights

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
