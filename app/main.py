from app.knights_stats.create_knights import preparations
from app.knights_stats.general import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot, mordred, arthur, red_knight = preparations(knights_config)
    # ROUND 1
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # ROUND 2
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    for knight in [lancelot, mordred, arthur, red_knight]:
        knight.check_hp()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
