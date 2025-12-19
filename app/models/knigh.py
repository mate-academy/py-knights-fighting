from dataclasses import dataclass
from app.models.equipment import Armour, Weapon, Potion


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    protection: int = 0

    def apply_armour(self, armour: list[Armour]) -> None:
        self.protection += sum(a.protection for a in armour)

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion | None) -> None:
        if potion is None:
            return

        for stat, value in potion.effect.items():
            setattr(self, stat, getattr(self, stat) + value)

    def receive_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)
