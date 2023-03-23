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
    knights_instances_list = []
    for name in names_of_knights:
        knights_instances_list.append({"name": name})
    return knights_instances_list

