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

    for fighter in Knights.listknights:
        if len(fighter.armour) != 0:
            KnightsPrep.count_protection(fighter)

    for fighter in Knights.listknights:
        KnightsPrep.count_power(fighter)

    for fighter in Knights.listknights:
        KnightsPrep.apply_potion(fighter)

    lancelot = 0
    arthur = 0
    mordred = 0
    red_knight = 0

    for fighter in Knights.listknights:
        if fighter.name == "Lancelot":
            lancelot = fighter
        if fighter.name == "Artur":
            arthur = fighter
        if fighter.name == "Mordred":
            mordred = fighter
        if fighter.name == "Red Knight":
            red_knight = fighter

    KnightBattle.battle(lancelot, mordred)
    KnightBattle.battle(arthur, red_knight)

    KnightBattle.chek_hp(lancelot, mordred, arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
