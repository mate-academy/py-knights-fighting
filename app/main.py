from app.config_knights.setting_knights import setting_name
from app.logic_battle import battle_knight

from app.knights.lancelot import lancelot
from app.knights.red_knight import red_knight
from app.knights.arthur import arthur
from app.knights.mordred import mordred


knights = {"lancelot": lancelot,
           "red_knight": red_knight,
           "arthur": arthur,
           "mordred": mordred
           }


def battle(dict_knights):

    lancelot = setting_name(dict_knights["lancelot"])
    red_knight = setting_name(dict_knights["red_knight"])
    arthur = setting_name(dict_knights["arthur"])
    mordred = setting_name(dict_knights["mordred"])

    # 1 Lancelot vs Mordred:
    battle_1 = battle_knight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battle_2 = battle_knight(arthur, red_knight)

    # Return battle results:
    return battle_1 | battle_2


print(battle(knights))
