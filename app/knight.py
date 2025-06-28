from typing import List, Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[dict],
            weapon: dict,
            potion: Optional[dict] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

        self._apply_equipment()

    def _apply_equipment(self) -> None:
        self.protection = sum(
            armour_piece["protection"]
            for armour_piece in self.armour
        )
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> int:
        actual_damage = max(0, damage - self.protection)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self) -> bool:
        return self.hp > 0

    def get_stats(self) -> dict[str, int]:
        return {
            "name": self.name,
            "power": self.power,
            "hp": self.hp,
            "protection": self.protection
        }
