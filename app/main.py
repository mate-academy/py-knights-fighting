from app.knight import Knight


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
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights["lancelot"])

    # apply armour
    lancelot.apply_armour()

    # apply weapon
    lancelot.apply_weapon()

    # apply potion if exist
    lancelot.apply_potion()

    # arthur
    arthur = Knight(knights["arthur"])

    # apply armour
    arthur.apply_armour()

    # apply weapon
    arthur.apply_weapon()

    # apply potion if exist
    arthur.apply_potion()

    # mordred
    mordred = Knight(knights["mordred"])

    # apply armour
    mordred.apply_armour()

    # apply weapon
    mordred.apply_weapon()

    # apply potion if exist
    mordred.apply_potion()

    # red_knight
    red_knight = Knight(knights["red_knight"])

    # apply armour
    red_knight.apply_armour()

    # apply weapon
    red_knight.apply_weapon()

    # apply potion if exist
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # check if someone fell in battle
    lancelot.is_alive()
    mordred.is_alive()

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # check if someone fell in battle
    arthur.is_alive()
    red_knight.is_alive()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
