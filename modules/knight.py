from __future__ import annotations
from modules.arsenal import Armor, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0,
            armor: list[Armor] = None,
            weapon: Weapon = None,
            potion: None | Potion = None
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.armor = armor if armor is not None else []
        self.weapon = weapon
        self.potion = potion

    def equip_armor(self) -> None:
        if self.armor:
            for armor in self.armor:
                self.protection += armor.protection
                print(f"Knight {self.name} equipped {armor.part}")
        else:
            print(f"Knight {self.name} has no armor")

    def equip_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power
            print(f"Knight {self.name} equipped {self.weapon.name}")
        else:
            print(f"Knight {self.name} has no weapons")

    def unequip_armor(self) -> None:
        if self.armor:
            for armor in self.armor:
                self.protection -= armor.protection
                print(f"Knight {self.name} unequipped {armor.part}")
        else:
            print(f"Knight {self.name} has no armor")

    def unequip_weapon(self) -> None:
        if self.weapon:
            self.power -= self.weapon.power
            print(f"Knight {self.name} unequipped {self.weapon.name}")
        else:
            print(f"Knight {self.name} has no weapons")

    def drink_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            print(f"Knight {self.name} drank {self.potion.name} potion")
        else:
            print(f"Knight {self.name} has no potion")

    def fight_with(self, other: Knight) -> None:

        self.equip_armor()
        self.equip_weapon()
        self.drink_potion()

        other.equip_armor()
        other.equip_weapon()
        other.drink_potion()

        print(f"Knight {self.name} attacked Knight {other.name}.")
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
