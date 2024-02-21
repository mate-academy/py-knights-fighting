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
    def __init__(
            self,
            name: int, power: int, hp: int,
            armour: dict, weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        # Apply armour
        self.protection = sum(item["protection"] for item in self.armour)
        # Apply weapon
        self.power += self.weapon["power"]
        # Apply potion if exist
        if self.potion is not None:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]

        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # 2 Arthur vs Red Knight:
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
