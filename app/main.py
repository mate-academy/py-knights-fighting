from typing import Dict

from app.knights.knight import Knight


def battle(knights_data: Dict[str, dict]) -> Dict[str, int]:
    knights = {}
    for name, data in knights_data.items():

        knight = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"]
        )
        knights[name] = knight

    for knight in knights.values():
        knight.apply_effects()

    results = {}
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for knight1_name, knight2_name in battles:
        knight1 = knights[knight1_name]
        knight2 = knights[knight2_name]

        knight2_hp_loss = max(0,
                              knight2.power - knight1.calculate_protection()
                              )
        knight1.hp -= knight2_hp_loss

        knight1_hp_loss = max(0,
                              knight1.power - knight2.calculate_protection()
                              )
        knight2.hp -= knight1_hp_loss

        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0

        results[knight1.name] = knight1.hp
        results[knight2.name] = knight2.hp

    return results
