from app.game.knights import Knight
from app.game.equipment.weapons import Weapon
from app.game.equipment.armors import Armor
from app.game.equipment.potions import Potion

KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        power=50,
        hp=100,
        armor=[Armor("helmet", 10), Armor("boots", 5)],
        weapon=Weapon("Sword", 30),
        potion=Potion("Healing", {"hp": 20}),
    ),
    "mordred": Knight(
        name="Mordred",
        power=55,
        hp=90,
        armor=[Armor("breastplate", 25)],
        weapon=Weapon("Axe", 35),
        potion=None,
    ),
    "arthur": Knight(
        name="Arthur",
        power=60,
        hp=110,
        armor=[Armor("shield", 20)],
        weapon=Weapon("Excalibur", 40),
        potion=Potion("Strength", {"power": 10}),
    ),
    "red_knight": Knight(
        name="Red Knight",
        power=40,
        hp=70,
        armor=[Armor("breastplate", 25)],
        weapon=Weapon("Sword", 45),
        potion=Potion("Blessing", {"hp": 10, "power": 5}),
    ),
}
