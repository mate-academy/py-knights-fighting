from __future__ import annotations

from app.character.inventory import Inventory


class Knight:
    def __init__(self,
                 name: str,
                 power: int = 1,
                 hp: int = 1,
                 armors: list[dict] = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.items = Inventory(weapon, armors, potion)
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

    def use_potion(self) -> None:
        if self.items.potion:
            print(f"{self.name} drinking potion {self.items.potion.name}")
            boost = self.items.potion.effect
            boost_keys = boost.keys()
            if "hp" in boost_keys:
                self.hp += boost["hp"]
            if "power" in boost_keys:
                self.power += boost["power"]
            if "protection" in boost_keys:
                self.protection += boost["protection"]
            self.items.potion = None
            self.effect = boost
        else:
            print(f"{self.name} hasn't potion")

    def potion_during_down(self) -> None:
        if self.effect:
            p_name = self.items.potion.name
            print(f"{p_name}'s duration is out for {self.name}")
            boost = self.effect
            boost_keys = boost.keys()
            if "hp" in boost_keys:
                self.hp -= boost["hp"]
            if "power" in boost_keys:
                self.power -= boost["power"]
            if "protection" in boost_keys:
                self.protection -= boost["protection"]
            self.effect = None

    def armor_up(self) -> None:
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

    def armor_down(self) -> None:
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

    def weapon_up(self) -> None:
        if self.items.weapon:
            if not self.is_weapon_up:
                self.power += self.items.weapon.power
                print(f"{self.name} raised his {self.items.weapon.name}")
                self.is_weapon_up = True
                if self.is_armored:
                    self.is_ready = True
        else:
            print(f"{self.name} hasn't weapon!")

    def weapon_down(self) -> None:
        if self.items.weapon:
            if self.is_weapon_up:
                self.power -= self.items.weapon.power
                print(f"{self.name} dropped his {self.items.weapon.name}")
                self.is_weapon_up = True
                if self.is_armored:
                    self.is_ready = True
        else:
            print(f"{self.name} hasn't weapon!")

    def ready_up(self) -> None:
        if not self.is_ready:

            self.weapon_up()
            self.armor_up()
            self.use_potion()

            self.is_ready = True
            print(f"{self.name} is ready!!!")

        else:
            print(f"{self.name} is already ready!!!")

    def ready_down(self) -> None:
        if not self.is_ready:

            self.weapon_down()
            self.armor_down()
            self.potion_during_down()

            self.is_ready = False

        else:
            print(f"{self.name} is already ready!!!")


default_knights = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Artur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}
