from app.knights.ammunition import Armour, Potion, Weapon
from app.knights.knight import Knight
from app.battlefield.battle import Battle


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


def battle(knightsConfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights = Knight.knights_from_dict(knightsConfig)
    for i in range(4):
        knight = knights[i]
        armour = Armour.armours_from_dict(
            knight.tech_name, knightsConfig
        )
        weapon = Weapon.weapon_from_dict(
            knightsConfig[knight.tech_name]["weapon"]
        )
        potion = Potion.potion_from_dict(
            knightsConfig[knight.tech_name]["potion"]
        )
        knight.apply_armour(armour)
        knight.apply_weapon(weapon)
        knight.apply_potion(potion)

    # # lancelot
    # lancelot_dict = knightsConfig["lancelot"]
    # lancelot = Knight.knight_from_dict(lancelot_dict)
    # lancelot.apply_armour(lancelot_dict["armour"])
    # lancelot.apply_weapon(lancelot_dict["weapon"])
    # lancelot.apply_potion(lancelot_dict["potion"])

    # # arthur
    # arthur_dict = knightsConfig["arthur"]
    # arthur = Knight.knight_from_dict(arthur_dict)
    # arthur.apply_armour(arthur_dict["armour"])
    # arthur.apply_potion(arthur_dict["potion"])
    # arthur.apply_weapon(arthur_dict["weapon"])

    # # # mordred
    # mordred_dict = knightsConfig["mordred"]
    # mordred = Knight.knight_from_dict(mordred_dict)
    # mordred.apply_armour(mordred_dict["armour"])
    # mordred.apply_potion(mordred_dict["potion"])
    # mordred.apply_weapon(mordred_dict["weapon"])

    # # # red_knight
    # red_knight_dict = knightsConfig["red_knight"]
    # red_knight = Knight.knight_from_dict(red_knight_dict)
    # red_knight.apply_armour(red_knight_dict["armour"])
    # red_knight.apply_potion(red_knight_dict["potion"])
    # red_knight.apply_weapon(red_knight_dict["weapon"])

    # # ------------------------------------------------
    # BATTLE:
    lancelot, arthur, mordred, red_knight = knights
    pair_1 = Battle(lancelot, mordred)
    pair_2 = Battle(arthur, red_knight)
    pair_1.battle()
    pair_2.battle()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
