from app.apply_equipment import apply_armour, apply_potion, apply_weapon


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
    # lancelot = knightsConfig["lancelot"]
    #
    # # apply armour
    # lancelot["protection"] = 0
    # for a in lancelot["armour"]:
    #     lancelot["protection"] += a["protection"]
    #
    # # apply weapon
    # lancelot["power"] += lancelot["weapon"]["power"]
    #
    # # apply potion if exist
    # if lancelot["potion"] is not None:
    #     if "power" in lancelot["potion"]["effect"]:
    #         lancelot["power"] += lancelot["potion"]["effect"]["power"]
    #
    #     if "protection" in lancelot["potion"]["effect"]:
    #         lancelot["protection"] +=
    #         lancelot["potion"]["effect"]["protection"]
    #
    #     if "hp" in lancelot["potion"]["effect"]:
    #         lancelot["hp"] += lancelot["potion"]["effect"]["hp"]
    #
    # # arthur
    # arthur = knightsConfig["arthur"]
    #
    # # apply armour
    # arthur["protection"] = 0
    # for a in arthur["armour"]:
    #     arthur["protection"] += a["protection"]
    #
    # # apply weapon
    # arthur["power"] += arthur["weapon"]["power"]
    #
    # # apply potion if exist
    # if arthur["potion"] is not None:
    #     if "power" in arthur["potion"]["effect"]:
    #         arthur["power"] += arthur["potion"]["effect"]["power"]
    #
    #     if "protection" in arthur["potion"]["effect"]:
    #         arthur["protection"] +=
    #         arthur["potion"]["effect"]["protection"]
    #
    #     if "hp" in arthur["potion"]["effect"]:
    #         arthur["hp"] += arthur["potion"]["effect"]["hp"]
    #
    # # mordred
    # mordred = knightsConfig["mordred"]
    #
    # # apply armour
    # mordred["protection"] = 0
    # for a in mordred["armour"]:
    #     mordred["protection"] += a["protection"]
    #
    # # apply weapon
    # mordred["power"] += mordred["weapon"]["power"]
    #
    # # apply potion if exist
    # if mordred["potion"] is not None:
    #     if "power" in mordred["potion"]["effect"]:
    #         mordred["power"] += mordred["potion"]["effect"]["power"]
    #
    #     if "protection" in mordred["potion"]["effect"]:
    #         mordred["protection"] +=
    #         mordred["potion"]["effect"]["protection"]
    #
    #     if "hp" in mordred["potion"]["effect"]:
    #         mordred["hp"] += mordred["potion"]["effect"]["hp"]
    #
    # # red_knight
    # red_knight = knightsConfig["red_knight"]
    #
    # # apply armour
    # red_knight["protection"] = 0
    # for a in red_knight["armour"]:
    #     red_knight["protection"] += a["protection"]
    #
    # # apply weapon
    # red_knight["power"] += red_knight["weapon"]["power"]
    #
    # # apply potion if exist
    # if red_knight["potion"] is not None:
    #     if "power" in red_knight["potion"]["effect"]:
    #         red_knight["power"] += red_knight["potion"]["effect"]["power"]
    #
    #     if "protection" in red_knight["potion"]["effect"]:
    #         red_knight["protection"] +=
    #         red_knight["potion"]["effect"]["protection"]
    #
    #     if "hp" in red_knight["potion"]["effect"]:
    #         red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]
    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    # lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    # mordred["hp"] -= lancelot["power"] - mordred["protection"]
    #
    # # check if someone fell in battle
    # if lancelot["hp"] <= 0:
    #     lancelot["hp"] = 0
    #
    # if mordred["hp"] <= 0:
    #     mordred["hp"] = 0
    #
    # # 2 Arthur vs Red Knight:
    # arthur["hp"] -= red_knight["power"] - arthur["protection"]
    # red_knight["hp"] -= arthur["power"] - red_knight["protection"]
    #
    # # check if someone fell in battle
    # if arthur["hp"] <= 0:
    #     arthur["hp"] = 0
    #
    # if red_knight["hp"] <= 0:
    #     red_knight["hp"] = 0

    def apply_damage(attacker: dict, defender: dict) -> None:
        damage1 = defender["power"] - attacker["protection"]
        damage2 = attacker["power"] - defender["protection"]

        attacker["hp"] -= max(damage1, 0)
        defender["hp"] -= max(damage2, 0)
        if attacker["hp"] <= 0:
            attacker["hp"] = 0

        if defender["hp"] <= 0:
            defender["hp"] = 0
    apply_damage(lancelot, mordred)
    apply_damage(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
