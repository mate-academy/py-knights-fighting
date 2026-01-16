from __future__ import annotations


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config.get("name")
        self.power = config.get("power")
        self.hp = config.get("hp")
        self.armor = config.get("armour")
        self.weapon = config.get("weapon")
        self.potion = config.get("potion")
        self.protection = 0
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        self.protection = sum(
            element.get("protection")
            for element in self.armor
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        if not self.potion:
            return
        effect = self.potion.get("effect")
        self.power += effect.get("power", 0)
        self.hp += effect.get("hp", 0)
        self.protection += effect.get("protection", 0)

    def battle(self, other: Knight) -> None:
        pass
