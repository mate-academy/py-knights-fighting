from app.items import Weapon, Armour, Potion, PotionEffect
from app.knight import Knight


def get_knights() -> dict:
    knights = {
        "lancelot": Knight("Lancelot", 35, 100, Weapon("Metal Sword", 50)),
        "arthur": Knight(
            "Arthur",
            45,
            75,
            Weapon("Two-handed Sword", 55),
            [
                Armour("helmet", 15),
                Armour("breastplate", 20),
                Armour("boots", 10),
            ],
        ),
        "mordred": Knight(
            "Mordred",
            30,
            90,
            Weapon("Poisoned Sword", 60),
            [Armour("breastplate", 15), Armour("boots", 10)],
            Potion("Berserk", PotionEffect(-5, 15, 10)),
        ),
        "red_knight": Knight(
            "Red Knight",
            40,
            70,
            Weapon("Sword", 45),
            [Armour("breastplate", 25)],
            Potion("Blessing", PotionEffect(10, 5, 0)),
        ),
    }
    return knights
