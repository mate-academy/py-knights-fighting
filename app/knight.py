from typing import List, Dict, Optional, Any


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, Any]],
        weapon: Dict[str, Any],
        potion: Optional[Dict[str, Any]],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(**armour_part) for armour_part in armour]
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None

    @property
    def protection(self) -> int:
        return sum(armour_part.protection for armour_part in self.armour)

    def apply_effects(self) -> None:
        self.power += self.weapon.power
        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)
            for armour_part in self.armour:
                armour_part.protection += (
                    self.potion.effect.get("protection", 0)
                )
