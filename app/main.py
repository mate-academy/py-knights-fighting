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

    for i in knightsConfig:
        knight = knightsConfig[i]

        # apply armour
        knight['protection'] = 0
        if bool(knight['armour']) is not False:
            am = len(knight['armour'])
            for w in range(am):
                knight['protection'] += knight['armour'][w]['protection']

        # apply weapon
        knight['power'] += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]
            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += \
                    knight["potion"]["effect"]["protection"]
            if "hp" in knight["potion"]["effect"]:
                potion_effect_hp = knight["potion"]["effect"]["hp"]
                knight["hp"] += potion_effect_hp

    # 1 Lancelot vs Mordred:
    knightsConfig['lancelot']['hp'] -= knightsConfig['mordred']['power'] - \
        knightsConfig['lancelot']['protection']
    knightsConfig['mordred']['hp'] -= knightsConfig['lancelot']['power'] - \
        knightsConfig['mordred']['protection']

    # 2 Arthur vs Red Knight:
    knightsConfig['arthur']['hp'] -= knightsConfig['red_knight']['power'] - \
        knightsConfig['arthur']['protection']
    knightsConfig['red_knight']['hp'] -= knightsConfig['arthur']['power'] - \
        knightsConfig['red_knight']['protection']

    # check if someone fell in battle
    for w in knightsConfig:
        if knightsConfig[w]['hp'] < 0:
            knightsConfig[w]['hp'] = 0

    # Return battle results:
    return {
        knightsConfig["lancelot"]["name"]: knightsConfig["lancelot"]["hp"],
        knightsConfig["arthur"]["name"]: knightsConfig["arthur"]["hp"],
        knightsConfig["mordred"]["name"]: knightsConfig["mordred"]["hp"],
        knightsConfig["red_knight"]["name"]: knightsConfig["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
