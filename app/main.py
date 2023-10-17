KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50,},
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
        "weapon": {"name": "Two-handed Sword", "power": 55,},
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
        "weapon": {"name": "Poisoned Sword", "power": 60,},
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

    def prepare(self):
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

    def fight(self, enemy) -> None:
        self.hp -= enemy.power - self.protection
        if self.hp <= 0:
            self.hp = 0
        
        enemy.hp -= self.power - enemy.protection
        if enemy.hp <= 0:
            enemy.hp = 0


lancelot_knight = Knight(
    list(KNIGHTS.keys())[0],
    KNIGHTS[list(KNIGHTS.keys())[0]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["potion"]
)
arthur_knight = Knight(
        list(KNIGHTS.keys())[1],
    KNIGHTS[list(KNIGHTS.keys())[1]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["potion"]
)
mordred_knight = Knight(
        list(KNIGHTS.keys())[2],
    KNIGHTS[list(KNIGHTS.keys())[2]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["potion"]
)
red_knight = Knight(
        list(KNIGHTS.keys())[3],
    KNIGHTS[list(KNIGHTS.keys())[3]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["potion"]
)


def tournament(lancelot_knight, arthur_knight, mordred_knight, red_knight):
    lancelot_knight.fight(arthur_knight)
    mordred_knight.fight(red_knight)

