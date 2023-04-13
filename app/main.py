from app.methods import Armour
from app.methods import Knight

from app.data import KNIGHTS


# creating class objects using Knight and Armour classes
knights = []
for i, objects in KNIGHTS.items():
    name = objects["name"]
    power = objects["power"]
    hp = objects["hp"]
    armour = ([Armour(item["part"], item["protection"])
               for item in objects["armour"]])
    weapon = objects["weapon"]
    potion = objects["potion"]

    knight = Knight(name, power, hp, armour, weapon, potion)

    knight.apply_potion()
    knight.apply_weapon()

    knights.append(knight)


def battle(knights: list[Knight]) -> str:
    # 1 Lancelot vs Mordred:
    damage_to_0 = getattr(knights[2], "power") \
        - knights[0].calculate_total_protection()
    damage_to_2 = getattr(knights[0], "power") \
        - knights[2].calculate_total_protection()
    hp_0 = getattr(knights[0], "hp") - damage_to_0
    if hp_0 < 0:
        hp_0 = 0
    hp_2 = getattr(knights[2], "hp") - damage_to_2
    if hp_2 < 0:
        hp_2 = 0

    # 2 Arthur vs Red Knight:
    damage_to_1 = getattr(knights[3], "power") \
        - knights[1].calculate_total_protection()
    damage_to_3 = getattr(knights[1], "power") \
        - knights[3].calculate_total_protection()
    hp_1 = getattr(knights[1], "hp") - damage_to_1
    if hp_1 < 0:
        hp_1 = 0
    hp_3 = getattr(knights[3], "hp") - damage_to_3
    if hp_3 < 0:
        hp_3 = 0

    result = f"{knights[0].name} dealt {damage_to_2} damage to " \
             f"{knights[2].name}; and has hp after the battle: {hp_0}\n" \
             f"{knights[2].name} dealt {damage_to_0} damage to " \
             f"{knights[0].name}; and has hp after the battle: {hp_2}\n" \
             f"{knights[1].name} dealt {damage_to_3} damage to " \
             f"{knights[3].name}; and has hp after the battle: {hp_1}\n" \
             f"{knights[3].name} dealt {damage_to_1} damage to " \
             f"{knights[1].name}; and has hp after the battle: {hp_3}"

    print(result)
    return result


battle(knights)
