from app.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        base_power: int,
        base_protection: int,
        weapon: Weapon | None = None,
        armour: list[Armour] | None = None,
        potion: Potion | None = None
    ) -> None:
        self.name = name
        self.hp = hp
        self.base_power = base_power
        self.base_protection = base_protection
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion
        self.power = base_power
        self.protection = base_protection

    def apply_equipment(self) -> None:
        if self.armour:
            self.protection += sum(a.protection for a in self.armour)
        if self.weapon:
            self.power += self.weapon.power
        if self.potion:
            effects = self.potion.effect
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)
