from __future__ import annotations


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
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = data["armour"]
        self.protection = 0
        self.weapon = data["weapon"]
        self.potion = data.get("potion")

    def apply_armour(self) -> None:
        self.protection = sum(element["protection"] for element in self.armour)

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def check_fell(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def results_hp(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection

    def battle_pre(self, other_knight: Knight) -> None:
        # BATTLE PREPARATIONS:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()

        other_knight.apply_armour()
        other_knight.apply_weapon()
        other_knight.apply_potion_if_exist()

        # BATTLE:
        self.results_hp(other_knight)
        self.check_fell()
        other_knight.check_fell()

    def __str__(self) -> str:
        return f"{self.name}: {self.hp}"


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(data) for name, data in knights_config.items()}

    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    arthur = knights.get("arthur")
    red_knight = knights.get("red_knight")

    if lancelot and mordred:
        lancelot.battle_pre(mordred)

    if arthur and red_knight:
        arthur.battle_pre(red_knight)

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
