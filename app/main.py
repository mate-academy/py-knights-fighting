from app.battle.before_battle import Knight
from app.battle.knights_info import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    after_battle = [lancelot, mordred, arthur, red_knight]
    for knight in after_battle:
        if knight.hp <= 0:
            knight.hp = 0

        return {
            lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp
        }


print(battle(KNIGHTS))
