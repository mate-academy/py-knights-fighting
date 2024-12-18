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


def put_on(personage: dict) -> dict:
    our_personage = personage.copy()
    our_personage["protection"] = 0
    for armour in personage["armour"]:
        our_personage["protection"] += armour["protection"]

    our_personage["power"] += our_personage["weapon"]["power"]

    if our_personage["potion"] is not None:
        our_p = our_personage["potion"]
        if "power" in our_p["effect"]:
            our_personage["power"] += our_p["effect"]["power"]

        if "protection" in our_p["effect"]:
            our_personage[
                "protection"
            ] += our_p["effect"]["protection"]

        if "hp" in our_p["effect"]:
            our_personage["hp"] += our_personage["potion"]["effect"]["hp"]

    return our_personage


def vs(pers1: dict, pers2: dict) -> dict:
    pers1["hp"] -= pers2["power"] - pers1["protection"]
    if pers1["hp"] <= 0:
        pers1["hp"] = 0

    return pers1


def battle(knights_config: dict) -> dict:

    # lancelot
    lancelot = put_on(knights_config["lancelot"])

    # arthur
    arthur = put_on(knights_config["arthur"])

    # mordred
    mordred = put_on(knights_config["mordred"])

    # red_knight
    red_knight = put_on(knights_config["red_knight"])

    # 1 Lancelot vs Mordred:
    lancelot = vs(lancelot, mordred)
    mordred = vs(mordred, lancelot)

    # 2 Arthur vs Red Knight:
    arthur = vs(arthur, red_knight)
    red_knight = vs(red_knight, arthur)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
