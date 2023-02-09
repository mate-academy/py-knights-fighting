from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = None
        self.potion = None

    def fight_enemy(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection

    def take_and_drink_potion(self, name: str, potions: dict | None) -> None:
        self.potion = potions.get(name).get("potion")
        if self.potion is not None:
            print(f"{self.name.capitalize()} drinks {self.potion['name']}.")

            for parameter, value in self.potion["effect"].items():
                if parameter != "name":
                    self.__dict__[parameter] += value

            print(f"{self.name} gains {self.potion['effect']}.")

    def __str__(self) -> str:
        return f"mighty knight {self.name.capitalize()}"

    def __repr__(self) -> str:
        return f"{self.name.capitalize()}: {self}"
