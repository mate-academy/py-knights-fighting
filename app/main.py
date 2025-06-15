from app.artifacts.armour import ArmourPart
from app.artifacts.knight import Knight
from app.artifacts.potion import Potion
from app.artifacts.weapon import Weapon
from app.battle_field.battle import BattleGround

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


def battle(knights_config):
    battle_ground = BattleGround()
    for knight in knights_config.values():
        the_knight = Knight(knight["name"], knight["power"], knight["hp"])

        for armour_part in knight["armour"]:
            the_knight.add_armour(ArmourPart(armour_part["part"], armour_part["protection"]))

        if not (knight["potion"] is None):
            potion = knight["potion"]
            potion_effect = potion["effect"]
            the_potion = Potion(
                potion["name"],
                potion_effect["power"] if "power" in potion_effect.keys() else 0,
                potion_effect["hp"] if "hp" in potion_effect.keys() else 0,
                potion_effect["protection"] if "protection" in potion_effect.keys() else 0,
            )

            the_knight.add_potion(the_potion)

        if not (knight["weapon"] is None):
            weapon = knight["weapon"]
            the_weapon = Weapon(weapon["name"], weapon["power"])

            the_knight.add_weapon(the_weapon)

        battle_ground.add_knight(the_knight)

    battle_ground.fight("Lancelot", "Mordred")
    battle_ground.fight("Arthur", "Red Knight")

    return battle_ground.results()


print(battle(KNIGHTS))
