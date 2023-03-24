import random

from libraries import names_of_knights,perks,gear,weapons,potions


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


def knight_creation():
    knights_instances = {}
    for name in names_of_knights:
        current_knight = {name: {
            "name": name,
            "power": random.randint(10, 15),
            "hp": random.randint(80, 100),
            "armour": armour_pick(9),
            "weapon": {},
            "potion": {}}}

        knights_instances.update(current_knight)
    return knights_instances


def armour_pick(max_amount):
    knight_gear = []
    return knight_gear

def weapon_pick:
    pass

def potion_pick:
    pass

