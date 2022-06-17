from app.battle.new_battle import Battle
from app.knight.new_knight import Knight

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
        "name": "Artur",
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

    # lancelot
    lancelot = Knight("Lancelot",
                      knightsConfig["lancelot"]["power"],
                      knightsConfig["lancelot"]["hp"]
                      )

    # apply armour
    lancelot.armour(knightsConfig["lancelot"]["armour"])

    # apply weapon
    lancelot.weapon(knightsConfig["lancelot"]["weapon"])

    # apply potion if exist
    lancelot.potion(knightsConfig["lancelot"]["potion"])

    # arthur
    arthur = Knight("Artur",
                    knightsConfig["arthur"]["power"],
                    knightsConfig["arthur"]["hp"]
                    )

    # apply armour
    arthur.armour(knightsConfig["arthur"]["armour"])

    # apply weapon
    arthur.weapon(knightsConfig["arthur"]["weapon"])

    # apply potion if exist
    arthur.potion(knightsConfig["arthur"]["potion"])

    # mordred
    mordred = Knight("Mordred",
                     knightsConfig["mordred"]["power"],
                     knightsConfig["mordred"]["hp"]
                     )

    # apply armour
    mordred.armour(knightsConfig["mordred"]["armour"])

    # apply weapon
    mordred.weapon(knightsConfig["mordred"]["weapon"])

    # apply potion if exist
    mordred.potion(knightsConfig["mordred"]["potion"])

    # red_knight
    red_knight = Knight("Red Knight",
                        knightsConfig["red_knight"]["power"],
                        knightsConfig["red_knight"]["hp"]
                        )

    # apply armour
    red_knight.armour(knightsConfig["red_knight"]["armour"])

    # apply weapon
    red_knight.weapon(knightsConfig["red_knight"]["weapon"])

    # apply potion if exist
    red_knight.potion(knightsConfig["red_knight"]["potion"])

    # -------------------------------------------------------------------------------
    # BATTLE:
    fight = Battle()
    # 1 Lancelot vs Mordred:
    fight_one = fight.knight_battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight_two = fight.knight_battle(arthur, red_knight)

    fight_one.update(fight_two)
    # Return battle results:
    return fight_one


print(battle(KNIGHTS))
