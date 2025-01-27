def battle_knights(knights: list) -> dict:
    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    lancelot.stats["hp"] -= (mordred.stats["power"]
                             - lancelot.stats["protection"])
    mordred.stats["hp"] -= (lancelot.stats["power"]
                            - mordred.stats["protection"])

    # check if someone fell in battle
    if lancelot.stats["hp"] <= 0:
        lancelot.stats["hp"] = 0

    if mordred.stats["hp"] <= 0:
        mordred.stats["hp"] = 0

    arthur.stats["hp"] -= (red_knight.stats["power"]
                           - arthur.stats["protection"])
    red_knight.stats["hp"] -= (arthur.stats["power"]
                               - red_knight.stats["protection"])

    # check if someone fell in battle
    if arthur.stats["hp"] <= 0:
        arthur.stats["hp"] = 0

    if red_knight.stats["hp"] <= 0:
        red_knight.stats["hp"] = 0

    return {
        lancelot.name: lancelot.stats["hp"],
        arthur.name: arthur.stats["hp"],
        mordred.name: mordred.stats["hp"],
        red_knight.name: red_knight.stats["hp"],
    }
