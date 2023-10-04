
from app.declarations.armour_parts import *
from app.declarations.weapon_types import *
from app.declarations.potions import *


Default = [
    {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": metal_sword,
        "potion": None,
    },
    {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            strong_helmet,
            average_breastplate,
            average_boots
        ],
        "weapon": two_handed_sword,
        "potion": None,
    },
    {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            weak_breastplate,
            average_boots
        ],
        "weapon": poisoned_sword,
        "potion": berserk
    },
    {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            strong_breastplate
        ],
        "weapon": sword,
        "potion": blessing
    }
]
