from app.preparation.knight import Knight


def health_point_check(knight: dict) -> None:
    if knight["hp"] < 0:
        knight["hp"] = 0


def battle(knights_config: dict) -> dict:

    lancelot = knights_config["lancelot"]
    knight_lancelot = Knight(
        name=lancelot["name"],
        power=lancelot["power"],
        hp=lancelot["hp"]
    )
    knight_lancelot.apply_armour(lancelot["armour"])
    knight_lancelot.apply_weapon(lancelot["weapon"])
    knight_lancelot.apply_potion(lancelot["potion"])
    lancelot["hp"] = knight_lancelot.hp
    lancelot["power"] = knight_lancelot.power
    lancelot["protection"] = knight_lancelot.protection

    arthur = knights_config["arthur"]
    knight_arthur = Knight(
        name=arthur["name"],
        power=arthur["power"],
        hp=arthur["hp"]
    )
    knight_arthur.apply_armour(arthur["armour"])
    knight_arthur.apply_weapon(arthur["weapon"])
    knight_arthur.apply_potion(arthur["potion"])
    arthur["hp"] = knight_arthur.hp
    arthur["power"] = knight_arthur.power
    arthur["protection"] = knight_arthur.protection

    mordred = knights_config["mordred"]
    knight_mordred = Knight(
        name=mordred["name"],
        power=mordred["power"],
        hp=mordred["hp"]
    )
    knight_mordred.apply_armour(mordred["armour"])
    knight_mordred.apply_weapon(mordred["weapon"])
    knight_mordred.apply_potion(mordred["potion"])
    mordred["hp"] = knight_mordred.hp
    mordred["power"] = knight_mordred.power
    mordred["protection"] = knight_mordred.protection

    red_knight = knights_config["red_knight"]
    knight_red_knight = Knight(
        name=red_knight["name"],
        power=red_knight["power"],
        hp=red_knight["hp"]
    )
    knight_red_knight.apply_armour(red_knight["armour"])
    knight_red_knight.apply_weapon(red_knight["weapon"])
    knight_red_knight.apply_potion(red_knight["potion"])
    red_knight["hp"] = knight_red_knight.hp
    red_knight["power"] = knight_red_knight.power
    red_knight["protection"] = knight_red_knight.protection

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    health_point_check(lancelot)

    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    health_point_check(mordred)

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    health_point_check(arthur)

    red_knight["hp"] -= arthur["power"] - red_knight["protection"]
    health_point_check(red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
