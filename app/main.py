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


def knight_charm(knight_params: dict) -> dict:
    knights = dict()

    for name, params in knight_params.items():
        knights[name] = {"name": params["name"]}
        knights[name]["hp"] = (
            params["hp"]
            + (params["potion"] or {}).get("effect", {}).get("hp", 0))
        knights[name]["power"] = (
            params["power"] + params["weapon"]["power"]
            + (params["potion"] or {}).get("effect", {}).get("power", 0))
        knights[name]["protection"] = (
            sum([dic.get("protection", 0) for dic in params["armour"]] + [0])
            + (params["potion"] or {}).get("effect", {}).get("protection", 0))
    return knights


def battle_harm(knight: dict, harm: int) -> None:
    knight["hp"] -= harm - knight["protection"]
    knight["hp"] = max(knight["hp"], 0)


def battle(knight_params: dict) -> dict:
    # PRE-BATTLE CALCULATIONS:
    knights = knight_charm(knight_params)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    battle_harm(knights["lancelot"], knights["mordred"]["power"])
    battle_harm(knights["mordred"], knights["lancelot"]["power"])

    # 2 Arthur vs Red Knight:
    battle_harm(knights["arthur"], knights["red_knight"]["power"])
    battle_harm(knights["red_knight"], knights["arthur"]["power"])

    # # Return battle results:
    return {knights[name]["name"]: knights[name]["hp"] for name in knights}


print(battle(KNIGHTS))
