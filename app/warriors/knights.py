from app.equips.potion import Potion
from app.equips.armour import Armour
from app.equips.weapon import Weapon


class Knight:
    def __init__(
            self, name: str,
            base_hp: int,
            base_power: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None
    ) -> None:

        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power

        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.hp = base_hp
        self.power = base_power
        self.protection = 0

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_armour(self) -> None:
        if self.armour:
            for piece in self.armour:
                self.protection += piece.protection

    def apply_potion(self) -> None:
        if self.potion is None:
            return
        self.hp += self.potion.effect.get("hp", 0)
        self.power += self.potion.effect.get("power", 0)
        self.protection += self.potion.effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_potion()
        self.apply_weapon()
