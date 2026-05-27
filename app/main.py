from app.equips.armour import Armour
from app.equips.potion import Potion
from app.equips.weapon import Weapon
from app.warriors.knights import Knight
from app.Fight.battle import conducting_battle


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


def battle(knights_config: dict) -> dict:
    knight_objects = {}

    for key, value in knights_config.items():
        armour_pieces = [Armour(**piece) for piece in value["armour"]]
        weapon_obj = Weapon(**value["weapon"])
        potion_obj = Potion(**value["potion"]) if value["potion"] else None

        knight_objects[key] = Knight(
            name=value["name"],
            base_power=value["power"],
            base_hp=value["hp"],
            armour=armour_pieces,
            weapon=weapon_obj,
            potion=potion_obj
        )

        knight_objects[key].prepare_for_battle()

    lancelot = knight_objects["lancelot"]
    red_knight = knight_objects["red_knight"]
    arthur = knight_objects["arthur"]
    mordred = knight_objects["mordred"]

    conducting_battle(lancelot, mordred)
    conducting_battle(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        red_knight.name: red_knight.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
    }
