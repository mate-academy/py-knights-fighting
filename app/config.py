# config.py
from models import Knight, Weapon, Armour, Potion

KNIGHTS = {
    "Lancelot": Knight(
        "Lancelot", 50, 80,
        [Armour("helmet", 10)],
        Weapon("Sword", 30),
        Potion("Strength", {"power": 5})
    ),
    "Mordred": Knight(
        "Mordred", 45, 90,
        [Armour("breastplate", 20)],
        Weapon("Axe", 35)
    ),
    "Arthur": Knight(
        "Arthur", 55, 85,
        [Armour("shield", 15)],
        Weapon("Sword", 25),
        Potion("Health", {"hp": 10})
    ),
    "Red Knight": Knight(
        "Red Knight", 40, 70,
        [Armour("breastplate", 25)],
        Weapon("Sword", 45),
        Potion("Blessing", {"hp": 10, "power": 5})
    ),
}
