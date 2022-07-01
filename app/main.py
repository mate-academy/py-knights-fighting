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



from app.solution.knights_creation import Knights
from app.solution.dict_transformation import transformation


def battle(kn_dict: dict):
    l = transformation("lancelot", kn_dict)
    lancelot = Knights(l[0], l[1], l[2], l[3])
    a = transformation("arthur", kn_dict)
    arthur = Knights(a[0], a[1], a[2], a[3])
    m = transformation("mordred", kn_dict)
    mordred = Knights(m[0], m[1], m[2], m[3])
    r = transformation("red_knight", kn_dict)
    red_knight = Knights(r[0], r[1], r[2], r[3])
    lancelot.one_battle(mordred)
    arthur.one_battle(red_knight)
    heroes = [arthur, lancelot, mordred, red_knight]
    result = {hero.name: hero.hp for hero in heroes}
    return result
