from app.models import Knight


def create_knight(data: dict) -> Knight:
    return Knight(
        name=data["name"],
        hp=data["hp"],
        power=data["power"],
        armour=data["armour"],
        weapon=data["weapon"],
        potion=data["potion"],
    )


def battle(knights_config: dict) -> dict:
    """Create Knights: """
    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    """Preparation Knights: """
    for person in [lancelot, arthur, mordred, red_knight]:
        person.prepare()

    """Battle first: """
    lancelot.damage(mordred.power)
    mordred.damage(lancelot.power)

    """Battle second: """
    arthur.damage(red_knight.power)
    red_knight.damage(arthur.power)

    """Result battle: """
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
