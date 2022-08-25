from app.classess import Weapon, Knight, Armour


def battle(KNIGHTS):

    lancelot_values = KNIGHTS["lancelot"]
    arthur_values = KNIGHTS["arthur"]
    mordred_values = KNIGHTS["mordred"]
    red_knight_values = KNIGHTS["red_knight"]

    lancelot = Knight(lancelot_values["name"],
                      lancelot_values["power"],
                      lancelot_values["hp"],
                      [Armour(item["part"], item["protection"])
                       for item in lancelot_values["armour"]],
                      Weapon(lancelot_values["weapon"]["name"],
                             lancelot_values["weapon"]["power"]),
                      lancelot_values["potion"])

    arthur = Knight(arthur_values["name"],
                    arthur_values["power"],
                    arthur_values["hp"],
                    [Armour(item["part"], item["protection"])
                     for item in arthur_values["armour"]],
                    Weapon(arthur_values["weapon"]["name"],
                           arthur_values["weapon"]["power"]),
                    arthur_values["potion"])

    mordred = Knight(mordred_values["name"],
                     mordred_values["power"],
                     mordred_values["hp"],
                     [Armour(item["part"], item["protection"])
                      for item in mordred_values["armour"]],
                     Weapon(mordred_values["weapon"]["name"],
                            mordred_values["weapon"]["power"]),
                     mordred_values["potion"])

    red_knight = Knight(red_knight_values["name"],
                        red_knight_values["power"],
                        red_knight_values["hp"],
                        [Armour(item["part"], item["protection"])
                         for item in red_knight_values["armour"]],
                        Weapon(red_knight_values["weapon"]["name"],
                               red_knight_values["weapon"]["power"]),
                        red_knight_values["potion"])

    list_knights = [lancelot, arthur, mordred, red_knight]

    list_knights = [lancelot, arthur, mordred, red_knight]
    for knight in list_knights:
        sum_armour = 0
        for armour in knight.armour:
            sum_armour += armour.protection
        knight.armour = sum_armour
        knight.power = knight.power + knight.weapon.power
        if knight.potion is not None:
            potion = knight.potion["effect"]
            knight.hp = knight.hp + potion["hp"]
            knight.power = knight.power + potion["power"]
            if len(potion) == 3:
                knight.armour = \
                    knight.armour + potion["protection"]
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
