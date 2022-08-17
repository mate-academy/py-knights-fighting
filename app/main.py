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


def battle(KNIGHTS):
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

    lancelot_values = KNIGHTS["lancelot"]
    armour_lancelot = [Armour(item["part"], item["protection"])
                       for item in lancelot_values["armour"]]
    arthur_values = KNIGHTS["arthur"]
    armour_arthur = [Armour(item["part"], item["protection"])
                     for item in arthur_values["armour"]]
    mordred_values = KNIGHTS["mordred"]
    armour_mordred = [Armour(item["part"], item["protection"])
                      for item in mordred_values["armour"]]
    red_knight_values = KNIGHTS["red_knight"]
    armour_red_knight = [Armour(item["part"], item["protection"])
                         for item in red_knight_values["armour"]]

    lancelot = Knight(lancelot_values["name"],
                      lancelot_values["power"],
                      lancelot_values["hp"],
                      armour_lancelot,
                      Weapon(lancelot_values["weapon"]["name"],
                             lancelot_values["weapon"]["power"]),
                      lancelot_values["potion"])

    arthur = Knight(arthur_values["name"],
                    arthur_values["power"],
                    arthur_values["hp"],
                    armour_arthur,
                    Weapon(arthur_values["weapon"]["name"],
                           arthur_values["weapon"]["power"]),
                    arthur_values["potion"])

    mordred = Knight(mordred_values["name"],
                     mordred_values["power"],
                     mordred_values["hp"],
                     armour_mordred,
                     Weapon(mordred_values["weapon"]["name"],
                            mordred_values["weapon"]["power"]),
                     mordred_values["potion"])

    red_knight = Knight(red_knight_values["name"],
                        red_knight_values["power"],
                        red_knight_values["hp"],
                        armour_red_knight,
                        Weapon(red_knight_values["weapon"]["name"],
                               red_knight_values["weapon"]["power"]),
                        red_knight_values["potion"])

    list_knights = [lancelot, arthur, mordred, red_knight]

    list_knights = [lancelot, arthur, mordred, red_knight]
    for knight in list_knights:
        sum_armour = 0
        for i in knight.armour:
            sum_armour += i.protection
        knight.armour = sum_armour

    for knight in list_knights:
        knight.power = knight.power + knight.weapon.power

    for knight in list_knights:
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

    for knight in list_knights:
        if knight.hp < 0:
            knight.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
