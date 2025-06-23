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


class BattleOfKnights:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection
        self.add_protection()
        self.add_power_from_weapon()
        self.add_potion()

    def add_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def add_power_from_weapon(self) -> None:
        self.power += self.weapon["power"]

    def add_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def fight(self, other: "BattleOfKnights") -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0


def battle(knightsconfig: dict) -> dict:
    dict_of_knights = {}
    for knight in knightsconfig:
        dict_of_knights[knight] = BattleOfKnights(
            knightsconfig[knight]["name"],
            knightsconfig[knight]["power"],
            knightsconfig[knight]["hp"],
            knightsconfig[knight]["armour"],
            knightsconfig[knight]["weapon"],
            knightsconfig[knight]["potion"],
        )
    dict_of_knights["lancelot"].fight(dict_of_knights["mordred"])
    dict_of_knights["arthur"].fight(dict_of_knights["red_knight"])
    return {knight.name: knight.hp for knight in dict_of_knights.values()}
