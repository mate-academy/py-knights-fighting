from app.game.armour import Armour
from app.game.Weapon import Weapon
from app.game.Potion import Potion

slem = Armour("slem", 20)
bronia = Armour("bronia", 45)

metal_sword = Weapon("Metal Sword", 50)
sword = Weapon("Sword", 45)

blessing = Potion("Blessing", {"hp": 10, "power": 5})

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [slem, bronia],
        "weapon": metal_sword,
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [Armour("shoulder", 15)],
        "weapon": Weapon("Excalibur", 60),
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 55,
        "hp": 90,
        "armour": [Armour("helmet", 20)],
        "weapon": Weapon("Dark Sword", 40),
        "potion": None,
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [Armour("breastplate", 25)],
        "weapon": sword,
        "potion": blessing,
    },
}