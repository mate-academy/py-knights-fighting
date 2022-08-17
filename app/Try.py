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

Lancelot = KNIGHTS["lancelot"]
Arthur = KNIGHTS["arthur"]
Mordred = KNIGHTS["mordred"]
Red_knight = KNIGHTS["red_knight"]


lancelot = Knight(Lancelot["name"],
                  Lancelot["power"],
                  Lancelot["hp"],
                  Lancelot["armour"],
                  Lancelot["weapon"],
                  Lancelot["potion"])

arthur = Knight(Arthur["name"],
                Arthur["power"],
                Arthur["hp"],
                Arthur["armour"],
                Arthur["weapon"],
                Arthur["potion"])

mordred = Knight(Mordred["name"],
                 Mordred["power"],
                 Mordred["hp"],
                 Mordred["armour"],
                 Mordred["weapon"],
                 Mordred["potion"])

red_knight = Knight(Red_knight["name"],
                    Red_knight["power"],
                    Red_knight["hp"],
                    Red_knight["armour"],
                    Red_knight["weapon"],
                    Red_knight["potion"])

list_knights = [lancelot, arthur, mordred, red_knight]


def battle(list_knights):
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
    list_knights = [lancelot, arthur, mordred, red_knight]
    for knight in list_knights:
        if knight.hp < 0:
            knight.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}

