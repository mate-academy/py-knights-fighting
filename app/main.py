from app.battle.battle import Battle
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.protection import Protection
from app.knights.weapon import Weapon
from app.data.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []

    for knight in knights_config:
        knights.append(Knight.create_knight(knights_config[knight]))

    for knight in knights:
        Protection.apply_protection(knight)
        Weapon.apply_weapon(knight)
        Potion.apply_potion(knight)

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # # 1 Lancelot vs Mordred:
    Battle.begin_battle(lancelot, mordred)
    # # 2 Arthur vs Red Knight:
    Battle.begin_battle(arthur, red_knight)

    return Battle.result_of_battle(lancelot, arthur, mordred, red_knight)


print(battle(KNIGHTS))
