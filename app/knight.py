from typing import List, Optional
from app.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        armour: Optional[List[dict]] = None,
        weapon: Optional[dict] = None,
        potion: Optional[dict] = None,
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power

        self.armour = [Armour(**a) for a in armour] if armour else []
        self.weapon = Weapon(**weapon) if weapon else None
        self.potion = Potion(**potion) if potion else None

        self.hp = self.base_hp + self._get_potion_effect("hp")
        self.power = (self.base_power
                      + (self.weapon.power if self.weapon else 0))
        self.power += self._get_potion_effect("power")
        self.protection = sum(a.protection for a in self.armour)
        self.protection += self._get_potion_effect("protection")

    def _get_potion_effect(self, key: str) -> int:
        if not self.potion:
            return 0
        return self.potion.effect.get(key, 0)

    def take_damage(self, damage: int) -> None:
        actual_damage = max(damage - self.protection, 0)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
