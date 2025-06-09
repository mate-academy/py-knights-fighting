from app.knights.knights import Knights
from app.knights.classes import Armour, Potion, Weapon


def knights_characteristics() -> list:
    armour_lancelot = []
    weapon_lancelot = Weapon("Metal Sword", 50)
    potion_lancelot = None
    lancelot = Knights(
        "Lancelot",
        35,
        100,
        armour_lancelot,
        weapon_lancelot,
        potion_lancelot
    )

    armour1_mordred = Armour("breasplate", 15)
    armour2_mordred = Armour("boots" , 10)
    armour_mordred = [armour1_mordred, armour2_mordred]
    weapon_mordred = Weapon("Poisoned Sword", 60)
    potion_mordred = Potion("Berserk", 15, -5, 10)
    mordred = Knights(
        "Mordred",
        30,
        90,
        armour_mordred,
        weapon_mordred,
        potion_mordred
    )

    armour1_arthur = Armour("helmet", 15)
    armour2_arthur = Armour("breastplate", 20)
    armour3_arthur = Armour("boots", 10)

    armour_arthur = [armour1_arthur, armour2_arthur, armour3_arthur]
    weapon_arthur = Weapon("Two-handed Sword", 55)
    potion_arthur = None
    arthur = Knights(
        "Arthur",
        45,
        75,
        armour_arthur,
        weapon_arthur,
        potion_arthur
    )

    armour_red_knight = [Armour("breasplate", 25)]
    weapon_red_knight = Weapon("Sword", 45)
    potion_red_knight = Potion("Blessing", 5, 10, 0)
    red_knight = Knights(
        "Red Knight",
        40,
        70,
        armour_red_knight,
        weapon_red_knight,
        potion_red_knight
    )
    knights = [lancelot, arthur, mordred, red_knight]
    return knights
