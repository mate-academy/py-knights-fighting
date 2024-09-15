from app.prepare.knight import ReadyKnight
from app.prepare.armour import armour
from app.prepare.potion import drink_potion
from app.prepare.battle import battle_vs

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


def battle(knight_info: dict) -> dict:
    knights_ready = {}

    for key in knight_info.keys():
        # writing the knight's name for preparation
        knights_ready[key] = key
        # the medical board creates a knight's card
        knights_ready[key] = ReadyKnight(
            name=knight_info[key]["name"],
            hp=knight_info[key]["hp"],
            power=knight_info[key]["power"],
            protection=0
        )
        # Dressing the fighter in armor
        knights_ready[key].protection = armour(knight_info[key]["armour"])
        # drink a potion from a strange granny
        drink_potion(
            knight=knights_ready[key],
            potions=knight_info[key]["potion"]
        )
        # noble takes up arms
        knights_ready[key].power += knight_info[key]["weapon"]["power"]
    # trumpets announce Lancelot's fight against Mordred
    battle_vs(knights_ready["lancelot"], knights_ready["mordred"])
    # an exciting battle between Arthur and the Red Knight began
    battle_vs(knights_ready["arthur"], knights_ready["red_knight"])

    return {
        knights_ready["lancelot"].name: knights_ready["lancelot"].hp,
        knights_ready["arthur"].name: knights_ready["arthur"].hp,
        knights_ready["mordred"].name: knights_ready["mordred"].hp,
        knights_ready["red_knight"].name: knights_ready["red_knight"].hp
    }


print(battle(KNIGHTS))
