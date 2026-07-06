from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def equip_armour(self) -> None:
        for item in self.armour:
            self.protection += item.protection

    def equip_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def battle_preparation(self) -> None:
        self.equip_armour()
        self.equip_weapon()
        self.apply_potion()

    def battle_with(self, other: "Knight") -> None:
        self.battle_preparation()
        other.battle_preparation()
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
