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


class Knights:
    def __init__(self, configurations):
        # for i in configurations.values():
        self.name = configurations['name']
        self.hp = configurations["hp"]
        self.power = configurations["power"]
        self.apply_arm(configurations["armour"])
        self.apply_weapon(configurations["weapon"])
        if configurations["potion"]:
            self.apply_potions(configurations["potion"])

    def apply_arm(self, armor):
        for health in armor:
            self.hp += health["protection"]

    def apply_weapon(self, weapon):
        self.power += weapon["power"]

    def apply_potions(self, potion):
        pot_effect = potion["effect"]
        if "hp" in pot_effect:
            self.hp += pot_effect["hp"]
        if "protection" in pot_effect:
            self.hp += pot_effect["protection"]
        if "power" in pot_effect:
            self.power += pot_effect["power"]

    def damage(self, amount_of_damage):
        if amount_of_damage > self.hp:
            self.hp = 0
        else:
            self.hp -= amount_of_damage

    def battle(knights_config):
        knights = []
        for knight in knights_config.values():
            knights.append(Knights(knight))
        knights[0].damage(knights[2].power)
        knights[2].damage(knights[0].power)
        knights[1].damage(knights[3].power)
        knights[3].damage(knights[1].power)
        return {knight.name: knight.hp for knight in knights}
