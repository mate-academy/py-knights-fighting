from typing import Optional, List, Dict


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
        base_hp: int,
        base_power: int,
        armour: Optional[List[Armour]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.hp = base_hp
        self.power = base_power
        self.protection = 0

    def prepare_stats(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        # armour
        for tough in self.armour:
            self.protection += tough.protection

        # weapon
        if self.weapon:
            self.power += self.weapon.power

        # potion
        if self.potion:
            effect = self.potion.effect
            self.hp += int(effect.get("hp", 0))
            self.power += int(effect.get("power", 0))
            self.protection += int(effect.get("protection", 0))

        self.protection = max(0, int(self.protection))

    def take_damage(self, amount: int) -> None:
        if amount <= 0:
            return
        self.hp = max(0, self.hp - int(amount))
