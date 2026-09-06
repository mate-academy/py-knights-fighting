from app.preparation import prepare_knight


def fight(attacker: dict, defender: dict) -> dict:
    damage = attacker["power"] - defender["protection"]
    defender["hp"] -= damage

    if defender["hp"] <= 0:
        defender["hp"] = 0


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        prepare_knight(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]

    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    fight(lancelot, mordred)
    fight(mordred, lancelot)

    fight(arthur, red_knight)
    fight(red_knight, arthur)

    return {
        knight["name"]: knight["hp"]
        for knight in knights_config.values()
    }
