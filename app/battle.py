from knights import Knight


def battle() -> dict:
    for fighter in Knight.knights:
        if fighter.armour:
            fighter.hp += sum(fighter.armour)
        fighter.power += fighter.weapon
        if fighter.potion is not None:
            if "power" in fighter.potion:
                fighter.power += fighter.potion["power"]
            if "protection" in fighter.potion:
                fighter.hp += fighter.potion["protection"]
            if "hp" in fighter.potion:
                fighter.hp += fighter.potion["hp"]

    lancelot = Knight.knights[0]
    arthur = Knight.knights[1]
    mordred = Knight.knights[2]
    red_knight = Knight.knights[3]

    # 1
    lancelot.hp -= mordred.power
    mordred.hp -= lancelot.power

    # 2
    arthur.hp -= red_knight.power
    red_knight.hp -= arthur.power

    for fighter in Knight.knights:
        if fighter.hp < 0:
            fighter.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
