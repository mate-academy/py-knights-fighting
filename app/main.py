from app.knights.armour import Armour
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.weapon import Weapon

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


def make_knight(config):
    armour = [Armour(a["part"], a["protection"]) for a in config["armour"]]
    weapon = Weapon(config["weapon"]["name"], config["weapon"]["power"])
    potion = None
    if config["potion"] is not None:
        potion = Potion(config["potion"]["name"], config["potion"]["effect"])
    return Knight(
        config["name"],
        config["power"],
        config["hp"],
        weapon,
        armour,
        potion,
    )


def battle(knights_config):
    lancelot = make_knight(knights_config["lancelot"])
    arthur = make_knight(knights_config["arthur"])
    mordred = make_knight(knights_config["mordred"])
    red_knight = make_knight(knights_config["red_knight"])

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        knight.name: knight.total_hp
        for knight in (lancelot, arthur, mordred, red_knight)
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
