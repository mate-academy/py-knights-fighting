from knight_battle.item.armor import Armor
from knight_battle.item.weapon import Weapon
from knight_battle.item.potion import Potion
from typing import List, Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armor_configs: List[dict],
        weapon_config: dict,
        potion_config: Optional[dict],
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armor_configs = armor_configs
        self.weapon_config = weapon_config
        self.potion_config = potion_config

        self.armor: List[Armor] = []
        self.weapon: Optional[Weapon] = None
        self.potion: Optional[Potion] = None

        self.hp: int = 0
        self.power: int = 0
        self.protection: int = 0

        self._apply_items()
        self._calculate_stats()

    def _apply_items(self):
        for armor_config in self.armor_configs:
            self.armor.append(
                Armor(
                    name=armor_config["part"],
                    part=armor_config["part"],
                    protection=armor_config["protection"],
                )
            )

        self.weapon = Weapon(
            name=self.weapon_config["name"], power=self.weapon_config["power"]
        )

        if self.potion_config:
            self.potion = Potion(
                name=self.potion_config["name"], effect=self.potion_config["effect"]
            )

    def _calculate_stats(self):
        self.protection = sum(armor.protection for armor in self.armor)
        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp

        if self.potion:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, opponent: "Knight"):
        damage = max(0, self.power - opponent.protection)
        opponent.take_damage(damage)
