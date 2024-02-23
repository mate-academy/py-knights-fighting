from app.knights.potion import Potion
from app.knights.armour import Armour
from app.knights.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_the_fight(self) -> None:
        for equipment in self.armour:
            self.protection += equipment.protection

        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if hasattr(self.potion, "effect") and \
                isinstance(self.potion.effect, dict):
            for name, effect in self.potion.effect.items():
                if hasattr(self, name):
                    setattr(self, name, getattr(self, name) + effect)

    def fight_and_apply_damage(self, other_knight: "Knight") -> None:
        self.hp -= other_knight.power - self.protection
        if self.hp <= 0:
            self.hp = 0
