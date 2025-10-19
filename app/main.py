from app.knight.knight import Knight

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
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.from_dict(knights_config["lancelot"])

    # apply armour
    lancelot.apply_armour()

    # apply weapon
    lancelot.apply_weapon()

    # apply potion if exist
    lancelot.drink_potion()

    # arthur
    arthur = Knight.from_dict(knights_config["arthur"])

    # apply armour
    arthur.apply_armour()

    # apply weapon
    arthur.apply_weapon()

    # apply potion if exist
    arthur.drink_potion()

    # mordred
    mordred = Knight.from_dict(knights_config["mordred"])

    # apply armour
    mordred.apply_armour()

    # apply weapon
    mordred.apply_weapon()

    # apply potion if exist
    mordred.drink_potion()

    # red_knight
    red_knight = Knight.from_dict(knights_config["red_knight"])

    # apply armour
    red_knight.apply_armour()

    # apply weapon
    red_knight.apply_weapon()

    # apply potion if exist
    red_knight.drink_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.take_damage(mordred.total_power)
    mordred.take_damage(lancelot.total_power)

    # 2 Arthur vs Red Knight:
    arthur.take_damage(red_knight.total_power)
    red_knight.take_damage(arthur.total_power)

    # Return battle results:
    return {
        lancelot.name: lancelot.get_hp(),
        arthur.name: arthur.get_hp(),
        mordred.name: mordred.get_hp(),
        red_knight.name: red_knight.get_hp()
    }


print(battle(KNIGHTS))
