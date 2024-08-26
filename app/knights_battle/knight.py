from __future__ import annotations


class Knight:

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

    def adding_value_to_instance(self, element: dict) -> None:
        self.name = element["name"]
        self.power = element["power"] + element["weapon"]["power"]
        self.hp = element["hp"]
        self.protection = sum(a["protection"] for a in element["armour"])

    def adding_potion_to_instance(self, element: dict) -> None:
        if element["potion"] is not None:
            for value in element["potion"]["effect"]:
                if value == "power":
                    self.power += element["potion"]["effect"][value]
                if value == "hp":
                    self.hp += element["potion"]["effect"][value]
                if value == "protection":
                    self.protection += element["potion"]["effect"][value]

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection

    def check_if_someone_fell_in_battle(self) -> None:
        if self.hp <= 0:
            self.hp = 0
