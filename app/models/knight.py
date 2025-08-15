from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int = 0,
        power: int = 0,
        armour: list = None,
        weapon: Weapon = None,
        potion: Potion = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = 0

        for arm in self.armour:
            self.protection += arm.protection

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.hp_effect
            self.power += self.potion.power_effect
            self.protection += self.potion.protection_effect

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def __repr__(self) -> str:
        return (
            f"Knight(name='{self.name}', hp={self.hp}, "
            f"power={self.power}, protection={self.protection})"
        )
