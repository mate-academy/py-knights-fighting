import time
from random import randint
from typing import Any
from app.king_garden.knights import Knight
from app.armory.weapons import Weapon
from app.armory.armours import Armour


class Squire:
    def __init__(self, name: str) -> None:
        self.name = name
        self.weapons = None
        self.armours = None

    def take_arms_from(self, armaments: dict) -> None:
        print(f"{self} takes armaments from armory.")
        armours = {name: pack["armour"] for name, pack in armaments.items()}
        self.armours = {}
        for name, lst in armours.items():
            if lst:
                self.armours[name] = []
                for item in lst:
                    self.armours[name].append(
                        Armour(
                            name=name,
                            part=item["part"],
                            protection=item["protection"]
                        )
                    )

        self.weapons = {
            name: Weapon(name=weapon["weapon"]["name"],
                         power=weapon["weapon"]["power"])
            for name, weapon in armaments.items()
        }

    def enarm(self, name: str, knight: Knight) -> None:
        time.sleep(randint(1, 3))
        print(f"{self} enarms {knight} with a {self.weapons[name].name}.")
        time.sleep(randint(2, 5))
        knight.weapon = self.weapons[name].name
        knight.power += self.weapons[name].power

        if self.armours.get(name):
            print(f"{self} places armour on {knight.name.capitalize()}.")
            knight.protection += sum(armour.protection
                                     for armour in self.armours[name])
            time.sleep(randint(2, 5))

    def knights_enarm(self, knights: list[tuple[str | dict, Any]]) -> None:
        for name, knight in knights:
            self.enarm(name=name, knight=knight)
            time.sleep(randint(2, 5))
            print(f"{knight.name} is totally equipped.")

    def __str__(self) -> str:
        return f"Squire {self.name}"
