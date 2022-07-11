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

    knights = {}

    def __init__(self, name: str, power, hp, protection):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Knight.knights[self.name] = self

    def __sub__(self, other):
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0
        other.hp -= self.power - other.protection
        if other.hp < 0:
            other.hp = 0


def knight_to_class(knights):
    fighters = [value for key, value in knights.items()]
    for knight in fighters:
        name = knight["name"]
        power = knight["power"] + knight["weapon"]["power"]
        hp = knight["hp"]
        protection = sum(i["protection"] for i in knight["armour"])

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                power += knight["potion"]["effect"]["power"]
            if "hp" in knight["potion"]["effect"]:
                hp += knight["potion"]["effect"]["hp"]
            if "protection" in knight["potion"]["effect"]:
                protection += knight["potion"]["effect"]["protection"]

        Knight(name=name, power=power, hp=hp, protection=protection)


def battle(knights):
    knight_to_class(knights)
    lancelot = Knight.knights["Lancelot"]
    arthur = Knight.knights["Artur"]
    mordred = Knight.knights["Mordred"]
    red_knight = Knight.knights["Red Knight"]
    result_list = [lancelot, arthur, mordred, red_knight]

    # Battles

    lancelot - mordred
    arthur - red_knight

    return {i.name: i.hp for i in result_list}


print(battle(KNIGHTS))
