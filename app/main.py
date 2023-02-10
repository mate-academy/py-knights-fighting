from __future__ import annotations
from app.knigts.all_knigts import KNIGHTS
from app.knigts.knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"]).prepare_to_battle()
    mordred = Knight(knights["mordred"]).prepare_to_battle()
    arthur = Knight(knights["arthur"]).prepare_to_battle()
    red_knight = Knight(knights["red_knight"]).prepare_to_battle()
    return {
        lancelot.name: lancelot.fight(mordred),
        arthur.name: arthur.fight(red_knight),
        mordred.name: mordred.fight(lancelot),
        red_knight.name: red_knight.fight(arthur)
    }


print(battle(KNIGHTS))
