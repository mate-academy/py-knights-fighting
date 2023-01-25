from app.knights_stats import TheKnight
from app.scores import Scores
from app.knight_dict import knights


class KnightConfig:

    @staticmethod
    def battle() -> dict:
        list_of_knights = TheKnight.stats(knights)
        knight1 = list_of_knights[0]
        knight2 = list_of_knights[1]
        print(f"The battle between {knight1['name']} and {knight2['name']} started!")
        Scores.battle_scores(knight1, knight2)
        knight3 = list_of_knights[2]
        knight4 = list_of_knights[3]
        print(f"The battle between {knight3['name']} and {knight4['name']} started!")
        Scores.battle_scores(knight3, knight4)
        results = Scores.battle_scores(knight1, knight2).update(Scores.battle_scores(knight3, knight4))
        return results

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

    # lancelot
    lancelot = knightsConfig["lancelot"]

    # apply armour
    lancelot["protection"] = 0
    for a in lancelot["armour"]:
        lancelot["protection"] += a["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] += lancelot["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    # arthur
    arthur = knightsConfig["arthur"]

    # apply armour
    arthur["protection"] = 0
    for a in arthur["armour"]:
        arthur["protection"] += a["protection"]

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    if arthur["potion"] is not None:
        if "power" in arthur["potion"]["effect"]:
            arthur["power"] += arthur["potion"]["effect"]["power"]

        if "protection" in arthur["potion"]["effect"]:
            arthur["protection"] += arthur["potion"]["effect"]["protection"]

        if "hp" in arthur["potion"]["effect"]:
            arthur["hp"] += arthur["potion"]["effect"]["hp"]

    # mordred
    mordred = knightsConfig["mordred"]

    # apply armour
    mordred["protection"] = 0
    for a in mordred["armour"]:
        mordred["protection"] += a["protection"]

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    if mordred["potion"] is not None:
        if "power" in mordred["potion"]["effect"]:
            mordred["power"] += mordred["potion"]["effect"]["power"]

        if "protection" in mordred["potion"]["effect"]:
            mordred["protection"] += mordred["potion"]["effect"]["protection"]

        if "hp" in mordred["potion"]["effect"]:
            mordred["hp"] += mordred["potion"]["effect"]["hp"]

    # red_knight
    red_knight = knightsConfig["red_knight"]

    # apply armour
    red_knight["protection"] = 0
    for a in red_knight["armour"]:
        red_knight["protection"] += a["protection"]

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] += red_knight["potion"]["effect"]["power"]

        if "protection" in red_knight["potion"]["effect"]:
            red_knight["protection"] += red_knight["potion"]["effect"]["protection"]

        if "hp" in red_knight["potion"]["effect"]:
            red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
