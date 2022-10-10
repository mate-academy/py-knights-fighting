from app.knights.class_of_knigts import Knights


def battle(knights_cof: dict):
    lancelot = Knights(knights_cof["lancelot"])
    arthur = Knights(knights_cof["arthur"])
    mordred = Knights(knights_cof["mordred"])
    red_knight = Knights(knights_cof["red_knight"])
    # Preparations:
    knights_list = [lancelot, arthur, mordred, red_knight]
    for knight in knights_list:
        knight.preparations()
    # BATTLE:
    lancelot.main_battle(mordred)
    arthur.main_battle(red_knight)
    # Return battle results:
    return {
        lord.name: lord.hp
        for lord in knights_list
    }
