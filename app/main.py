from app.Knight.potion import Potion
from app.Knight.weapon import Weapon
from app.Knight.armour import ArmourPart
from app.Knight.knight import Knight


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


def create_knight(knight_config: dict) -> Knight:
    gun = Weapon(
        knight_config["weapon"]["name"],
        knight_config["weapon"]["power"]
    )
    shield = []
    for part in knight_config["armour"]:
        armor = ArmourPart(part["part"], part["protection"])
        shield.append(armor)
    potion = None
    if knight_config["potion"] is not None:
        potion = Potion(
            knight_config["potion"]["name"],
            knight_config["potion"]["effect"]
        )
    return Knight(knight_config["name"],
                  knight_config["power"],
                  knight_config["hp"],
                  shield,
                  gun,
                  potion
                  )


def battle(knights_config: dict) -> dict:
    knights = {}
    for name, config in knights_config.items():
        knight = create_knight(config)
        knight.calculate_stats()
        knights[name] = knight

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
