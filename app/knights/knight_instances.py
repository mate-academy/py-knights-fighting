from __future__ import annotations
from app.buffs.armour import Armour
from app.buffs.weapon import Weapon
from app.buffs.potion import Potion
from app.knights.knight_prototype import Knight

lancelot = Knight(
    name="Lancelot",
    power=35,
    hp=100,
    weapon=Weapon("Metal Sword", 50),
)

arthur_armour = [
    Armour(part="helmet", protection=15),
    Armour(part="breastplate", protection=20),
    Armour(part="boots", protection=10)
]
arthur = Knight(
    name="Arthur",
    power=45,
    hp=75,
    weapon=Weapon(name="Two-handed Sword", power=55),
    armour=arthur_armour,
)

mordred_armour = [
    Armour(part="breastplate", protection=15),
    Armour(part="boots", protection=10)
]
mordred = Knight(
    name="Mordred",
    power=45,
    hp=75,
    weapon=Weapon(name="Poisoned Sword", power=60),
    armour=mordred_armour,
    potion=Potion(
        name="Berserk",
        power=+15,
        protection=+10,
        hp=-5
    )
)

red_knight_armour = [
    Armour(part="breastplate", protection=25)
]

red_knight = Knight(
    name="Red Knight",
    power=40,
    hp=70,
    weapon=Weapon(name="Sword", power=45),
    armour=red_knight_armour,
    potion=Potion(
        name="Blessing",
        power=+5,
        hp=+10
    )
)
