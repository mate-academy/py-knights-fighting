from app.knight_stats import KNIGHTS
from app.knight import Knight


def battle(cfg):

    # Knights are coming to the arena
    lancelot = Knight(cfg["lancelot"]["name"],
                      cfg["lancelot"]["power"],
                      cfg["lancelot"]["hp"],
                      cfg["lancelot"]["armour"],
                      cfg["lancelot"]["weapon"],
                      cfg["lancelot"]["potion"])

    arthur = Knight(cfg["arthur"]["name"],
                    cfg["arthur"]["power"],
                    cfg["arthur"]["hp"],
                    cfg["arthur"]["armour"],
                    cfg["arthur"]["weapon"],
                    cfg["arthur"]["potion"])

    mordred = Knight(cfg["mordred"]["name"],
                     cfg["mordred"]["power"],
                     cfg["mordred"]["hp"],
                     cfg["mordred"]["armour"],
                     cfg["mordred"]["weapon"],
                     cfg["mordred"]["potion"])

    red_knight = Knight(cfg["red_knight"]["name"],
                        cfg["red_knight"]["power"],
                        cfg["red_knight"]["hp"],
                        cfg["red_knight"]["armour"],
                        cfg["red_knight"]["weapon"],
                        cfg["red_knight"]["potion"])

    # preparation
    lancelot.equip().drink_potion()
    arthur.equip().drink_potion()
    mordred.equip().drink_potion()
    red_knight.equip().drink_potion()

    # FIGHT!
    lancelot.challenge(mordred)
    arthur.challenge(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
