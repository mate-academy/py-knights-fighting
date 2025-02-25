from typing import Dict, Any
from knight.config import KNIGHTS
from knight.knight import Knight
from battle.battle import calculate_battle


def create_knight(knight_data: Dict[str, Any]) -> Knight:
    return Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"],
        knight_data["armour"],
        knight_data["weapon"],
        knight_data["potion"],
    )


lancelot = create_knight(KNIGHTS["lancelot"])
mordred = create_knight(KNIGHTS["mordred"])
arthur = create_knight(KNIGHTS["arthur"])
red_knight = create_knight(KNIGHTS["red_knight"])


result_1 = calculate_battle(lancelot, mordred)
result_2 = calculate_battle(arthur, red_knight)


print("Battle 1 Result:", result_1)
print("Battle 2 Result:", result_2)
