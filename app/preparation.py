def prepare_for_fight(fighters: list):

    for knight in fighters.values():
        # print(knight.armor)
        knight.protection = equip_armour(knight.armour)
        knight.power += equip_weapon(knight.weapon)
        drink_potion(knight, knight.potion)

    return fighters


def equip_armour(armours: list):
    protect = 0
    for armour in armours:
        protect += armour["protection"]
    return protect


def equip_weapon(weapon: dict):
    return weapon["power"]


def drink_potion(knight, potion: dict):
    if potion:
        if "power" in potion["effect"]:
            knight.power += potion["effect"]["power"]

        if "protection" in potion["effect"]:
            knight.protection += potion["effect"]["protection"]

        if "hp" in potion["effect"]:
            knight.hp += potion["effect"]["hp"]
