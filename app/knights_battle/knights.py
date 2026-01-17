from app.knights_battle.weapons import Weapon
from app.knights_battle.potions import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = None
        self.calculate_protection()

    def calculate_protection(self) -> None:
        self.protection = sum(item["protection"] for item in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.effect
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} is dead")
