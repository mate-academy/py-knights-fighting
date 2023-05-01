from typing import Optional

from app.items import Weapon, Armour, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: dict,
        armour: list[dict],
        potion: Optional[dict] = None,
    ) -> None:
        self.name = name
        self._base_power = power
        self._base_hp = hp
        self._base_protection = 0
        self.protection = self._base_protection
        self.weapon: Weapon = Weapon(**weapon)
        if not armour:
            self.armour = []
        else:
            self.armour: list[Armour] = [Armour(**armour_item)
                                         for armour_item in armour]
        self.potion = None
        if potion is not None:
            self.potion = Potion(**potion)
        self.hp = self._base_hp
        self.power = self._base_power
        self.apply_stats()

    def apply_stats(self) -> None:
        self.hp = self._base_hp
        self.protection = self._base_protection
        self.power = self._base_power

        # apply armour
        for item in self.armour:
            self.protection += item.protection

        # apply weapon
        self.power += self.weapon.power

        # apply potion if exist

        if self.potion is not None:
            for attr in ["hp", "power", "protection"]:
                attr_value = getattr(self.potion.effect, attr)
                setattr(self, attr, getattr(self, attr) + attr_value)

    def battle(self, enemy: object) -> None:
        results = {enemy: max(enemy.hp - self.power + enemy.protection, 0)}
        self.hp = max(self.hp - enemy.power + self.protection, 0)

        results[self] = self.hp
        print(f"{self.name} Battle result: {results}")
        return results

    def __repr__(self) -> None:
        return self.name
