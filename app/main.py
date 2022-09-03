from app.knight.knight import Knight


def battle(knightsConfig):
    # create knights instances

    lancelot_dict = knightsConfig["lancelot"]
    lancelot = Knight(lancelot_dict["name"],
                      lancelot_dict["power"],
                      lancelot_dict["hp"])
    arthur_dict = knightsConfig["arthur"]
    arthur = Knight(arthur_dict["name"],
                    arthur_dict["power"],
                    arthur_dict["hp"])
    mordred_dict = knightsConfig["mordred"]
    mordred = Knight(mordred_dict["name"],
                     mordred_dict["power"],
                     mordred_dict["hp"])
    red_knight_dict = knightsConfig["red_knight"]
    red_knight = Knight(red_knight_dict["name"],
                        red_knight_dict["power"],
                        red_knight_dict["hp"])

    # apply armour

    lancelot.get_armour(lancelot_dict)
    arthur.get_armour(arthur_dict)
    mordred.get_armour(mordred_dict)
    red_knight.get_armour(red_knight_dict)

    # get weapons

    lancelot.get_weapon(lancelot_dict)
    arthur.get_weapon(arthur_dict)
    mordred.get_weapon(mordred_dict)
    red_knight.get_weapon(red_knight_dict)

    # create and apply potion instances

    lancelot.get_potion(lancelot_dict)
    arthur.get_potion(arthur_dict)
    mordred.get_potion(mordred_dict)
    red_knight.get_potion(red_knight_dict)

    # knights fight

    arthur.fight(red_knight)
    lancelot.fight(mordred)

    # return results

    result = {lancelot.name: lancelot.hp,
              arthur.name: arthur.hp,
              mordred.name: mordred.hp,
              red_knight.name: red_knight.hp}
    return result
