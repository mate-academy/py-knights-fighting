from knights.knight import Knight
from knights import stats


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Artur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}

lancelot = Knight(
    name=stats.get_name(KNIGHTS["lancelot"]),
    hp=stats.get_hp(KNIGHTS["lancelot"]),
    power=stats.get_power(KNIGHTS["lancelot"]),
    protection=stats.get_protection(KNIGHTS["lancelot"])
)
arthur = Knight(
    name=stats.get_name(KNIGHTS["arthur"]),
    hp=stats.get_hp(KNIGHTS["arthur"]),
    power=stats.get_power(KNIGHTS["arthur"]),
    protection=stats.get_protection(KNIGHTS["arthur"])
)
mordred = Knight(
    name=stats.get_name(KNIGHTS["mordred"]),
    hp=stats.get_hp(KNIGHTS["mordred"]),
    power=stats.get_power(KNIGHTS["mordred"]),
    protection=stats.get_protection(KNIGHTS["mordred"])
)
red_knight = Knight(
    name=stats.get_name(KNIGHTS["red_knight"]),
    hp=stats.get_hp(KNIGHTS["red_knight"]),
    power=stats.get_power(KNIGHTS["red_knight"]),
    protection=stats.get_protection(KNIGHTS["red_knight"])
)

battle_1 = lancelot.battle(mordred)
battle_2 = arthur.battle(red_knight)

print(battle_1)
print(battle_2)
