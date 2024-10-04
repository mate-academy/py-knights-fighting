from __future__ import annotations

from app.knights import Knight


def pre_battle(knight: dict) -> Knight:

    fighter = Knight(knight)
    fighter.apply_armor()
    fighter.apply_weapon()

    if fighter.potion is not None:
        fighter.apply_potion()

    return fighter


def battle(knights_config: dict) -> dict:
    lancelot = pre_battle(knights_config["lancelot"])
    arthur = pre_battle(knights_config["arthur"])
    mordred = pre_battle(knights_config["mordred"])
    red_knight = pre_battle(knights_config["red_knight"])

    lancelot.damage(mordred)
    arthur.damage(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
