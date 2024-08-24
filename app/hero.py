from __future__ import annotations

from app.equipment.armor import Armor
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Hero:
    def __init__(
        self,
        name: str = "Default knight",
        power: int = 20,
        hp: int = 50,
        armor: list[Armor] = None,
        weapon: Weapon = None,
        potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor or []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def create_from_config(cls, config: dict) -> Hero:
        armor_items = [
            Armor(item["part"], item["protection"])
            for item in config.get("armour", [])
        ]
        weapon_item = Weapon(
            config["weapon"]["name"], config["weapon"]["power"]
        ) if config.get("weapon") else None
        potion_item = Potion(
            config["potion"]["name"], config["potion"]["effect"]
        ) if config.get("potion") else None

        return cls(
            name=config.get("name"),
            power=config.get("power"),
            hp=config.get("hp"),
            armor=armor_items,
            weapon=weapon_item,
            potion=potion_item
        )

    def equip_armor(self) -> None:
        for item in self.armor:
            item.apply_effect(self)

    def equip_weapon(self) -> None:
        if self.weapon:
            self.weapon.apply_effect(self)

    def drink_potion(self) -> None:
        if self.potion:
            self.potion.apply_effect(self)

    def prepare_to_battle(self) -> None:
        self.equip_armor()
        self.equip_weapon()
        self.drink_potion()

    def attack(self, target: Hero) -> None:
        damage = self.power - target.protection
        target.hp -= max(damage, 0)
        if target.hp < 0:
            target.hp = 0

    def __repr__(self) -> str:
        hero_info = (
            "-----------------------------------------------------\n"
            f"Name: {self.name}\n"
            f"Power: {self.power}\n"
            f"HP: {self.hp}\n"
        )

        if self.weapon:
            hero_info += (f"Weapon: \n\t{self.weapon.name}, "
                          f"power = {self.weapon.power}\n")

        if self.armor:
            details = "".join(
                f"\t{item.name} = {item.protection}\n" for item in self.armor
            )
            hero_info += f"Armor: \n{details}"

        if self.potion:
            details = ", ".join(
                f"{stat} += {value}"
                for stat, value in self.potion.effect.items()
            )
            hero_info += f"Potion: \n\t{self.potion.name} ({details})\n"

        hero_info += "-----------------------------------------------------\n"
        return hero_info
