from app.knights import Knight
from battle import Battle
from knight_list import KNIGHTS


all_knights = {key: Knight.from_config(val) for key, val in KNIGHTS.items()}

for knight in all_knights.values():
    knight.prepare()

battle1 = Battle(all_knights["lancelot"], all_knights["mordred"])
battle1.run()

battle2 = Battle(all_knights["arthur"], all_knights["red_knight"])
battle2.run()

final_result: dict[str, int] = {
    knight_obj.name: knight_obj.hp
    for knight_obj in all_knights.values()
}

print(final_result)
