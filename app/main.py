from app.armour import armour
from app.weapon import weapon
from app.potion import potion


def battle(knights: dict) -> dict:
    armour(knights)
    weapon(knights)
    potion(knights)

    knights["lancelot"]["hp"] -= (knights["mordred"]["power"]
                                  - knights["lancelot"]["protection"])
    knights["mordred"]["hp"] -= (knights["lancelot"]["power"]
                                 - knights["mordred"]["protection"])

    if knights["lancelot"]["hp"] <= 0:
        knights["lancelot"]["hp"] = 0

    if knights["mordred"]["hp"] <= 0:
        knights["mordred"]["hp"] = 0

    knights["arthur"]["hp"] -= (knights["red_knight"]["power"]
                                - knights["arthur"]["protection"])
    knights["red_knight"]["hp"] -= (knights["arthur"]["power"]
                                    - knights["red_knight"]["protection"])

    if knights["arthur"]["hp"] <= 0:
        knights["arthur"]["hp"] = 0

    if knights["red_knight"]["hp"] <= 0:
        knights["red_knight"]["hp"] = 0

    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["arthur"]["name"]: knights["arthur"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
        knights["red_knight"]["name"]: knights["red_knight"]["hp"],
    }
