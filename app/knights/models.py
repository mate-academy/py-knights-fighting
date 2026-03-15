from typing import Dict, Optional
from app.knights.equipment import total_protection, weapon_power, apply_potion


class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            base_hp: int,
            armour: Optional[list] = None,
            weapon: Optional[dict] = None,
            potion: Optional[dict] = None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

    def prepare_stats(self) -> Dict[str, int]:
        stats = {
            "hp": self.base_hp,
            "power": self.base_power,
            "protection": total_protection(self.armour)
        }

        stats["power"] += weapon_power(self.weapon)

        stats = apply_potion(stats, self.potion)

        return stats
