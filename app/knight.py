from __future__ import annotations


class Knight:

    def __init__(
            self,
            knight: dict
    ) -> None:
        self.name: str = knight.get("name")
        self.power: int = knight.get("power")
        self.hp: int = knight.get("hp")
        self.armour: list[dict] = knight.get("armour")
        self.weapon: dict = knight.get("weapon")
        self.potion = knight.get("potion")
        self.protection = 0

    def apply_equipment(self) -> None:
        self.protection = sum(
            armour.get("protection")
            for armour in self.armour
        )
        self.power += self.weapon.get("power")
        if self.potion:
            for key in self.potion["effect"]:
                setattr(self, key, getattr(self, key)
                        + self.potion["effect"][key])

    def duel(self, other: Knight) -> dict:
        self.apply_equipment()
        other.apply_equipment()
        self.hp = Knight.health_checker(
            self.hp - (other.power - self.protection)
        )
        other.hp = Knight.health_checker(
            other.hp - (self.power - other.protection)
        )
        return {
            self.name: self.hp,
            other.name: other.hp
        }

    @staticmethod
    def health_checker(hp: int) -> int:
        if hp >= 0:
            return hp
        else:
            return 0
