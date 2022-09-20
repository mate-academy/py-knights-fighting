from app.setting_battle.setting_fight import setting_battle
from app.knights_config.setting_knights import setting_knight
from app.knights import arthur_stats, lancelot_stats
from app.knights import mordred_stats, red_knight_stats


knights = {
    "lancelot": lancelot_stats,
    "arthur": arthur_stats,
    "mordred": mordred_stats,
    "red_knight": red_knight_stats

}


def battle(knights_dict: dict):
    lancelot = setting_knight(knights_dict["lancelot"])
    mordred = setting_knight(knights_dict["mordred"])
    arthur = setting_knight(knights_dict["arthur"])
    red_knight = setting_knight(knights_dict["red_knight"])

    battle_1 = setting_battle(lancelot, mordred)
    battle_2 = setting_battle(arthur, red_knight)
    result = {**battle_1, **battle_2}
    return result
