from app.models.knight import Knight


def prepare_knight(knight_config: dict) -> any:
    return Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
        armour=knight_config["armour"],
        weapon=knight_config["weapon"],
        potion=knight_config["potion"]
    )


def battle(knights_config: dict) -> None:
    arthur = prepare_knight(knights_config["arthur"])
    lancelot = prepare_knight(knights_config["lancelot"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    lancelot.calculate_damage(mordred.power)
    mordred.calculate_damage(lancelot.power)

    arthur.calculate_damage(red_knight.power)
    red_knight.calculate_damage(arthur.power)

    if lancelot.hp < 0:
        lancelot.hp = 0
    if mordred.hp < 0:
        mordred.hp = 0
    if arthur.hp < 0:
        arthur.hp = 0
    if red_knight.hp < 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
