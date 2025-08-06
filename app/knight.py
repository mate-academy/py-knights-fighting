from typing import List, Optional


class ArmourPart:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[ArmourPart]],
        weapon: Weapon,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        self.hp = hp
        self.power = power
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(part.protection for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return
        effect = self.potion.effect
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

        self.hp = max(self.hp, 0)
        self.power = max(self.power, 0)
        self.protection = max(self.protection, 0)

    def fight(self, opponent: "Knight") -> None:
        damage_to_self = max(opponent.power - self.protection, 0)
        damage_to_opponent = max(self.power - opponent.protection, 0)

        self.hp = max(self.hp - damage_to_self, 0)
        opponent.hp = max(opponent.hp - damage_to_opponent, 0)
