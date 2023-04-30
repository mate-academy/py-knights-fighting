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
        self.armour = [
            Armour(**armour_item) for armour_item in armour
        ]
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

    def battle(self, enemy: "Enemy") -> None:
        results = {self: None, enemy: None}
        enemy_damage = max(enemy.hp - self.power + enemy.protection, 0)
        self_damage = max(self.hp - enemy.power + self.protection, 0)
        results[self] = self_damage
        results[enemy] = enemy_damage
        self.hp = max(self.hp - enemy_damage, 0)
        enemy.hp = max(enemy.hp - self_damage, 0)
        print(f"{self.name} Battle {enemy.name} result: {results}")
        return results

    def __repr__(self) -> None:
        return self.name
