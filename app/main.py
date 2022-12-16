from app.data import KNIGHTS
from knights_battle.battle import knights_battle
from knights.knight import Knight


def battle(knightsconfig: callable) -> dict:
    # lancelot
    lancelot = Knight("Lancelot", knightsconfig["lancelot"]["power"],
                      knightsconfig["lancelot"]["hp"])
    lancelot.using_armour(knightsconfig["lancelot"]["armour"],
                          knightsconfig["lancelot"]["weapon"]["power"])
    lancelot.using_potion(knightsconfig["lancelot"]["potion"])

    # mordred
    mordred = Knight("Mordred", knightsconfig["mordred"]["power"],
                     knightsconfig["mordred"]["hp"])
    mordred.using_armour(knightsconfig["mordred"]["armour"],
                         knightsconfig["mordred"]["weapon"]["power"])
    mordred.using_potion(knightsconfig["mordred"]["potion"])

    # arthur
    arthur = Knight("Artur", knightsconfig["arthur"]["power"],
                    knightsconfig["arthur"]["hp"])
    arthur.using_armour(knightsconfig["arthur"]["armour"],
                        knightsconfig["arthur"]["weapon"]["power"])
    arthur.using_potion(knightsconfig["arthur"]["potion"])

    # red_knight
    red_knight = Knight("Red Knight", knightsconfig["red_knight"]["power"],
                        knightsconfig["red_knight"]["hp"])
    red_knight.using_armour(knightsconfig["red_knight"]["armour"],
                            knightsconfig["red_knight"]["weapon"]["power"])
    red_knight.using_potion(knightsconfig["red_knight"]["potion"])

    first_battle = knights_battle(lancelot, mordred)
    second_battle = knights_battle(arthur, red_knight)
    result = {
        "Lancelot": first_battle["Lancelot"],
        "Artur": second_battle["Artur"],
        "Mordred": first_battle["Mordred"],
        "Red Knight": second_battle["Red Knight"],
    }
    print(result)
    return result


print(battle(KNIGHTS))
