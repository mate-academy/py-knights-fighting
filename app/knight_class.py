from __future__ import annotations


class Knights:

    def __init__(self, name: str, power: int, hp: int, protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def fight(self, knight_2: Knights):
        self.hp -= knight_2.power - self.protection
        knight_2.hp -= self.power - knight_2.protection

        if self.hp <= 0:
            self.hp = 0
        if knight_2.hp <= 0:
            knight_2.hp = 0


def return_result(knights_obj: list):
    return {
        knights_obj[0].name: knights_obj[0].hp,
        knights_obj[1].name: knights_obj[1].hp,
        knights_obj[2].name: knights_obj[2].hp,
        knights_obj[3].name: knights_obj[3].hp,
    }


def create_knights_obj(knights: dict):
    knights_obj = []
    for key, value in knights.items():
        knight = Knights(
            hp=value["hp"],
            power=value["power"],
            protection=value["protection"],
            name=key.capitalize()
        )
        knights_obj.append(knight)
    return knights_obj
