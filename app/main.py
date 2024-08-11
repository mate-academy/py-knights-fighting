from __future__ import annotations

from app.knights_config import Knight


def get_knight(knight_data: dict) -> Knight:
    return Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        weapon=knight_data["weapon"],
        armour=knight_data["armour"],
        potion=knight_data["potion"]
    )


def fight(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0


def battle(knights_config: dict) -> dict:
    lancelot = get_knight(knights_config["lancelot"])
    arthur = get_knight(knights_config["arthur"])
    mordred = get_knight(knights_config["mordred"])
    red_knight = get_knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
