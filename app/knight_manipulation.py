import random

import libraries, event_master

knights_obj_list = []


def knight_dict_creation():
    knights_instances_dict = {}
    for name in libraries.names_of_knights:
        current_knight = {name: {
            "name": name.capitalize() if "_" not in name
            else name.replace("_", " ").title(),
            "power": random.randint(10, 15),
            "hp": random.randint(80, 100),
            "armour": armour_pick(),
            "weapon": weapon_pick(),
            "potion": random.choice(libraries.potions)}}

        knights_instances_dict.update(current_knight)
    return knights_instances_dict


def armour_pick():
    knight_gear = []

    for part in libraries.gear:
        perk = random.choice(libraries.perks)
        if perk is not None:
            knight_gear.append({
                "part": f"{part} of {perk[0]}",
                "protection": perk[1]
            })
        else:
            knight_gear.append({
                "part": f"{part}",
                "protection": 5
            })

    return knight_gear


def weapon_pick():
    knight_weapon = {}
    perk = random.choice(libraries.perks)
    if perk is not None:
        knight_weapon["name"] = f"{random.choice(libraries.weapons)} of {perk[0]}"
        knight_weapon["power"] = 10 + perk[1]
    else:
        knight_weapon["name"] = f"{random.choice(libraries.weapons)}"
        knight_weapon["power"] = 10
    return knight_weapon


def knight_fight(participant_1,participant_2):
    knights = []
    for knight_obj in knights_obj_list:
        if knight_obj.get(participant_1) is not None:
            knights.append(knight_obj.get(participant_1))
        if knight_obj.get(participant_2) is not None:
            knights.append(knight_obj.get(participant_2))
    knights[0].hp -= knights[1].power
    knights[1].hp -= knights[0].power

def tournament_result():
    result = {}
    for knight_obj in knights_obj_list:
        for knight_name, characteristics in knight_obj.items():
            result[knight_name] = characteristics.hp if characteristics.hp > 0 else 0

    return result



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

    def stats_calculation():
        for knight_dict in knights_obj_list:
            for characteristics in knight_dict.values():

                for equipment in characteristics.armour:
                    if equipment is not None:
                        characteristics.hp += equipment["protection"]
                characteristics.power += characteristics.weapon["power"]
                if characteristics.potion is not None:
                    characteristics.potion["effect"]["power"]
                    characteristics.power += characteristics.potion["effect"]["power"]
                    characteristics.hp += characteristics.potion["effect"]["hp"]
                    characteristics.hp += characteristics.potion["effect"]["protection"]

    def knight_obj_creation(participants_dict):
        global knights_obj_list

        for participant in participants_dict.values():
            prepared_knight = Knight(name=participant["name"],
                                     power=participant["power"],
                                     hp=participant["hp"],
                                     armour=participant["armour"],
                                     weapon=participant["weapon"],
                                     potion=participant["potion"])

            knights_obj_list.append(
                {participant["name"]: prepared_knight})
        return knights_obj_list
