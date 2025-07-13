from typing import List, Optional, Dict


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        base_hp: int,
        base_power: int,
        weapon: Weapon,
        armour: Optional[List[Armour]] = None,
        potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion

        # These are final stats
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> int:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> int:
        self.power += self.weapon.power

    def apply_potion(self) -> int:
        if not self.potion:
            return
        for key, value in self.potion.effect.items():
            if key == "hp":
                self.hp += value
            elif key == "power":
                self.power += value
            elif key == "protection":
                self.protection += value
