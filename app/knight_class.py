from __future__ import annotations
from typing import List


class Knights:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def fight(self, knight_2: Knights) -> None:
        self.hp -= knight_2.power - self.protection
        knight_2.hp -= self.power - knight_2.protection

        if self.hp <= 0:
            self.hp = 0
        if knight_2.hp <= 0:
            knight_2.hp = 0


def return_knights_and_hp(knights_obj: list) -> dict:
    return {
        knights_obj[0].name: knights_obj[0].hp,
        knights_obj[1].name: knights_obj[1].hp,
        knights_obj[2].name: knights_obj[2].hp,
        knights_obj[3].name: knights_obj[3].hp,
    }


def create_knights(knights: dict) -> List[Knights]:
    knights_list = []
    for key, value in knights.items():
        hp = value["hp"]
        power = value["power"]
        name = value["name"]
        protection = 0

        if value["weapon"]["power"]:
            power += value["weapon"]["power"]

        if value["armour"]:
            for item in value["armour"]:
                protection += item["protection"]

        if value["potion"] is not None:
            if "protection" in value["potion"]["effect"]:
                if value["armour"]:
                    protection += value["potion"]["effect"]["protection"]

            if "hp" in value["potion"]["effect"]:
                hp += value["potion"]["effect"]["hp"]

            if "power" in value["potion"]["effect"]:
                power += value["potion"]["effect"]["power"]

        knights_list.append(Knights(name, power, hp, protection))

    return knights_list
