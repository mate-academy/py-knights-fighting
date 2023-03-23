import random

print("Knight __main__")


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
    names_of_knights = ["Lancelot", "Artur", "Mordred", "Red Knight"]
    knights_instances = {}
    for name in names_of_knights:
        current_knight = {name: {
            "name": "Lancelot",
            "power": random.randint(10, 20),
            "hp": random.randint(100, 150),
            "armour": armour_pick(9),
            "weapon": {},
            "potion": {}}}

        knights_instances.update(current_knight)
    return knights_instances


def armour_pick(max_amount):
    gear = ["Helmet", "pauldrons", "breastplate", "vambrace",
            "gauntlets", "cuisses", "poleyns", "greaves", "sabatons"]
    knight_gear = [] # list[{"part": "s", "protection": 1}, {"part": "s", "protection": 1}]
    amount = random.randint(0, max_amount)
    if amount == 0:
        return []
    for pick in range(0, amount):

        return knight_gear


armour_pick(9)
