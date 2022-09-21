from __future__ import annotations

from app.character.inventory import Inventory


class Knight:
    def __init__(self,
                 k_name: str,
                 k_power: int = 1,
                 k_hp: int = 1,
                 k_armors=[],
                 k_weapon=None,
                 k_potion=None
                 ) -> None:
        self.name = k_name
        self.power = k_power
        self.hp = k_hp
        self.protection = 0
        self.items = Inventory(k_weapon, k_armors, k_potion)
        self.is_ready = False
        self.is_armored = False
        self.is_weapon_up = False
        self.effect = None

    @classmethod
    def from_dict(cls, pers: dict) -> Knight:
        return cls(
            pers["name"],
            pers["power"],
            pers["hp"],
            pers["armour"],
            pers["weapon"],
            pers["potion"]
        )

    def use_potion(self):
        if self.items.potion:
            print(f"{self.name} drinking potion {self.items.potion.name}")
            boost = self.items.potion.effect
            boost_k = boost.keys()
            if "hp" in boost_k:
                self.hp += boost["hp"]
            if "power" in boost_k:
                self.power += boost["power"]
            if "protection" in boost_k:
                self.protection += boost["protection"]
            self.items.potion = None
            self.effect = boost
        else:
            print(f"{self.name} hasn't potion")

    def armor_up(self):
        if self.items.armors:
            if not self.is_armored:
                for arm in self.items.armors:
                    self.protection += arm.protection
                    print(f"{self.name} wear {arm.part}")
                self.is_armored = True
                if self.is_weapon_up:
                    self.is_ready = True
            else:
                print(f"{self.name} is already armored!")
        else:
            print(f"{self.name} hasn't armors!")

    def armor_down(self):
        if self.items.armors:
            if self.is_armored:
                for arm in self.items.armors:
                    self.protection -= arm.protection
                    print(f"{self.name} unwearied {arm.part}")
                self.is_armored = False
                self.is_ready = False
            else:
                print(f"{self.name} is without armors!")
        else:
            print(f"{self.name} hasn't armors!")

    def weapon_up(self):
        if self.items.weapon:
            if not self.is_weapon_up:
                self.power += self.items.weapon.power
                print(f"{self.name} raised his {self.items.weapon.name}")
                self.is_weapon_up = True
                if self.is_armored:
                    self.is_ready = True
        else:
            print(f"{self.name} hasn't weapon!")

    def weapon_down(self):
        if self.items.weapon:
            if self.is_weapon_up:
                self.power -= self.items.weapon.power
                print(f"{self.name} dropped his {self.items.weapon.name}")
                self.is_weapon_up = True
                if self.is_armored:
                    self.is_ready = True
        else:
            print(f"{self.name} hasn't weapon!")

    def ready_up(self):
        if not self.is_ready:

            self.weapon_up()
            self.armor_up()
            if self.items.potion:
                self.use_potion()

            self.is_ready = True
            print(f"{self.name} is ready!!!")

        else:
            print(f"{self.name} is already ready!!!")

    def ready_down(self):
        if not self.is_ready:

            self.weapon_down()
            self.armor_down()
            if self.effect:
                p_name = self.items.potion.name
                print(f"{p_name}'s duration is out for {self.name}")
                boost = self.effect
                if boost["hp"]:
                    self.hp -= boost["hp"]
                if boost["power"]:
                    self.power -= boost["power"]
                if boost["protection"]:
                    self.protection -= boost["protection"]
                self.effect = None

            self.is_ready = False

        else:
            print(f"{self.name} is already ready!!!")
