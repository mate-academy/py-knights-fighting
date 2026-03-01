from app.knight import Knight


def prepare_knights(knights_config: dict) -> dict:
    result = {}
    for key, config in knights_config.items():
        knight = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )
        knight.prepare_for_battle()
        result[knight.name] = knight
    return result


def fight(knight1: dict, knight2: dict) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights_config: dict) -> dict:
    knights = prepare_knights(knights_config)
    fight(knights["Lancelot"], knights["Mordred"])
    fight(knights["Arthur"], knights["Red Knight"])
    result = {}
    for value in knights.values():
        result[value.name] = value.hp
    return result
