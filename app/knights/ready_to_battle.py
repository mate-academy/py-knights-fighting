from app.knights.basic_stats import knights_instances_dict
from app.knights.prepare_to_battle import KnightsPrepareToBattle


def knights_get_ready_to_battle(knights_dict: dict) -> dict:
    knights_instances = knights_instances_dict(knights_dict)
    final_knights_stats = {}

    for knight_name, knight_stats in knights_instances.items():
        final_knights_stats[knight_name] = KnightsPrepareToBattle(knight_stats)
        final_knights_stats[knight_name].apply_armour(knight_stats)
        final_knights_stats[knight_name].apply_weapon(knight_stats)
        final_knights_stats[knight_name].apply_potion(knight_stats)

    return final_knights_stats


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
#         "name": "Artur",
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
#
# knights = knights_get_ready_to_battle(KNIGHTS)
# lancelot = knights["lancelot"]
# print(lancelot.hp)
# for knight, knight_stat in knights.items():
#     print(knight, ":", knight_stat.hp)
