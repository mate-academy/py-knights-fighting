from app.Knights.knights import Knight

# підрахунок шкоди

def calc_damage(power: int, protection: int) -> int:
    return max(0, power - protection)

# duel takes two knights and call "calc_damage"

def duel(couple: tuple["Knight", "Knight"]) -> dict[str, int]:
    duel_result = {}
    for idx in range(len(couple)):
        hp = couple[idx].hp
        hp -= calc_damage(couple[(idx + 1) % 2].power, couple[idx].protection)
        duel_result.update({couple[idx].name: max(0, hp)})
    return duel_result    

# battle itterates through the list of couples and call "duel" func for each cople

def battle(knights: list[tuple["Knight", "Knight"]]) -> dict[str, int]:
    battle_result = {}
    for couple in knights:
        battle_result.update(duel(couple))
    return battle_result







    first_knight = couple[0]
    second_knight = couple[1]

    hp1 = first_knight.hp
    hp2 = second_knight.hp

    hp1 -= calc_damage(second_knight.power, first_knight.protection)
    hp2 -= calc_damage(first_knight.power, second_knight.protection)



# def battle(
#         first_knight: "Knight",
#         second_knight: "Knight",
#         third_knight: "Knight" = None,
#         fourth_knight: "Knight" = None
# ) -> dict[str, int]:
    
    # if fourth_knight:

    #     hp1 = first_knight.hp
    #     hp2 = second_knight.hp
    #     hp3 = third_knight.hp
    #     hp4 = fourth_knight.hp

    #     hp1 -= calc_damage(second_knight.power, first_knight.protection)
    #     hp2 -= calc_damage(first_knight.power, second_knight.protection)
    #     hp3 -= calc_damage(fourth_knight.power, third_knight.protection)
    #     hp4 -= calc_damage(third_knight.power, fourth_knight.protection)
        
    #     hp1 = max(0, hp1)
    #     hp2 = max(0, hp2)
    #     hp3 = max(0, hp3)
    #     hp4 = max(0, hp4)
        
    #     return {
    #         first_knight.name: hp1,
    #         second_knight.name: hp2,
    #         third_knight.name: hp3,
    #         fourth_knight.name: hp4
    #     }

    # else:
    #     hp1 = first_knight.hp
    #     hp2 = second_knight.hp


    #     hp1 -= calc_damage(second_knight.power, first_knight.protection)
    #     hp2 -= calc_damage(first_knight.power, second_knight.protection)

    #     hp1 = max(0, hp1)
    #     hp2 = max(0, hp2)

        
    #     return {
    #         first_knight.name: hp1,
    #         second_knight.name: hp2,
    #     }

# друга версія битви
    
def battle(knights: list[list]):
    for idx, knight in enumerate(knights):
        hp = knight.hp
        hp -= calc_damage(knights[(idx + 1) % 2].power, knights[(idx + 1) % 2].protection)

    
    
    
    
    
    
    
    
    
    pass
    







'''
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


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

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
'''