from typing import Optional

from app.inventory.armour import Armour
from app.inventory.potion import Potion
from app.inventory.weapon import Weapon


class Knight:
    knights = {}

    def __init__(
            self,
            alias: str,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: Optional[dict] = None
    ) -> None:
        self.alias = alias
        self.name = name
        self._power = power
        self.hp = hp
        self.armour = [Armour(**a) for a in armour]
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None
        self.protection = sum(a.get("protection", 0) for a in armour)

    @classmethod
    def load_knights(cls, knights_config: dict) -> None:
        cls.knights = {
            alias: Knight(alias=alias, **attributes)
            for alias, attributes in knights_config.items()
        }

    def effective_power(self) -> int:
        return self._power + self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            self._power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_potion()

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)
