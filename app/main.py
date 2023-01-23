from __future__ import annotations
from app.knights import Knights


def ready_to_battle(knight_param: dict) -> Knights:
    knight = Knights(
        name=knight_param["name"],
        hp=knight_param["hp"],
        power=knight_param["power"]
    )
    knight.use_weapon(knight_param["weapon"])
    knight.use_armour(knight_param["armour"])
    knight.use_potion(knight_param["potion"])
    return knight


def battle(knight: dict) -> dict:
    lancelot = ready_to_battle(knight_param=knight["lancelot"])
    mordred = ready_to_battle(knight_param=knight["mordred"])
    artur = ready_to_battle(knight_param=knight["arthur"])
    red_knight = ready_to_battle(knight_param=knight["red_knight"])

    lancelot.fight(other=mordred)
    artur.fight(other=red_knight)

    return {
        lancelot.name: lancelot.hp,
        artur.name: artur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
