from typing import Any
# I dont now why you dont see my files
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


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        items_in_backpack = ["armour", "weapon", "potion"]
        self.backpack = {
            key: knight[key] for key in items_in_backpack if key in knight
        }

    def apply_armour(self) -> None:
        if self.backpack["armour"]:
            for armour in self.backpack["armour"]:
                self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.backpack["weapon"]["power"]

    def apply_potion(self) -> None:
        if self.backpack["potion"] is not None:
            if "power" in self.backpack["potion"]["effect"]:
                self.power += self.backpack["potion"]["effect"]["power"]

            if "protection" in self.backpack["potion"]["effect"]:
                self.protection += (
                    self.backpack["potion"]["effect"]["protection"]
                )

            if "hp" in self.backpack["potion"]["effect"]:
                self.hp += self.backpack["potion"]["effect"]["hp"]

    def battle(self, other: Any) -> None:
        if other.power - self.protection > 0:
            self.hp -= other.power - self.protection

        if self.power - other.protection > 0:
            other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0


def battle(base_knights_config: dict) -> dict:
    # create a list with individual knights
    knights = [value for value in base_knights_config.values()]
    list_dict = []
    for knight in knights:
        list_dict.append(knight)
    # create a list with knight objects
    list_kinghts = []
    for item in list_dict:
        list_kinghts.append(Knight(item))

    for knight in list_kinghts:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()
    lancelot, arthur, mordred, red_knight = list_kinghts
    arthur.battle(red_knight)
    lancelot.battle(mordred)
    result_battle = {
        arthur.name: arthur.hp,
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
    return result_battle


battle(KNIGHTS)
