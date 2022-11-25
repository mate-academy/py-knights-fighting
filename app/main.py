from app.knight.knights import Knight


def battle(knights: dict) -> dict:
    knights_list = [Knight(knights[kn]) for kn in knights]
    for hero in knights_list:
        hero.apply_weapon()
        if hero.armour:
            hero.apply_armour()
        if hero.potion is not None:
            hero.apply_potion()
    for first in knights_list:
        if first.name == "Lancelot":
            for second in knights_list:
                if second.name == "Mordred":
                    first.assign_opponent(second)
        elif first.name == "Artur":
            for third in knights_list:
                if third.name == "Red Knight":
                    first.assign_opponent(third)
    battle_result = {}
    for knight in knights_list:
        knight.hp -= knight.opponent.power - knight.protection
        if knight.hp <= 0:
            knight.hp = 0
        battle_result.update({knight.name: knight.hp})
    return battle_result
