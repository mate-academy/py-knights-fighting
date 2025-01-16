from app.fight.fight import fight
from app.initializate.make_objects import init_input, make_knight_object

if __name__ == "__main__":
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
            "name": "Arthur",
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
    knights = KNIGHTS

    knight_objects = init_input(knights)
    knight_fighter = make_knight_object(knight_objects)
    ready_fighters = [item.prepare_to_fight() for item in knight_fighter]

    # show_info = show_ready_fighters(ready_fighters)
    # show_total_info = get_full_info(ready_fighters)
    fight(ready_fighters)
