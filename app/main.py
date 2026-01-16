from __future__ import annotations
from app.inst_pkg.init import initiation
from app.inst_pkg.dict_knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = initiation(knights_config["lancelot"])
    arthur = initiation(knights_config["arthur"])
    mordred = initiation(knights_config["mordred"])
    red_knight = initiation(knights_config["red_knight"])

    lancelot - mordred
    arthur - red_knight

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
