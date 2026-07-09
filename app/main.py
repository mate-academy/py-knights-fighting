from app.models import Armour, Knights, Potion, Weapon


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, config in knights_config.items():
        potion = None
        if config["potion"]:
            potion = Potion(
                name=config["potion"]["name"],
                effect=config["potion"]["effect"]
            )
        knights[key] = Knights(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=[Armour(a["part"], a["protection"])
                    for a in config["armour"]],
            weapon=Weapon(config["weapon"]["name"], config["weapon"]["power"]),
            potion=potion
        )

    for knight in knights.values():
        knight.protection = sum(a.protection for a in knight.armour)
        knight.power += knight.weapon.power

        if knight.potion:
            for stat, value in knight.potion.effect.items():
                setattr(knight, stat, getattr(knight, stat, 0) + value)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    lancelot.hp = max(lancelot.hp, 0)
    mordred.hp = max(mordred.hp, 0)

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection
    arthur.hp = max(arthur.hp, 0)
    red_knight.hp = max(red_knight.hp, 0)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
