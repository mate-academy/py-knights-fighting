from __future__ import annotations

from app.inventory.knight_inventory import Armour, Weapon, Potion


class Knight:

    def __init__(self, knight_config: dict) -> None:
        self.name: str = knight_config["name"]
        self.power: int = knight_config["power"]
        self.hp: int = knight_config["hp"]
        self.armour: dict = knight_config["armour"]
        self.weapon: dict = knight_config["weapon"]
        self.potion: dict = knight_config["potion"]
        self.protection: int = 0
        self.prepare_for_battle()

    def put_on_armour(self) -> None:
        armour_list = [Armour(armour_part) for armour_part in self.armour]
        for armour_part in armour_list:
            self.protection += armour_part.protection

    def take_weapon(self) -> None:
        weapon = Weapon(self.weapon)
        self.power += weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            potion = Potion(self.potion)
            if "power" in potion.effect:
                self.power += potion.effect["power"]
            if "protection" in potion.effect:
                self.protection += potion.effect["protection"]
            if "hp" in potion.effect:
                self.hp += potion.effect["hp"]

    def prepare_for_battle(self) -> None:
        self.put_on_armour()
        self.take_weapon()
        self.apply_potion()

    def attack(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
