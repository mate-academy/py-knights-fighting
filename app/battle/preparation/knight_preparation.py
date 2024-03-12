from typing import Optional

class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name: str = name
        self.power: int = power

class Potion:
    def __init__(self, name: str, hp_effect: int = 0, power_effect: int = 0) -> None:
        self.name: str = name
        self.hp_effect: int = hp_effect
        self.power_effect: int = power_effect

class Knight:
    def __init__(self, name: str, power: int, hp: int, weapon: Weapon, potion: Optional[Potion] = None) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.weapon: Weapon = weapon
        self.potion: Optional[Potion] = potion

    def apply_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.hp_effect
            self.power += self.potion.power_effect

    def battle(self) -> None:
        # Example battle logic here, assuming it modifies the hp of both self and opponent
        pass