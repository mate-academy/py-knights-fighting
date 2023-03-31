# import random
# import libraries

from app import libraries
from app import event_master
import random






knights_obj_list = []


def knight_dict_creation():
    knights_instances_dict = {}
    for name in libraries.names_of_knights:
        if name == "arthur":
            name = "Artur"
        current_knight = {name: {
            "name": name.replace("_"," ").title(),
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


def knight_fight(participant_1, participant_2):
    knight_1, knight_2 = None, None
    #print(knights_obj_list)
    for knight_dict in knights_obj_list:
        for name, characteristics in knight_dict.items():
            #print(name)
            #print(type(name))
            if name.lower() == participant_1.lower():
                knight_1 = characteristics
    for knight_dict in knights_obj_list:
        for name, characteristics in knight_dict.items():
            if name.lower() == participant_2.lower():
                knight_2 = characteristics
    # print(f"Knight_1 = {knight_1} / {knight_1.name} or {participant_1} |"
    #       f"| Knight_2 = {knight_2} / {knight_2.name} or {participant_2}")
    # print(f"{knight_1.name} stats before :HP = {knight_1.hp},ATT = {knight_1.power}")
    # print(f"{knight_2.name} stats before :HP = {knight_2.hp},ATT = {knight_2.power}")
    #print("knight_1.hp -= knight_2.power")
    #print(type(knight_1))
    #print(knight_1.name)
    #print(type(knight_2))
    #print(knight_2.name)
    knight_1.hp -= knight_2.power
    knight_2.hp -= knight_1.power
    # print(f"{knight_1.name} stats after :HP = {knight_1.hp} (puched for {knight_2.power})")
    # print(f"{knight_2.name} stats after :HP = {knight_2.hp} (puched for {knight_1.power})")
    knight_1, knight_2 = None, None


def tournament_result():
    result = {}
    for knight_obj in knights_obj_list:
        #print(knight_obj)
        for knight_name, characteristics in knight_obj.items():
            #print(knight_name, characteristics)
            result[knight_name] = characteristics.hp if characteristics.hp > 0 else 0
    print(knights_obj_list)
    print(result)

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
                # print(f"Stat calculation here. {characteristics.name} HP:{characteristics.hp}, "
                #       f"ATT: {characteristics.power}")
                for equipment in characteristics.armour:
                    if equipment is not None:
                        # print(equipment)
                        # print(f" hp {characteristics.hp} += hp {equipment['protection']}")
                        characteristics.hp += equipment["protection"]
                        #print(f" = {characteristics.hp}")
                #print(f"ATK {characteristics.power} += weapon ATK"
                 #     f" {characteristics.weapon['power']}")
                characteristics.power += characteristics.weapon["power"]
                #print(f" = {characteristics.power}")

                if characteristics.potion is not None:
                    if "power" in characteristics.potion["effect"]:
                       # print(f"potion | ATK {characteristics.power} +="
                             # f" ATK {characteristics.potion['effect']['power']}")
                        characteristics.power += characteristics.potion["effect"]["power"]
                       # print(f"ATK {characteristics.power}")
                    if "hp" in characteristics.potion["effect"]:
                       # print(f"potion | HP {characteristics.hp} +="
                            #  f" ATK {characteristics.potion['effect']['hp']}")
                        characteristics.hp += characteristics.potion["effect"]["hp"]
                       # print(f"HP {characteristics.power}")
                    if "protection" in characteristics.potion["effect"]:
                        #print(f"potion | PROT {characteristics.hp} +="
                              #f"  {characteristics.potion['effect']['hp']}")
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


def test_names():
   # print("_________________________________________________")
    #print(f"libraries.names_of_knights: {libraries.names_of_knights}")
    testo = []

    for i in knights_obj_list:
        for k, v in i.items():
            testo.append(k)

   # print(f"knights_obj_list name of dicts: {testo}")
