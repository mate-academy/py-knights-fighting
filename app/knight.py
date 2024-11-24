from app.items import Weapon, Armour, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: list[Armour],
        potion: Potion = None,
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.total_power = self.base_power + self.weapon.power
        self.protection = sum(a.protection for a in self.armour)

        if self.potion:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        effect = self.potion.effect
        self.total_power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.protection)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
