from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.equipment.armour import Armour
from app.knights.knight import Knight
from app.battle import Battle

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


def create_knight(config: dict) -> "Knight":
    armour = [Armour(**item) for item in config.get("armour", [])]
    weapon = Weapon(**config["weapon"]) if config.get("weapon") else None
    potion = Potion(**config["potion"]) if config.get("potion") else None
    return Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knightsConfig: dict) -> dict:
    knight1 = create_knight(knightsConfig["lancelot"])
    knight2 = create_knight(knightsConfig["arthur"])
    knight3 = create_knight(knightsConfig["mordred"])
    knight4 = create_knight(knightsConfig["red_knight"])
    result = Battle.fight(knight1, knight3, knight2, knight4)
    return result


battle(KNIGHTS)
