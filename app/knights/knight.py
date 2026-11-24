from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None = None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.potion = potion
        if self.potion is not None:
            self.hp += self.potion.effect.get("hp", 0)
        self.armour = armour
        self.weapon = weapon

    @property
    def protection(self) -> int:
        total = sum(item.protection for item in self.armour)
        if self.potion is not None:
            total += self.potion.effect.get("protection", 0)
        return total

    @property
    def power(self) -> int:
        potion_bonus = 0
        if self.potion is not None:
            potion_bonus = self.potion.effect.get("power", 0)
        return self.base_power + self.weapon.power + potion_bonus
