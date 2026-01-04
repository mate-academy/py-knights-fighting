from __future__ import annotations

from app.knight.weapon import Weapon
from app.knight.armor import Armor
from app.knight.potion import Potion


class Knight:

    def __init__(self, knight_config: dict) -> None:
        self.base_power = knight_config["power"]
        self.base_hp = knight_config["hp"]
        self.name = knight_config["name"]
        # add armour
        self.protection = 0
        self.power = self.base_power
        self.hp = self.base_hp
        self.armor = []
        for armor in knight_config["armour"]:
            self.armor.append(Armor(name=armor["part"],
                                    protection=armor["protection"]))

        # add weapon
        self.weapon = Weapon(name=knight_config["weapon"]["name"],
                             power=knight_config["weapon"]["power"])

        # add potion if exist
        potion_name = "None"
        potion_protection = 0
        potion_hp = 0
        potion_power = 0

        if knight_config["potion"] is not None:

            if "power" in knight_config["potion"]["effect"]:
                potion_power = (
                    knight_config)["potion"]["effect"]["power"]

            if "protection" in knight_config["potion"]["effect"]:
                potion_protection = (
                    knight_config)["potion"]["effect"]["protection"]

            if "hp" in knight_config["potion"]["effect"]:
                potion_hp = knight_config["potion"]["effect"]["hp"]

        self.potion = Potion(name=potion_name, power=potion_power,
                             hp=potion_hp, protection=potion_protection
                             )

    def apply_potion(self) -> None:
        self.hp += self.potion.hp
        self.power += self.potion.power
        self.protection += self.potion.protection

    def apply_armor(self) -> None:
        for armor in self.armor:
            self.protection += armor.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def prepare_for_battle(self) -> None:
        self.apply_weapon()
        self.apply_armor()
        self.apply_potion()

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
