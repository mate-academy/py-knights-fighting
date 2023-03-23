from __future__ import annotations


class Knight:

    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.power = info["power"]
        self.hp = info["hp"]
        self.protection = 0

        if info["armour"] != []:
            for part in info["armour"]:
                self.protection += part["protection"]

        if info["weapon"] is not None:
            self.power += info["weapon"]["power"]

        if info["potion"] is not None:
            self.power += info["potion"]["effect"].get("power", 0)
            self.hp += info["potion"]["effect"].get("hp", 0)
            self.protection += info["potion"]["effect"].get("protection", 0)

    def __str__(self) -> str:
        return f"{self.name} | HP: {self.hp} | Power: {self.power} " \
               f"| Protection: {self.protection}"

    @classmethod
    def battle(cls, first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        if first_knight.hp <= 0:
            first_knight.hp = 0
        if second_knight.hp <= 0:
            second_knight.hp = 0
