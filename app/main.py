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


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: dict,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def preparation(self) -> None:
        # apply armour
        for i in self.armour:
            self.protection += i["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect, 0) + value)
            # if "power" in self.potion["effect"]:
            #     self.power += self.potion["effect"]["power"]
            #
            # if "protection" in self.potion["effect"]:
            #     self.protection += self.potion["effect"]["protection"]
            #
            # if "hp" in self.potion["effect"]:
            #     self.hp += self.potion["effect"]["hp"]

    def check_fall(self) -> None:
        if self.hp <= 0:
            self.hp = 0


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    first_knight.check_fall()
    second_knight.check_fall()


def battle(knightsconfig: dict) -> dict:
    knights = {}
    for name, stats in knightsconfig.items():
        knight = Knight(stats.get("name"),
                        stats.get("power"),
                        stats.get("hp"),
                        stats.get("armour"),
                        stats.get("weapon"),
                        stats.get("potion"))
        knight.preparation()
        knights[name] = knight

    lancelot = knights.get("lancelot")
    arthur = knights.get("arthur")
    mordred = knights.get("mordred")
    red_knight = knights.get("red_knight")

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
