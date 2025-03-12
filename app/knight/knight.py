from app.item.armor import Armor
from app.item.weapon import Weapon
from app.item.potion import Potion
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

    def _apply_items(self) -> None:
        # Apply armor
        for armor_config in self.armor_configs:
            self.armor.append(
                Armor(
                    name=armor_config["part"],
                    part=armor_config["part"],
                    protection=armor_config["protection"],
                )
            )

        # Apply weapon
        self.weapon = Weapon(
            name=self.weapon_config["name"], power=self.weapon_config["power"]
        )

        # Apply potion
        if self.potion_config:
            self.potion = Potion(
                name=self.potion_config["name"],
                effect=self.potion_config["effect"]
            )

    def _calculate_stats(self) -> None:
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

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, opponent: "Knight") -> None:
        damage = max(0, self.power - opponent.protection)
        opponent.take_damage(damage)

    def __str__(self) -> None:
        return (f"Knight {self.name} (HP: {self.hp}, "
                f"Power: {self.power}, "
                f"Protection: {self.protection})")
