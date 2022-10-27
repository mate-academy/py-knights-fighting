from app.knight import Knight
from app.items import Item

lancelot = Knight("Lancelot", 35, 100)
lancelot.apply_weapon(Item.weapons[0])

arthur = Knight("Artur", 45, 75)
arthur.apply_armor([Item.armors[0], Item.armors[1], Item.armors[3]])
arthur.apply_weapon(Item.weapons[3])

mordred = Knight("Mordred", 30, 90)
mordred.apply_armor([Item.armors[1], Item.armors[2]])
mordred.apply_weapon(Item.weapons[1])
mordred.apply_potion(Item.potions[0]["name"])

red_knight = Knight("Red Knight", 40, 70)
red_knight.apply_armor([Item.armors[1]])
red_knight.apply_weapon(Item.weapons[2])
red_knight.apply_potion(Item.potions[1]["name"])

knights = [lancelot, mordred, arthur, red_knight]


# -------------------------------------------------------------------------------
# BATTLE:
def battle(knights_list: list):
    if len(knights_list) != 4:
        print(f"For Battle required 4 Kninghs, please invite not less or more 4")
    # Fights:
    result_list = []
    for i in range(0, len(knights_list), 2):
        print(f"Battle {knights_list[i].name} vs {knights_list[i + 1].name} has started!")
        while knights_list[i].hp >= 0 or knights_list[i+1].hp >= 0:
            knights_list[i].hp -= knights_list[i+1].power - knights_list[i].protection
            print(f"{knights_list[i+1].name} hit {knights_list[i].name} with power "
                  f"{knights_list[i+1].power - knights_list[i].protection}")
            knights_list[i+1].hp -= knights_list[i].power - knights_list[i+1].protection
            print(f"{knights_list[i].name} hit {knights_list[i+1].name} with power "
                  f"{knights_list[i].power - knights_list[i+1].protection}")
            print(f"{knights_list[i].name} : {knights_list[i].hp}, "
                  f"{knights_list[i+1].name} : {knights_list[i+1].hp}")
            if knights_list[i].hp <= 0:
                knights_list[i].hp = 0
                print(f"{knights_list[i].name} : {knights_list[i].hp}, "
                      f"{knights_list[i+1].name} : {knights_list[i+1].hp}")
                print(f"{knights_list[i].name} Lost!")
                result_list.append(f"{knights_list[i].name} Lost!, {knights_list[i + 1].name} Won!")
                break
            if knights_list[i+1].hp <= 0:
                knights_list[i+1].hp = 0
                print(f"{knights_list[i].name} : {knights_list[i].hp}, "
                      f"{knights_list[i+1].name} : {knights_list[i+1].hp}")
                print(f"{knights_list[i+1].name} Lost!")
                result_list.append(f"{knights_list[i+1].name} Lost!, {knights_list[i].name} Won!")
                break

    # Return battle results:
    return result_list


print(battle(knights))
