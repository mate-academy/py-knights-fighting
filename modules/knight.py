from __future__ import annotations
from modules.arsenal import Armor, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0,
            armor: list[Armor] = [],
            weapon: Weapon = None,
            potion: None | Potion = None
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.armor = armor
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


KNIGHTS = {
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
        "name": "Arthur",
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
