from __future__ import annotations


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 protection: int = 0
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self) -> None:
        self.protection += sum(arm.get("protection", 0) for arm in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def prepare(self) -> None:
        self.apply_potion()
        self.apply_weapon()
        self.apply_armour()

    def fighting(self, enemy: Knight) -> None:
        self.prepare()
        enemy.prepare()
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        self.hp = max(self.hp, 0)
        enemy.hp = max(enemy.hp, 0)
