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

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights_list[0].hp -= knights_list[2].power - knights_list[0].protection
    knights_list[2].hp -= knights_list[0].power - knights_list[2].protection

    # check if someone fell in battle
    if knights_list[0].hp <= 0:
        knights_list[0].hp = 0

    if knights_list[2].hp <= 0:
        knights_list[2].hp = 0

    # 2 Arthur vs Red Knight:
    knights_list[1].hp -= knights_list[3].power - knights_list[1].protection
    knights_list[3].hp -= knights_list[1].power - knights_list[3].protection

    # check if someone fell in battle
    if knights_list[1].hp <= 0:
        knights_list[1].hp = 0

    if knights_list[3].hp <= 0:
        knights_list[3].hp = 0

    # Return battle results:
    return {
        knights_list[0].name: knights_list[0].hp,
        knights_list[1].name: knights_list[1].hp,
        knights_list[2].name: knights_list[2].hp,
        knights_list[3].name: knights_list[3].hp,
    }


print(battle(KNIGHTS))
