from app.knights import Knights, create_knight
from app.battle import fight

# KNIGHTS = {
#     "lancelot": {
#         "name": "Lancelot",
#         "power": 35,
#         "hp": 100,
#         "armour": [],
#         "weapon": {
#             "name": "Metal Sword",
#             "power": 50,
#         },
#         "potion": None,
#     },
#     "arthur": {
#         "name": "Arthur",
#         "power": 45,
#         "hp": 75,
#         "armour": [
#             {
#                 "part": "helmet",
#                 "protection": 15,
#             },
#             {
#                 "part": "breastplate",
#                 "protection": 20,
#             },
#             {
#                 "part": "boots",
#                 "protection": 10,
#             }
#         ],
#         "weapon": {
#             "name": "Two-handed Sword",
#             "power": 55,
#         },
#         "potion": None,
#     },
#     "mordred": {
#         "name": "Mordred",
#         "power": 30,
#         "hp": 90,
#         "armour": [
#             {
#                 "part": "breastplate",
#                 "protection": 15,
#             },
#             {
#                 "part": "boots",
#                 "protection": 10,
#             }
#         ],
#         "weapon": {
#             "name": "Poisoned Sword",
#             "power": 60,
#         },
#         "potion": {
#             "name": "Berserk",
#             "effect": {
#                 "power": +15,
#                 "hp": -5,
#                 "protection": +10,
#             }
#         }
#     },
#     "red_knight": {
#         "name": "Red Knight",
#         "power": 40,
#         "hp": 70,
#         "armour": [
#             {
#                 "part": "breastplate",
#                 "protection": 25,
#             }
#         ],
#         "weapon": {
#             "name": "Sword",
#             "power": 45
#         },
#         "potion": {
#             "name": "Blessing",
#             "effect": {
#                 "hp": +10,
#                 "power": +5,
#             }
#         }
#     }
# }


def battle(knights_info: dict) -> dict:
    battle_result = {}
    create_knight(knights_info)

    fight(Knights.knights_list[0], Knights.knights_list[2])
    fight(Knights.knights_list[1], Knights.knights_list[3])

    for knight in Knights.knights_list:
        battle_result.update({knight.name: knight.hp})

    return battle_result

# print(battle(KNIGHTS))
