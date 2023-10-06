import json

from Knight_class import creation_of_knight_instances
from action import all_battles, battle

with open("KNIGHTS.json", "r") as json_file:
    KNIGHTS = json.load(json_file)

knights = creation_of_knight_instances(KNIGHTS)

for knight in knights.values():
    knight.apply_armour()
    knight.apply_potion()
    knight.apply_weapon()

knights_pairs = {
    "lancelot": "mordred",
    "arthur": "red_knight"
}

all_battles(knights_pairs, knights)

print(battle(knights))
