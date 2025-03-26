from app.knights.knight_class import Knight


def battle(knights: dict) -> dict:

    lancelot = Knight(
        name=knights["lancelot"]["name"],
        power=knights["lancelot"]["power"],
        hp=knights["lancelot"]["hp"],
        armour=knights["lancelot"]["armour"],
        weapon=knights["lancelot"]["weapon"],
        potion=knights["lancelot"]["potion"]
    )

    arthur = Knight(
        name=knights["arthur"]["name"],
        power=knights["arthur"]["power"],
        hp=knights["arthur"]["hp"],
        armour=knights["arthur"]["armour"],
        weapon=knights["arthur"]["weapon"],
        potion=knights["arthur"]["potion"]
    )

    mordred = Knight(
        name=knights["mordred"]["name"],
        power=knights["mordred"]["power"],
        hp=knights["mordred"]["hp"],
        armour=knights["mordred"]["armour"],
        weapon=knights["mordred"]["weapon"],
        potion=knights["mordred"]["potion"]
    )

    red_knight = Knight(
        name=knights["red_knight"]["name"],
        power=knights["red_knight"]["power"],
        hp=knights["red_knight"]["hp"],
        armour=knights["red_knight"]["armour"],
        weapon=knights["red_knight"]["weapon"],
        potion=knights["red_knight"]["potion"]
    )

    # battle1
    lancelot.take_damage(mordred.power), mordred.take_damage(lancelot.power)

    # battle2
    arthur.take_damage(red_knight.power), red_knight.take_damage(arthur.power)

    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
