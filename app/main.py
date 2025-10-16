from app.game.knight import Knight
from app.game.armour import Armour
from app.game.weapon import Weapon
from app.game.potion import Potion
from app.game.battle import Battle

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


def create_knights(knight_keys: dict) -> Knight:
    armour = [Armour(items["part"], items["protection"])
              for items in knight_keys["armour"]]

    weapon = knight_keys["weapon"]
    weapon = Weapon(weapon["name"], weapon["power"])

    potion = knight_keys["potion"]
    if potion:
        potion = Potion(potion["name"], potion["effect"])

    knight = Knight(name=knight_keys["name"],
                    power=knight_keys["power"],
                    hp=knight_keys["hp"],
                    armour=armour,
                    weapon=weapon,
                    potion=potion)

    return knight


def battle(knightsConfig: dict) -> dict:
    knights = []
    for key in knightsConfig:
        knight = create_knights(knightsConfig[key])
        knights.append(knight)

    battle_result = Battle.start_battle(knights[0], knights[1])
    battle_result.update(Battle.start_battle(knights[2], knights[3]))

    return battle_result


print(battle(KNIGHTS))
