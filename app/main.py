from app.declarations.battle_configs import Default
from app.knight.knight import Knight


def battle(knight_configs=Default):
    # BATTLE PREPARATIONS:
    knights = [Knight(knight_config) for knight_config in knight_configs]

    # BATTLE:
    index = 0
    while index < len(knights) - 1:
        print(f"{knights[index].name} is attacking {knights[index + 1].name}")
        knights[index].attack(knights[index + 1])
        if knights[index + 1].hp > 0:
            print(f"{knights[index + 1].name} has {knights[index + 1].hp}hp left.")
        else:
            knights[index + 1].hp = 0
            print(f"{knights[index + 1].name} has fallen.")
            index += 2
            continue

        print(f"{knights[index + 1].name} is attacking {knights[index].name}")
        knights[index + 1].attack(knights[index])
        if knights[index].hp > 0:
            print(f"{knights[index].name} has {knights[index].hp}hp left.")
        else:
            knights[index].hp = 0
            print(f"{knights[index].name} has fallen.")
            index += 2
            continue

        index += 2

    return {
        knight.name: knight.hp
        for knight in knights
    }


print(battle())
