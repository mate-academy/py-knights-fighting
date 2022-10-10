from app.knights.class_of_knigts import Knights
from app.knights import fight_rules


def battle(knights_cof: dict) -> dict:
    lancelot = Knights(knights_cof["lancelot"])
    arthur = Knights(knights_cof["arthur"])
    mordred = Knights(knights_cof["mordred"])
    red_knight = Knights(knights_cof["red_knight"])
    # Preparations:
    knights_list = [lancelot, arthur, mordred, red_knight]
    for knight in knights_list:
        knight.preparations()
    # BATTLE:
    fight_rules.main_battle(lancelot, mordred)
    fight_rules.main_battle(arthur, red_knight)
    # Return battle results:
    return {
        lord.name: lord.hp
        for lord in knights_list
    }
