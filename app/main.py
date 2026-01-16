from __future__ import annotations
from app.input_data import KNIGHTS
from app.knight import Knight


def battle_prepare(knight: dict) -> Knight:
    prepared_knight = Knight(knight)

    # apply armour
    prepared_knight.apply_armor()

    # apply weapon
    prepared_knight.apply_weapon()

    # apply potion if exist
    if prepared_knight.potion is not None:
        prepared_knight.apply_potion()

    return prepared_knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = battle_prepare(knights_config["lancelot"])

    # arthur
    arthur = battle_prepare(knights_config["arthur"])

    # mordred
    mordred = battle_prepare(knights_config["mordred"])

    # red_knight
    red_knight = battle_prepare(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle_action(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle_action(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
