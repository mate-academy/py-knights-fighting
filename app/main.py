from app.weapon.weapon import Weapon
from app.armour.armour import Armour
from app.battle.battle import Battle
from app.knight.knight import Knight
from app.potion.potion import Potion
from app.potion.effect import Effect
from app.knights import KNIGHTS

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


def create_knight(knight_data: dict) -> Knight:
    weapon_data = knight_data["weapon"]
    weapon = Weapon(name=weapon_data["name"], power=weapon_data["power"])

    knight = Knight(name=knight_data["name"],
                    power=knight_data["power"],
                    hp=knight_data["hp"],
                    weapon=weapon)

    for armour_data in knight_data["armour"]:
        armour = Armour(part=armour_data["part"],
                        protection=armour_data["protection"])
        knight.equip_armour(armour)

    potion_data = knight_data.get("potion")

    if potion_data:
        effect_data = potion_data["effect"]
        power = effect_data.get("power", 0)
        hp = effect_data.get("hp", 0)
        protection = effect_data.get("protection", 0)

        effect = Effect(power=power, hp=hp, protection=protection)
        potion = Potion(potion_data["name"], effect)
        knight.equip_potion(potion)

    return knight


def battle(knight_data: dict) -> dict:
    lancelot = create_knight(knight_data["lancelot"])
    arthur = create_knight(knight_data["arthur"])
    mordred = create_knight(knight_data["mordred"])
    red_knight = create_knight(knight_data["red_knight"])

    first_battle = Battle(first_knight=mordred, second_knight=lancelot)
    first_battle_result = first_battle.combat()

    second_battle = Battle(first_knight=arthur, second_knight=red_knight)
    second_battle_result = second_battle.combat()

    battle_results = {
        "Arthur": second_battle_result.get("Arthur"),
        "Lancelot": first_battle_result.get("Lancelot"),
        "Mordred": first_battle_result.get("Mordred"),
        "Red Knight": second_battle_result.get("Red Knight")
    }

    return battle_results


if __name__ == "__main__":
    print(battle(KNIGHTS))
