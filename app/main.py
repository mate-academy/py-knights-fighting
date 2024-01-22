# main.py
from knight import Knight
from battle import Battle

KNIGHTS = {
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
    "lancelot": {
        "name": "Lancelot",
        "power": 50,
        "hp": 80,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "shield",
                "protection": 20,
            }
        ],
        "weapon": {"name": "Lance", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 60,
        "hp": 75,
        "armour": [
            {
                "part": "breastplate",
                "protection": 30,
            }
        ],
        "weapon": {"name": "Axe", "power": 60},
        "potion": {
            "name": "Curse",
            "effect": {
                "hp": -5,
                "power": +10,
            },
        },
    },
    "arthur": {
        "name": "Arthur",
        "power": 55,
        "hp": 85,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {"name": "Excalibur", "power": 65},
        "potion": {
            "name": "Healing",
            "effect": {
                "hp": +15,
                "power": 0,
            },
        },
    }
}


def main():
    # Create knights
    red_knight = Knight(**KNIGHTS["red_knight"])
    lancelot = Knight(**KNIGHTS["lancelot"])
    mordred = Knight(**KNIGHTS["mordred"])
    arthur = Knight(**KNIGHTS["arthur"])

    # Create battles
    battle1 = Battle(lancelot, mordred)
    battle2 = Battle(arthur, red_knight)

    # Conduct battles
    print(battle1.conduct())
    print(battle2.conduct())


if __name__ == "__main__":
    main()
