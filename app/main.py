from app.characters.knights import KNIGHTS
from app.characters.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_list = []

    for key, value in knights_config.items():
        knight = Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            armour=value["armour"],
            weapon=value["weapon"],
            potion=value["potion"]
        )
        knight.get_ready()
        knights_list.append(knight)
    lancelot, arthur, mordred, red_knight = knights_list

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    lancelot.hp = 0 if lancelot.hp <= 0 else lancelot.hp

    mordred.hp = 0 if mordred.hp <= 0 else mordred.hp

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    arthur.hp = 0 if arthur.hp <= 0 else arthur.hp

    red_knight.hp = 0 if red_knight.hp <= 0 else red_knight.hp

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
