from .knight import Knight
from .equipment import Armour, Weapon, Potion

KNIGHTS = {
    "Lancelot": Knight(
        name="Lancelot",
        base_power=60,
        base_hp=280,
        armours=[Armour("Shield", 20)],
        weapon=Weapon("Spear", 15),
        potion=Potion(
            "Cursed Brew",
            {"power": -10, "protection": +5},
        ),
    ),
    "Arthur": Knight(
        name="Arthur",
        base_power=50,
        base_hp=300,
        armours=[Armour("Helmet", 10), Armour("Boots", 5)],
        weapon=Weapon("Excalibur", 25),
        potion=Potion(
            "Health Potion",
            {"hp": +50},
        ),
    ),
    "Mordred": Knight(
        name="Mordred",
        base_power=55,
        base_hp=290,
        armours=[],
        weapon=Weapon("Dark Blade", 30),
        potion=None,
    ),
    "Red Knight": Knight(
        name="Red Knight",
        base_power=45,
        base_hp=320,
        armours=[],
        weapon=Weapon("Mace", 20),
        potion=None,
    ),
}
