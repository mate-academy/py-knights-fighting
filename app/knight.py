from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        if knight.get("armour"):
            for part in knight["armour"]:
                self.protection += part["protection"]

        if knight.get("weapon"):
            self.power += knight["weapon"]["power"]

        if knight.get("potion"):
            for attr, value in knight["potion"]["effect"].items():
                setattr(self, attr, getattr(self, attr) + value)

    def __str__(self) -> str:
        return f"{self.name} | HP: {self.hp} | Power: {self.power} " \
               f"| Protection: {self.protection}"

    @classmethod
    def check_correctness_hp(cls, knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0

    @classmethod
    def battle(cls, first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection
