import random
from typing import List, Dict, Tuple, Any

from app.event_items.event_master import Event
from app.knight_items import libraries

knights_obj_list = []


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict[str, Any]],
                 weapon: Dict[str, Any],
                 potion: Dict[str, Any]):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion


def knight_dict_creation() -> Dict[str, Dict[str, Any]]:
    knights_full_equip = {}
    for name in libraries.names_of_knights:
        if name == "arthur":
            name = "Artur"

        knights_full_equip[name] = {
            "name": name.replace("_", " ").title(),
            "power": random.randint(50, 55),
            "hp": random.randint(200, 220),
            "armour": armour_pick(),
            "weapon": weapon_pick(),
            "potion": random.choice(libraries.potions)
        }

    return knights_full_equip


def knight_obj_creation(participants_dict: Dict[str, Dict[str, Any]]) -> None:
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


def armour_pick() -> List[Dict[str, Any]]:
    knight_gear = []
    for part in libraries.gear:
        perk = random.choice(libraries.perks)
        part_name = f"{part} of {perk[0]}" if perk is not None else part
        protection = perk[1] if perk is not None else 5
        gear = {"part": part_name, "protection": protection}
        knight_gear.append(gear)
    return knight_gear


def weapon_pick() -> Dict[str, Any]:
    perk = random.choice(libraries.perks)
    if perk is not None:
        weapon_name = f"{random.choice(libraries.weapons)} of {perk[0]}"
        power = perk[1] + 10
    else:
        weapon_name = random.choice(libraries.weapons)
        power = 10
    return {"name": weapon_name, "power": power}


def stats_calculation() -> None:
    for knight_dict in knights_obj_list:
        for characteristics in knight_dict.values():
            apply_armour(characteristics)
            apply_weapon(characteristics)
            apply_potion(characteristics)


def apply_armour(characteristics: Knight) -> None:
    for equipment in characteristics.armour:
        if equipment is not None:
            characteristics.hp += equipment["protection"]


def apply_weapon(characteristics: Knight) -> None:
    characteristics.power += characteristics.weapon["power"]


def apply_potion(characteristics: Knight) -> None:
    if characteristics.potion is not None:
        potion_effect = characteristics.potion["effect"]
        if "power" in potion_effect:
            characteristics.power += potion_effect["power"]
        if "hp" in potion_effect:
            characteristics.hp += potion_effect["hp"]
        if "protection" in potion_effect:
            characteristics.hp += potion_effect["protection"]


def knight_fight(participant_1: str,
                 participant_2: str) -> Tuple[Knight, Knight]:
    knight_1, knight_2 = None, None
    for knight_dict in knights_obj_list:
        for name, knight in knight_dict.items():
            if name.lower() == participant_1.lower():
                knight_1 = knight
            if name.lower() == participant_2.lower():
                knight_2 = knight
    knight_1.hp -= knight_2.power
    knight_2.hp -= knight_1.power
    Event.event_fight(knight_1, knight_2)
    return knight_1, knight_2


def tournament_result() -> Dict[str, int]:
    result = {}
    for knight_obj in knights_obj_list:
        for knight_name, characteristics in knight_obj.items():
            result[knight_name] = (
                characteristics.hp if characteristics.hp > 0 else 0
            )
    Event.event_result(result)
    return result


def for_pytest_func(test_dict: Dict[str, Dict]) -> Dict[str, int]:
    knight_obj_creation(test_dict)
    stats_calculation()

    knight_1, knight_2, knight_3, knight_4 = None, None, None, None

    for knight_dict in knights_obj_list:
        for name, knight in knight_dict.items():
            if name.lower() == "Lancelot".lower():
                knight_1 = knight
            if name.lower() == "Mordred".lower():
                knight_2 = knight
    for knight_dict in knights_obj_list:
        for name, knight in knight_dict.items():
            if name.lower() == "Artur".lower():
                knight_3 = knight
            if name.lower() == "Red Knight".lower():
                knight_4 = knight
    knight_1.hp -= knight_2.power
    knight_2.hp -= knight_1.power
    knight_3.hp -= knight_4.power
    knight_4.hp -= knight_3.power

    tournament_result = {}
    for knight_obj in knights_obj_list:
        for knight_name, characteristics in knight_obj.items():
            tournament_result[knight_name] = (
                characteristics.hp if characteristics.hp > 0 else 0
            )
    return tournament_result
