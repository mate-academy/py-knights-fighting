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

class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

lancelot_ = KNIGHTS["lancelot"]
armour_lancelot = ([Armour(item["part"], item["protection"]) for item in lancelot_["armour"] ] if lancelot_["armour"] else [])
arthur_ = KNIGHTS["arthur"]
armour_arthur = [Armour(item["part"], item["protection"]) for item in arthur_["armour"]]
mordred_ = KNIGHTS["mordred"]
armour_mordred = [Armour(item["part"], item["protection"]) for item in mordred_["armour"]]
red_knight_ = KNIGHTS["red_knight"]
armour_red_knight = [Armour(item["part"], item["protection"]) for item in red_knight_["armour"]]

lancelot = Knight(name=lancelot_["name"],
                  power=lancelot_["power"],
                  hp=lancelot_["hp"],
                  armour=armour_lancelot,
                  weapon=Weapon(lancelot_["weapon"]["name"], lancelot_["weapon"]["power"]),
                  potion=lancelot_["potion"])

arthur = Knight(arthur_["name"],
                arthur_["power"],
                arthur_["hp"],
                armour_arthur,
                Weapon(arthur_["weapon"]["name"], arthur_["weapon"]["power"]),
                arthur_["potion"])

mordred = Knight(mordred_["name"],
                 mordred_["power"],
                 mordred_["hp"],
                 armour_mordred,
                 Weapon(mordred_["weapon"]["name"], mordred_["weapon"]["power"]),
                 mordred_["potion"])

red_knight = Knight(red_knight_["name"],
                    red_knight_["power"],
                    red_knight_["hp"],
                    armour_red_knight,
                    Weapon(red_knight_["weapon"]["name"], red_knight_["weapon"]["power"]),
                    red_knight_["potion"])

list_knights = [lancelot, arthur, mordred, red_knight]


def battle(list_knights):
    for knight in range(len(list_knights)):
        sum_armour = 0
        for i in list_knights[knight].armour:
            sum_armour += i.protection
        knight.armour = sum_armour

    for knight in list_knights_:
        knight.power = knight.power + knight.weapon.power

    for knight in list_knights_:
        if knight.potion is not None:
            a = knight.potion["effect"]
            knight.hp = knight.hp + a["hp"]
            knight.power = knight.power + a["power"]
            if len(a) == 3:
                knight.armour = knight.armour + a["protection"]
            else:
                pass

    lancelot.hp -= mordred.power - lancelot.armour
    mordred.hp -= lancelot.power - mordred.armour
    arthur.hp -= red_knight.power - arthur.armour
    red_knight.hp -= arthur.power - red_knight.armour

    for knight in list_knights_:
        if knight.hp < 0:
            knight.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}

print(lancelot.armour)