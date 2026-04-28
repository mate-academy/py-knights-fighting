from app.knight_prepare.knight import Knight


def prepare_knights(knights: dict) -> dict:
    ready_knights = {}

    for key, equip in knights.items():
        knight = Knight(
            equip.get("name"),
            equip.get("power"),
            equip.get("hp"),
            equip.get("weapon"),
            equip.get("armour"),
            equip.get("potion")
        )

        knight.equip_knight()
        ready_knights[key] = knight

    return ready_knights


def battle(knights: dict) -> dict:
    ready_knights = prepare_knights(knights)

    lancelot = ready_knights["lancelot"]
    arthur = ready_knights["arthur"]
    mordred = ready_knights["mordred"]
    red_knight = ready_knights["red_knight"]

    lancelot.hp -= max(0, mordred.power - lancelot.protection)
    mordred.hp -= max(0, lancelot.power - mordred.protection)

    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)

    arthur.hp -= max(0, red_knight.power - arthur.protection)
    red_knight.hp -= max(0, arthur.power - red_knight.protection)

    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
