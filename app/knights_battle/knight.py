from typing import Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: Optional[dict],
        potion: Optional[dict]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def total_power(self) -> int:
        total = self.power
        if self.weapon:
            total += self.weapon.get("power", 0)
        if self.potion and "power" in self.potion.get("effect", {}):
            total += self.potion["effect"]["power"]
        return total

    def total_protection(self) -> int:
        total = 0
        for part in self.armour:
            total += part["protection"]
        total_potion = 0
        if self.potion and "protection" in self.potion.get("effect", {}):
            total_potion = self.potion["effect"]["protection"]
        return total + total_potion

    def total_hp(self) -> int:
        total = self.hp
        if self.potion and "hp" in self.potion.get("effect", {}):
            total += self.potion["effect"]["hp"]
        return total
