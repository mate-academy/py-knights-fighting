from typing import Any
from app.classes.class_knight import prepare_knight
from app.knights_pack.knights_dict import knights_dict


def battle(knights_config: dict) -> dict[Any, int]:
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= max(0, mordred.power - lancelot.protection)
    mordred.hp -= max(0, lancelot.power - mordred.protection)

    # check if someone fell in battle
    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)

    # 2 Arthur vs Red Knight:
    arthur.hp -= max(0, red_knight.power - arthur.protection)
    red_knight.hp -= max(0, arthur.power - red_knight.protection)

    # check if someone fell in battle
    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(knights_dict))
