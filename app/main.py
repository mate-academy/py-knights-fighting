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
    def __init__(self, config):
        self.name = config["name"]

        self.hp = config["hp"]
        self.power = config["power"]

        self.__apply_armour(config["armour"])
        self.__apply_weapon(config["weapon"])

        if config["potion"]:
            self.__apply_potion(config["potion"])

    def __apply_armour(self, armour):
        for part in armour:
            self.hp += part["protection"]

    def __apply_weapon(self, weapon):
        self.power += weapon["power"]

    def __apply_potion(self, potion):
        effect = potion["effect"]

        if "hp" in effect:
            self.hp += effect["hp"]
        if "protection" in effect:
            self.hp += effect["protection"]
        if "power" in effect:
            self.power += effect["power"]

    def damage(self, damage_amount):
        if self.hp < damage_amount:
            self.hp = 0
        else:
            self.hp -= damage_amount


def battle(knights_config):
    knights = []

    for knight in knights_config:
        knights.append(Knight(knights_config[knight]))

    knights[0].damage(knights[2].power)
    knights[2].damage(knights[0].power)

    knights[1].damage(knights[3].power)
    knights[3].damage(knights[1].power)

    return {knight.name: knight.hp for knight in knights}
