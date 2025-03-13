from dataclasses import dataclass
from typing import List, Optional

from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Armour]
    weapon: Weapon
    potion: Optional[Potion]

    def apply_armour(self) -> int:
        """Применяет броню и возвращает общую защиту."""
        return sum(part.protection for part in self.armour)

    def apply_weapon(self) -> int:
        """Применяет оружие и возвращает общую силу."""
        return self.power + self.weapon.power

    def apply_potion(self) -> dict:
        """Применяет зелье и возвращает изменения характеристик."""
        if self.potion:
            return self.potion.effect
        return {"hp": 0, "power": 0, "protection": 0}

    def calculate_stats(self) -> dict:
        """Рассчитывает итоговые характеристики рыцаря."""
        protection = self.apply_armour()
        power = self.apply_weapon()
        potion_effect = self.apply_potion()

        return {
            "hp": self.hp + potion_effect.get("hp", 0),
            "power": power + potion_effect.get("power", 0),
            "protection": protection + potion_effect.get("protection", 0),
        }
