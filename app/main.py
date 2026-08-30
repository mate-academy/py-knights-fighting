from app.knight import Knight


def prepare_knight(data: dict) -> Knight:
    knight = Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=data.get("armour", []),
        weapon=data.get("weapon", {}),
        potion=data.get("potion"),
    )
    knight.power += knight.weapon["power"]
    knight.protection = sum(
        armour_piece["protection"]
        for armour_piece in knight.armour
    )
    if knight.potion is not None:
        effects = knight.potion["effect"]
        knight.power += effects.get("power", 0)
        knight.protection += effects.get("protection", 0)
        knight.hp += effects.get("hp", 0)
    return knight


def battle(knights_config: dict) -> dict[str, int]:
    prepared_knights = {}

    for knight_key, knight_data in knights_config.items():
        prepared_knights[knight_key] = prepare_knight(knight_data)

    # lancelot
    lancelot = prepared_knights["lancelot"]

    # arthur
    arthur = prepared_knights["arthur"]

    # mordred
    mordred = prepared_knights["mordred"]

    # red_knight
    red_knight = prepared_knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,

    }
