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
        armour: Optional[list[ArmourPart]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.hp = 0
        self.power = 0
        self.protection = 0
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = sum(part.protection for part in self.armour)

        if self.weapon:
            self.power += self.weapon.power

        if self.potion:
            effect = self.potion.effect
            if isinstance(effect, dict):
                self.hp += effect.get("hp", 0)
                self.power += effect.get("power", 0)
                self.protection += effect.get("protection", 0)
            elif isinstance(effect, int):
                potion_name = self.potion.name.lower()
                if "hp" in potion_name or "heal" in potion_name:
                    self.hp += effect
                elif ("power" in potion_name
                      or "strength" in potion_name
                      or "berserk" in potion_name):
                    self.power += effect
                elif ("protect" in potion_name
                      or "shield" in potion_name
                      or "blessing" in potion_name):
                    self.protection += effect

    def receive_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)
