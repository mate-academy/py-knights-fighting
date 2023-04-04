import random

import libraries
from event_master import Event

# import random
# from app import libraries

knights_obj_list = []


def knight_dict_creation():
    knights_full_equip = {}
    for name in libraries.names_of_knights:
        if name == "arthur":
            name = "Artur"

        knights_full_equip[name] = {
            "name": name.replace("_", " ").title(),
            "power": random.randint(10, 15),
            "hp": random.randint(80, 100),
            "armour": armour_pick(),
            "weapon": weapon_pick(),
            "potion": random.choice(libraries.potions)
        }

    return knights_full_equip


def armour_pick():
    knight_gear = []
    for part in libraries.gear:
        perk = random.choice(libraries.perks)
        part_name = f"{part} of {perk[0]}" if perk is not None else part
        protection = perk[1] if perk is not None else 5
        gear = {"part": part_name, "protection": protection}
        knight_gear.append(gear)
    return knight_gear


def weapon_pick():
    perk = random.choice(libraries.perks)
    if perk is not None:
        weapon_name = f"{random.choice(libraries.weapons)} of {perk[0]}"
        power = perk[1] + 10
    else:
        weapon_name = random.choice(libraries.weapons)
        power = 10
    return {"name": weapon_name, "power": power}


def knight_fight(participant_1, participant_2):
    knight_1, knight_2 = None, None
    for knight_dict in knights_obj_list:
        for name, knight in knight_dict.items():
            if name.lower() == participant_1.lower():
                knight_1 = knight
            if name.lower() == participant_2.lower():
                knight_2 = knight
    knight_1.hp -= knight_2.power
    knight_2.hp -= knight_1.power
    Event.knights_fight(knight_1, knight_2)
    return knight_1, knight_2


def tournament_result():
    result = {}
    for knight_obj in knights_obj_list:
        for knight_name, characteristics in knight_obj.items():
            result[knight_name] = (
                characteristics.hp if characteristics.hp > 0 else 0
            )
    print(f"\n\n\n{result}")
    return result


def apply_armour(characteristics):
    for equipment in characteristics.armour:
        if equipment is not None:
            characteristics.hp += equipment["protection"]


def apply_weapon(characteristics):
    characteristics.power += characteristics.weapon["power"]


def apply_potion(characteristics):
    if characteristics.potion is not None:
        potion_effect = characteristics.potion["effect"]
        if "power" in potion_effect:
            characteristics.power += potion_effect["power"]
        if "hp" in potion_effect:
            characteristics.hp += potion_effect["hp"]
        if "protection" in potion_effect:
            characteristics.hp += potion_effect["protection"]


def stats_calculation():
    for knight_dict in knights_obj_list:
        for characteristics in knight_dict.values():
            apply_armour(characteristics)
            apply_weapon(characteristics)
            apply_potion(characteristics)



class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion


def knight_obj_creation(participants_dict):
    global knights_obj_list

    knights_obj_list = [
        {
            participant["name"]: Knight(
                name=participant["name"],
                power=participant["power"],
                hp=participant["hp"],
                armour=participant["armour"],
                weapon=participant["weapon"],
                potion=participant["potion"],
            )
        }
        for participant in participants_dict.values()
    ]
