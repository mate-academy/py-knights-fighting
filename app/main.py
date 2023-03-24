from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int | float,
                 hp: int | float,
                 armour: list[dict] | None,
                 weapon: dict,
                 potion: dict
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def __str__(self) -> str:
        return f"(" \
               f"{self.name}, " \
               f"{self.power}, " \
               f"{self.hp}, " \
               f"{self.armour}, " \
               f"{self.weapon}, " \
               f"{self.potion})"

    def wear_armour(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

    def take_weapon(self) -> None:
        self.power += self.weapon["power"]

    def drink_potion(self) -> None:
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect, 0) + value)

    def battle_results(self: Knight, other: Knight) -> None:
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


def battle(dict_with_knights: dict) -> dict:
    for knight, knight_config in dict_with_knights.items():
        prepared_knight = Knight(
            knight_config["name"],
            knight_config["power"],
            knight_config["hp"],
            knight_config["armour"],
            knight_config["weapon"],
            knight_config["potion"]
        )

        dict_with_knights[knight] = prepared_knight
        prepared_knight.wear_armour()
        prepared_knight.take_weapon()
        dict_with_knights[knight].drink_potion()

    dict_with_knights["lancelot"].battle_results(dict_with_knights["mordred"])
    dict_with_knights["arthur"].battle_results(dict_with_knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in dict_with_knights.values()
    }
