from app.character.knight import Knight
from app.character.knight import default_knights
from app.battle.battling import BattleArea


def battle(knights_config):
    lancelot = Knight.from_dict(knights_config["lancelot"])
    arthur = Knight.from_dict(knights_config["arthur"])
    mordred = Knight.from_dict(knights_config["mordred"])
    red_knight = Knight.from_dict(knights_config["red_knight"])

    for k in [lancelot, arthur, mordred, red_knight]:
        k.ready_up()

    BattleArea.dual_hit(lancelot, mordred)
    BattleArea.dual_hit(arthur, red_knight)

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}


print(battle(default_knights))
