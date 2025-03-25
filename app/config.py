from entities import Armour, Weapon, Potion, Knight

KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        power=35,
        hp=100,
        armour=[],
        weapon=Weapon(name="Metal Sword", power=50),
    ),
    "arthur": Knight(
        name="Arthur",
        power=45,
        hp=75,
        armour=[
            Armour(part="helmet", protection=15),
            Armour(part="breastplate", protection=20),
            Armour(part="boots", protection=10),
        ],
        weapon=Weapon(name="Two-handed Sword", power=55),
    ),
    "mordred": Knight(
        name="Mordred",
        power=30,
        hp=90,
        armour=[
            Armour(part="breastplate", protection=15),
            Armour(part="boots", protection=10),
        ],
        weapon=Weapon(name="Poisoned Sword", power=60),
        potion=Potion(
            name="Berserk",
            effect={"power": +15, "hp": -5, "protection": +10},
        ),
    ),
    "red_knight": Knight(
        name="Red Knight",
        power=40,
        hp=70,
        armour=[
            Armour(part="breastplate", protection=25),
        ],
        weapon=Weapon(name="Sword", power=45),
        potion=Potion(
            name="Blessing",
            effect={"hp": +10, "power": +5},
        ),
    ),
}
