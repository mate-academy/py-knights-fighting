from app.knight.knight import Knight
from app.armour.armour_part import ArmourPart
from app.weapon.weapon import Weapon
from app.potion.potion import Potion
from app.potion.effect import Effect


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
    knights = dict()

    for knight_dict in knights_config.values():
        armour = [ArmourPart(**armour_part)
                  for armour_part in knight_dict["armour"]
                  ]

        weapon = Weapon(**knight_dict["weapon"])

        if knight_dict["potion"] is None:
            potion = None
        else:
            potion = Potion(
                knight_dict["potion"]["name"],
                Effect(**knight_dict["potion"]["effect"])
            )

        knights[knight_dict["name"]] = Knight(
            name=knight_dict["name"],
            power=knight_dict["power"],
            hp=knight_dict["hp"],
            armour=armour,
            weapon=weapon,
            potion=potion
        )

        knights[knight_dict["name"]].apply_armour()
        knights[knight_dict["name"]].apply_weapon()
        knights[knight_dict["name"]].apply_potion()

    knights["Lancelot"].attack(knights["Mordred"])
    knights["Mordred"].attack(knights["Lancelot"])

    knights["Arthur"].attack(knights["Red Knight"])
    knights["Red Knight"].attack(knights["Arthur"])

    return {name: knights[name].hp for name in knights}


print(battle(KNIGHTS))
