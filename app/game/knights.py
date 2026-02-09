from app.game.equipment.armors import Armor
from app.game.equipment.potions import Potion
from app.game.equipment.weapons import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armor: list[Armor] = None,
                 weapon: Weapon = None,
                 potion: Potion = None) -> None:

        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armor = armor or []
        self.weapon = weapon
        self.potion = potion

        self.protection = sum(a.protection for a in self.armor)
        self.power = (self.base_power
                      + (self.weapon.power if self.weapon else 0))
        self.hp = self.base_hp

        if self.potion and isinstance(self.potion.effect, dict):
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, attack_power: int) -> None:
        damage = max(0, attack_power - self.protection)
        self.hp = max(0, self.hp - damage)

    def is_defeated(self) -> bool:
        return self.hp <= 0
