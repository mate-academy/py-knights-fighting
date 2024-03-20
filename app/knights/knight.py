from .equipment import Armour, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(**a) for a in armour]
        self.weapon = Weapon(**weapon) if weapon else None
        self.potion = Potion(**potion) if potion else None
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        if self.weapon:
            self.power += self.weapon.power
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        damage = max(damage - self.protection, 0)
        self.hp -= damage
        self.hp = max(self.hp, 0)
