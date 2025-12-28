from __future__ import annotations


class Knights:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        if armour:
            sum_protection = 0
            for stats in armour:
                sum_protection += stats["protection"]
            self.armour = sum_protection
        else:
            self.armour = 0
        self.weapon = weapon
        self.potion = potion


def knights_list(knights: dict) -> list[Knights]:
    return [
        Knights(
            name=configs["name"],
            power=configs["power"],
            hp=configs["hp"],
            armour=configs["armour"],
            weapon=configs["weapon"],
            potion=configs["potion"]
        )
        for configs in knights.values()
    ]
