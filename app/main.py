from app.battle.preparing_to_battle import preparing_to_battle
from app.split_dicts import split_dict1


# BATTLE:
def battle(knights: dict) -> dict:
    prepared = preparing_to_battle(knights)
    pairs = split_dict1(prepared)
    results = {}
    for pair in pairs:
        gladiator_1, gladiator_2 = list(pair.values())
        # 1 knight_1 vs knight_2:
        gladiator_1.hp -= gladiator_2.power - gladiator_1.protection
        gladiator_2.hp -= gladiator_1.power - gladiator_2.protection

        # check if someone fell in battle
        if gladiator_1.hp <= 0:
            gladiator_1.hp = 0

        if gladiator_2.hp <= 0:
            gladiator_2.hp = 0

        results.update({
            gladiator_1.name: gladiator_1.hp,
            gladiator_2.name: gladiator_2.hp
        })
    order = ["Lancelot", "Arthur", "Mordred", "Red Knight"]
    results_updated = {k: results[k] for k in order}
    return results_updated
