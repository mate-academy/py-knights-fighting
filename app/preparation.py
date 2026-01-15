from __future__ import annotations


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config.get("name")
        self.power = config.get("power")
        self.hp = config.get("hp")
        self.armour = config.get("armour")
        self.weapon = config.get("weapon")
        self.potion = config.get("potion", None)
        self.protection = 0
        self.calculate_protection()
        self.apply_weapon()
        self.apply_potion()

    def calculate_protection(self) -> None:
        self.protection = sum(item.get("protection") for item in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.get("effect")
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def fight_vs(self, enemy: Knight) -> None:
        self.hp -= max(0, enemy.power - self.protection)
        enemy.hp -= max(0, self.power - enemy.protection)

    def get_hp(self) -> int:
        return max(0, self.hp)
