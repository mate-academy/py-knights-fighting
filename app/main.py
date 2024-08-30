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
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.power = stats["power"]
        self.hp = stats["hp"]
        self.armour = stats["armour"]
        self.weapon = stats["weapon"]
        self.potion = stats["potion"]
        self.protection = 0

    def apply_armor(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]

        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]


def battle_prepare(knight: dict) -> Knight:
    prepared_knight = Knight(knight)

    # apply armour
    prepared_knight.apply_armor()

    # apply weapon
    prepared_knight.apply_weapon()

    # apply potion if exist
    if prepared_knight.potion is not None:
        prepared_knight.apply_potion()

    return prepared_knight


def battle_action(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = battle_prepare(knights_config["lancelot"])

    # arthur
    arthur = battle_prepare(knights_config["arthur"])

    # mordred
    mordred = battle_prepare(knights_config["mordred"])

    # red_knight
    red_knight = battle_prepare(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_action(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battle_action(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
