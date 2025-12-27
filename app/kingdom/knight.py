from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def __str__(self) -> str:
        return (f"{self.name} ->\tpwr: {self.power}, "
                f"hp: {self.hp}, protection: {self.protection}")

    def apply_armour(self, armour: list) -> None:
        for armour_element in armour:
            self.protection += armour_element["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, effect: dict) -> None:
        for effect_name, effect_value in effect.items():
            self.__dict__[effect_name] += effect_value

    def fully_prepare_knight(self, knight_info: dict) -> None:
        self.apply_armour(armour=knight_info["armour"])
        self.apply_weapon(weapon=knight_info["weapon"])
        if knight_info["potion"]:
            self.apply_potion(effect=knight_info["potion"]["effect"])

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        self.hp = max(0, self.hp)
        other.hp = max(0, other.hp)
