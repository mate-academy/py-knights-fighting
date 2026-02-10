from __future__ import annotations


class Knight:

    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config.get("name")
        self.basic_power = knight_config.get("power", 0)
        self.basic_hp = knight_config.get("hp", 0)
        self.basic_protection = knight_config.get("protection", 0)

        # weapons
        self.weapon = knight_config.get("weapon", {})
        self.armour = knight_config.get("armour", [])
        self.potion = knight_config.get("potion")

        # final stats
        self.power = self.calculate_power()
        self.protection = self.calculate_protection()
        self.hp = self.calculate_hp()

    def calculate_power(self) -> int:
        power = self.basic_power
        power += self.weapon.get("power", 0)

        if self.potion:
            effect = self.potion.get("effect", {})
            power += effect.get("power", 0)
        return power

    def calculate_protection(self) -> int:
        protection = self.basic_protection

        for armor in self.armour:
            protection += armor.get("protection", 0)

        if self.potion:
            effect = self.potion.get("effect", {})
            protection += effect.get("protection", 0)
        return protection

    def calculate_hp(self) -> int:
        hp = self.basic_hp

        if self.potion:
            effect = self.potion.get("effect", {})
            hp += effect.get("hp", 0)
        return hp

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)

    def fight(self, opponent: Knight) -> None:
        damage = max(0, opponent.power - self.protection)
        self.take_damage(damage)
