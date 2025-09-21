from __future__ import annotations
from app.config import KNIGHTS


class Person:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


def creator(knights: dict, name: str) -> Person | None:
    person = knights.get(name)
    person["protection"] = 0
    if person.get("armour"):
        for ar in person["armour"]:
            person["protection"] += ar["protection"]
    person["power"] += person["weapon"]["power"]
    if person["potion"] is not None:
        if "power" in person["potion"]["effect"]:
            person["power"] += person["potion"]["effect"]["power"]

        if "protection" in person["potion"]["effect"]:
            person["protection"] += person["potion"]["effect"]["protection"]

        if "hp" in person["potion"]["effect"]:
            person["hp"] += person["potion"]["effect"]["hp"]
    if person is not None:
        return Person(name=person["name"],
                      power=person["power"],
                      hp=person["hp"],
                      protection=person["protection"])


arthur = creator(KNIGHTS, "arthur")
lancelot = creator(KNIGHTS, "lancelot")
red_knight = creator(KNIGHTS, "red_knight")
mordred = creator(KNIGHTS, "mordred")

print(arthur.hp)
print(mordred.hp)
print(red_knight.hp, red_knight.protection, red_knight.power)
