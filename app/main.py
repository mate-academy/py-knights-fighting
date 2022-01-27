from knights.kClass import Knights
from battles.battle import KnightBattle
from battles.preparation import KnightsPrep


def battle(knightslist):
    for key in knightslist:
        Knights(
            knightslist[key]["name"],
            knightslist[key]["power"],
            knightslist[key]["hp"],
            knightslist[key]["armour"],
            knightslist[key]["weapon"],
            knightslist[key]["potion"]
        )

    for i in Knights.listknights:
        if len(i.armour) != 0:
            KnightsPrep.count_protection(i)

    for i in Knights.listknights:
        KnightsPrep.count_power(i)

    for i in Knights.listknights:
        KnightsPrep.apply_potion(i)

    lancelot = 0
    arthur = 0
    mordred = 0
    red_knight = 0

    for i in Knights.listknights:
        if i.name == "Lancelot":
            lancelot = i
        if i.name == "Artur":
            arthur = i
        if i.name == "Mordred":
            mordred = i
        if i.name == "Red Knight":
            red_knight = i

    KnightBattle.battle(lancelot, mordred)
    KnightBattle.battle(arthur, red_knight)

    KnightBattle.chek_hp(lancelot, mordred, arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
