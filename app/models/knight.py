from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour: list[Armour] = []
        self.weapon: Weapon | None = None
        self.potion: Potion | None = None

    def get_total_power(self) -> None:
        bonus = 0
        if self.potion:
            bonus += self.potion.effect.get("power", 0)

        return self.power + (self.weapon.power if self.weapon else 0) + bonus

    def get_total_protection(self) -> None:
        base = sum(a.protection for a in self.armour)

        bonus = 0
        if self.potion:
            bonus += self.potion.effect.get("protection", 0)

        return base + bonus

    def apply_potion(self) -> None:
        if not self.potion:
            return

        effect = self.potion.effect
        self.hp += effect.get("hp", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = max(0, enemy_power - self.get_total_protection())
        self.hp = max(0, self.hp - damage)
        self.potion = None
