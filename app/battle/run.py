from app.battle.knight import Knight
from app.battle.data import knights_dict

knights = [lancelot, arthur, mordred, red_knight] = [
    Knight(
        knight["name"],
        knight["power"],
        knight["hp"],
        knight["armour"],
        knight["weapon"],
        knight["potion"]
    )
    for knight in knights_dict.values()
]

for knight in knights:
    Knight.applying(knight)

lancelot.hp -= mordred.power - lancelot.protection
mordred.hp -= lancelot.power - mordred.protection
arthur.hp -= red_knight.power - arthur.protection
red_knight.hp -= arthur.power - red_knight.protection


def battle(list_of_nights):
    for ls in list_of_nights:
        if ls.hp <= 0:
            ls.hp = 0
    return {ls.name: ls.hp for ls in list_of_nights}


print(battle(knights))
