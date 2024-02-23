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


def battle(knights: dict) -> dict:
    dictionary_of_knights = {}
    for knight_name, knight_data in knights.items():
        knight_instance = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armour=[Armour(armour) for armour in knight_data["armour"]],
            weapon=Weapon(knight_data["weapon"]),
            potion=Potion(knight_data["potion"]),
        )
        dictionary_of_knights[knight_name] = knight_instance

    for knight in dictionary_of_knights:
        dictionary_of_knights.get(knight).prepare_for_the_fight()
        dictionary_of_knights.get(knight).apply_potion()

    lancelot = dictionary_of_knights.get("lancelot")
    mordred = dictionary_of_knights.get("mordred")
    arthur = dictionary_of_knights.get("arthur")
    red_knight = dictionary_of_knights.get("red_knight")

    lancelot.fight_and_apply_damage(mordred)
    mordred.fight_and_apply_damage(lancelot)
    arthur.fight_and_apply_damage(red_knight)
    red_knight.fight_and_apply_damage(arthur)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
