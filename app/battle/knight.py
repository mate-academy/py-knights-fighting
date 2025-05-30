from typing import Optional, List
from .item import Weapon, Armor, Potion


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armor: Optional[List[Armor]] = None,
                 weapon: Optional[Weapon] = None,
                 potion: Optional[Potion] = None) -> None:
        self.name = name
        self.base_power = power
        self.max_hp = hp
        self.hp = hp
        self.armor = armor if armor else []
        self.weapon = weapon
        self.potion = potion
        self.protection = sum(a.protection for a in self.armor)
        self.power = self.base_power + (self.weapon.power
                                        if self.weapon else 0)
        self._apply_potion()

    def _apply_potion(self) -> None:
        if self.potion and self.potion.effect:
            print(f"{self.name} вживає чарівне зілля '{self.potion.name}'.")
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
                self.max_hp += self.potion.effect["hp"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

    def take_damage(self, damage: int) -> None:
        damage_taken = max(0, damage - self.protection)
        self.hp -= damage_taken
        print(f"{self.name} був поранений в бою на "
              f"{damage_taken} ран. "
              f"Залишилось здоров'я: {max(0, self.hp)}")
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} сконав.")

    def attack(self, target: 'Knight') -> None:
        if self.weapon:
            print(f"{self.name} атакує {target.name} "
                  f"зброєю '{self.weapon.name}' "
                  f"(сила: {self.power}, "
                  f"захист цілі: {target.protection}).")
        else:
            print(f"{self.name} атакує {target.name} "
                  f"(сила: {self.power}, "
                  f"захист цілі: {target.protection}).")
        target.take_damage(self.power)

    def is_alive(self) -> None:
        return self.hp > 0
