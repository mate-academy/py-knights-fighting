from app.models.armour import Armour
from app.models.weapon import Weapon
from app.models.potion import Potion
from typing import Any, Dict


class Knight:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.name: str = config["name"]
        self.base_hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.armour: list[Armour] = [Armour(**a)
                                     for a in config.get("armour", [])]
        self.weapon: Weapon = Weapon(**config["weapon"])
        self.potion: Potion | None = (
            Potion(**config["potion"]) if config.get("potion") else None
        )

        self.apply_items()

    def apply_items(self) -> None:
        self.hp: int = self.base_hp
        self.power: int = self.base_power + self.weapon.power
        self.protection: int = sum(a.protection for a in self.armour)

        if self.potion:
            for stat, value in self.potion.effect.items():
                if hasattr(self, stat):
                    setattr(self, stat, max(
                        0, getattr(self, stat) + value))

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.protection)
        self.hp = max(0, self.hp - actual_damage)

    def __repr__(self) -> str:
        return (
            f"<Knight {self.name}: HP={self.hp}, "
            f"Power={self.power}, Protection={self.protection}>"
        )
