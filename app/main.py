from app.warrior.knight import Knight

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
            },
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
            },
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
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def battle(knights_config: dict[Knight]) -> None:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(
        knights_config["lancelot"]["name"],
        knights_config["lancelot"]["power"],
        knights_config["lancelot"]["hp"],
        knights_config["lancelot"]["armour"],
        knights_config["lancelot"]["weapon"],
        knights_config["lancelot"]["potion"],
    )

    # apply armour
    # apply weapon
    # apply potion if exist
    lancelot.battle_prepation()

    # arthur
    arthur = Knight(
        knights_config["arthur"]["name"],
        knights_config["arthur"]["power"],
        knights_config["arthur"]["hp"],
        knights_config["arthur"]["armour"],
        knights_config["arthur"]["weapon"],
        knights_config["arthur"]["potion"],
    )

    # apply armour
    # apply weapon
    # apply potion if exist
    arthur.battle_prepation()

    # mordred
    mordred = Knight(
        knights_config["mordred"]["name"],
        knights_config["mordred"]["power"],
        knights_config["mordred"]["hp"],
        knights_config["mordred"]["armour"],
        knights_config["mordred"]["weapon"],
        knights_config["mordred"]["potion"],
    )

    # apply armour
    # apply weapon
    # apply potion if exist
    mordred.battle_prepation()

    # red_knight
    red_knight = Knight(
        knights_config["red_knight"]["name"],
        knights_config["red_knight"]["power"],
        knights_config["red_knight"]["hp"],
        knights_config["red_knight"]["armour"],
        knights_config["red_knight"]["weapon"],
        knights_config["red_knight"]["potion"],
    )

    # apply armour
    # apply weapon
    # apply potion if exist
    red_knight.battle_prepation()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
