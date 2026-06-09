from app.Objects.weapon import Weapon
from app.Objects.potion import Potion

class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: Weapon,
            potion: Potion,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.protection = protection
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:

        for a in self.armour:
            self.protection += a.protection


    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self, potion) -> None:
        if potion is None:
            return

        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)
        self.hp += potion.effect.get("hp", 0)

    def get_damage(self, other: Knight) -> None:
        damage = max(other.power - self.protection, 0)
        self.hp -= damage
