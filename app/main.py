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
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]
    hero_list = [lancelot, arthur, mordred, red_knight]

    for hero in hero_list:
        hero["protection"] = 0
        for defense in hero["armour"]:
            hero["protection"] += defense["protection"]

        hero["power"] += hero["weapon"]["power"]

        if hero["potion"] is not None:
            if "power" in hero["potion"]["effect"]:
                hero["power"] += hero["potion"]["effect"]["power"]

            if "protection" in hero["potion"]["effect"]:
                hero["protection"] += hero["potion"]["effect"]["protection"]

            if "hp" in hero["potion"]["effect"]:
                hero["hp"] += hero["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:
    def clash(hero_list: list) -> None:
        for item in range(len(hero_list)):
            hero_1 = hero_list[item]
            hero_2 = hero_list[item + 2]
            hero_1["hp"] -= hero_2["power"] - hero_1["protection"]
            hero_2["hp"] -= hero_1["power"] - hero_2["protection"]
            if item == 1:
                break

    def helth_point(hero_list: list) -> None:
        for hero in hero_list:
            if hero["hp"] <= 0:
                hero["hp"] = 0

    clash(hero_list)
    helth_point(hero_list)
    return {hero["name"]: hero["hp"] for hero in hero_list}


print(battle(KNIGHTS))
