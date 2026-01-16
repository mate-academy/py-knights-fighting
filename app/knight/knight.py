from __future__ import annotations
from app.knight.armour import Armour
from app.knight.potion import Potion
from app.knight.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def use_armour(self) -> None:
        self.protection += sum(part.protection for part in self.armour)

    def use_weapon(self) -> None:
        self.power += self.weapon.power

    def use_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.effect
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def prepare_for_battle(self) -> None:
        self.use_armour()
        self.use_weapon()
        self.use_potion()

    def get_hit(self, damage: int) -> None:
        self.hp -= max(damage - self.protection, 0)
        if self.hp <= 0:
            self.hp = 0

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name}, power={self.power}, hp={self.hp}, "
            f"protection={self.protection}, weapon={repr(self.weapon)}, "
            f"armour=[{', '.join([repr(a) for a in self.armour])}], "
            f"potion={repr(self.potion) if self.potion else 'No potion'})"
        )
