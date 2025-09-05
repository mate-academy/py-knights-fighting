from app.combatant import Combatant


def duel(blue: Combatant, red: Combatant) -> None:
    blue.hp -= red.power - blue.protection
    red.hp -= blue.power - red.protection

    # check if someone fell in battle
    if blue.hp <= 0:
        blue.hp = 0

    if red.hp <= 0:
        red.hp = 0
