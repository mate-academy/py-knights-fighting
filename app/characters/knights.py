from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        weapon: Weapon,
        potion: Potion | None = None,
        armour: dict[str, Armour] | None = None,
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power

        self.weapon = weapon
        self.potion = potion
        self.armour: dict[str, Armour] = armour or {}

        self.hp = 0
        self.power = 0
        self.protection = 0

        self.recalc_stats()

    def _potion_bonus(self, stat: str) -> int:
        if self.potion is None:
            return 0
        return self.potion.effect.get(stat, 0)

    def _armour_bonus(self) -> int:
        return sum(a.protection for a in self.armour.values())

    def recalc_stats(self) -> None:
        self.hp = self.base_hp + self._potion_bonus("hp")
        self.power = (
            self.base_power
            + self.weapon.power
            + self._potion_bonus("power")
        )
        self.protection = (
            self._armour_bonus()
            + self._potion_bonus("protection")
        )
