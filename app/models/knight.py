from typing import Optional
from app.models.weapon import Weapon
from app.models.potion import Potion
from app.models.armour import ArmourPart


class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            base_hp: int,
            armour: Optional[ArmourPart] = None,
            weapon: Optional[Weapon] = None,
            potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = sum(part.protection for part in self.armour)

        if self.weapon:
            self.power += self.weapon.power
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def receive_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)
