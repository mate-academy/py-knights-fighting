from app.knight import Knight


def health_point_check(knight: dict) -> None:
    if knight["hp"] < 0:
        knight["hp"] = 0


def battle(knights_config: dict) -> dict:

    hero_dict = {}
    for person in knights_config.values():
        hero = person
        knight = Knight(
            name=hero["name"],
            power=hero["power"],
            hp=hero["hp"]
        )
        knight.armour_defence(hero["armour"])
        knight.use_of_weapons(hero["weapon"])
        knight.apply_potion(hero["potion"])
        hero["hp"] = knight.hp
        hero["power"] = knight.power
        hero["protection"] = knight.protection
        new_dict = {hero["name"]: hero}
        hero_dict.update(new_dict)

    lancelot = hero_dict["Lancelot"]
    arthur = hero_dict["Artur"]
    mordred = hero_dict["Mordred"]
    red_knight = hero_dict["Red Knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    health_point_check(lancelot)

    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    health_point_check(mordred)

    # 2 Arthur vs Red Knight:
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
