from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def calculate_protection(armor: list) -> int:
        # calculates a protection of knight based on its armour
        protection = 0
        if not armor:
            return protection
        for piece_of_armor in armor:
            protection += piece_of_armor["protection"]
        return protection

    def calculate_potion(self, potion: None | dict) -> None:
        # changes knights hp, power and protection
        # based on potion in knights pocket
        if potion is None:
            return None
        for stat, value in potion["effect"].items():
            if stat == "power":
                self.power += value
            elif stat == "hp":
                self.hp += value
            elif stat == "protection":
                self.protection += value
        return None

    def fight(self, other: Knight) -> None:
        # plays a fight between two knights
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0

    @classmethod
    def create_from_dict(cls, knight_dict: dict) -> Knight:
        # allows to create object of Knight class
        # using dict with data as an input
        knight = cls(
            name=knight_dict["name"],
            power=knight_dict["power"] + knight_dict["weapon"]["power"],
            hp=knight_dict["hp"],
        )
        knight.protection = (
            knight.calculate_protection(knight_dict.get("armour", []))
        )
        knight.calculate_potion(knight_dict["potion"])

        return knight
