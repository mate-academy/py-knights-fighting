from app.stuff.stuff import used_armor, used_weapon, used_potion
from app.knights.characteristic import KNIGHTS
from app.fight.fight import fight


def battle(knights_equip):
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knights_equip["lancelot"]
    used_armor(lancelot)
    used_weapon(lancelot)
    used_potion(lancelot)

    # arthur
    arthur = knights_equip["arthur"]
    used_armor(arthur)
    used_weapon(arthur)
    used_potion(arthur)

    # mordred
    mordred = knights_equip["mordred"]
    used_armor(mordred)
    used_weapon(mordred)
    used_potion(mordred)

    # red_knight
    red_knight = knights_equip["red_knight"]
    used_armor(red_knight)
    used_weapon(red_knight)
    used_potion(red_knight)

    # BATTLE:
    fight1 = fight(lancelot, mordred)
    fight2 = fight(arthur, red_knight)
    fight1.update(fight2)
    return fight1


print(battle(KNIGHTS))
