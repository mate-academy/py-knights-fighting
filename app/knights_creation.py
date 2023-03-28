import random

from libraries import names_of_knights, perks, gear, weapons, potions


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
            "armour": armour_pick(),
            "weapon": weapon_pick(),
            "potion": random.choice(potions)}}

        knights_instances.update(current_knight)
    return knights_instances


def armour_pick():
    knight_gear = []

    for part in gear:
        perk = random.choice(perks)
        knight_gear.append({
            "part": f"{part} of {perk[0]}",
            "protection": perk[1]
        })
    return knight_gear


def weapon_pick():
    knight_weapon = {}
    perk = random.choice(perks)
    knight_weapon["name"] = f"{random.choice(weapons)} of {perk[0]}"
    knight_weapon["power"] = 10 + perk[1]
    return knight_weapon

