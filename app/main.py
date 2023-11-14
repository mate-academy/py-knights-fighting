KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50, },
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
        "weapon": {"name": "Two-handed Sword", "power": 55, },
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
        "weapon": {"name": "Poisoned Sword", "power": 60, },
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
        name: str,
        power: float,
        hp: float,
        armour: list,
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
        self.prepare()

    def prepare(self) -> None:
        # apply armour
        for armour in self.armour:
            self.protection += armour["protection"]

        # apply power
        self.power += self.weapon["power"]

        # apply effects
        if self.potion:
            if "hp" in self.potion["effect"].keys():
                self.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"].keys():
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"].keys():
                self.protection += self.potion["effect"]["protection"]

    def fight(self, enemy: "Knight") -> None:
        self.hp -= enemy.power - self.protection
        if self.hp <= 0:
            self.hp = 0

        enemy.hp -= self.power - enemy.protection
        if enemy.hp <= 0:
            enemy.hp = 0


def battle(knights: dict) -> dict:
    lancelot_knight = Knight(
        list(knights.keys())[0],
        knights[list(knights.keys())[0]]["power"],
        knights[list(knights.keys())[0]]["hp"],
        knights[list(knights.keys())[0]]["armour"],
        knights[list(knights.keys())[0]]["weapon"],
        knights[list(knights.keys())[0]]["potion"]
    )
    arthur_knight = Knight(
        list(knights.keys())[1],
        knights[list(knights.keys())[1]]["power"],
        knights[list(knights.keys())[1]]["hp"],
        knights[list(knights.keys())[1]]["armour"],
        knights[list(knights.keys())[1]]["weapon"],
        knights[list(knights.keys())[1]]["potion"]
    )
    mordred_knight = Knight(
        list(knights.keys())[2],
        knights[list(knights.keys())[2]]["power"],
        knights[list(knights.keys())[2]]["hp"],
        knights[list(knights.keys())[2]]["armour"],
        knights[list(knights.keys())[2]]["weapon"],
        knights[list(knights.keys())[2]]["potion"]
    )
    red_knight = Knight(
        list(knights.keys())[3],
        knights[list(knights.keys())[3]]["power"],
        knights[list(knights.keys())[3]]["hp"],
        knights[list(knights.keys())[3]]["armour"],
        knights[list(knights.keys())[3]]["weapon"],
        knights[list(knights.keys())[3]]["potion"]
    )

    result = {}

    lancelot_knight.fight(mordred_knight)
    arthur_knight.fight(red_knight)

    result["Lancelot"] = lancelot_knight.hp
    result["Arthur"] = arthur_knight.hp
    result["Mordred"] = mordred_knight.hp
    result["Red Knight"] = red_knight.hp
    return result
