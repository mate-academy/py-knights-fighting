from app.fighter.knight_definition import Knight
from app.fight.if_fall import Fall

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


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    lancelot = Knight(knightsConfig["lancelot"]["name"],
                      knightsConfig["lancelot"]["power"],
                      knightsConfig["lancelot"]["hp"],
                      knightsConfig["lancelot"]["armour"],
                      knightsConfig["lancelot"]["weapon"],
                      knightsConfig["lancelot"]["potion"])
    lancelot.prepare_knight()

    arthur = Knight(knightsConfig["arthur"]["name"],
                    knightsConfig["arthur"]["power"],
                    knightsConfig["arthur"]["hp"],
                    knightsConfig["arthur"]["armour"],
                    knightsConfig["arthur"]["weapon"],
                    knightsConfig["arthur"]["potion"])
    arthur.prepare_knight()

    mordred = Knight(knightsConfig["mordred"]["name"],
                     knightsConfig["mordred"]["power"],
                     knightsConfig["mordred"]["hp"],
                     knightsConfig["mordred"]["armour"],
                     knightsConfig["mordred"]["weapon"],
                     knightsConfig["mordred"]["potion"])
    mordred.prepare_knight()

    red_knight = Knight(knightsConfig["red_knight"]["name"],
                        knightsConfig["red_knight"]["power"],
                        knightsConfig["red_knight"]["hp"],
                        knightsConfig["red_knight"]["armour"],
                        knightsConfig["red_knight"]["weapon"],
                        knightsConfig["red_knight"]["potion"])
    red_knight.prepare_knight()
    # Battle
    Fall.change_hp(lancelot, mordred.power)
    Fall.change_hp(mordred, lancelot.power)
    Fall.change_hp(arthur, red_knight.power)
    Fall.change_hp(red_knight, arthur.power)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
