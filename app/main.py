from app.config_fighters.setting_knights import setting_knight
from app.knights import arthur_stats, lancelot_stats
from app.knights import mordred_stats, red_knight_stats
from app.setting_battle.battle import battle_knight


knights = {"lancelot": lancelot_stats,
           "arthur": arthur_stats,
           "mordred": mordred_stats,
           "red_knight": red_knight_stats}


def battle(knights_dic):
    lancelot = setting_knight(knights_dic["lancelot"])
    arthur = setting_knight(knights_dic["arthur"])
    red_knight = setting_knight(knights_dic["red_knight"])
    mordred = setting_knight(knights_dic["mordred"])

    battle_1 = battle_knight(lancelot, mordred)

    battle_2 = battle_knight(arthur, red_knight)

    return battle_1 | battle_2
