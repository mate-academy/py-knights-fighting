from app.knight import Knight


def create_knight(knight_config: dict) -> Knight:
    knight = Knight(
        knight_config["name"],
        knight_config["power"],
        knight_config["hp"]
    )

    knight.apply_attributes(
        knight_config["armour"],
        knight_config["weapon"],
        knight_config["potion"]
    )

    return knight


def battle(knights_config: dict) -> dict:
    knight_instances = {
        knight["name"]: create_knight(knight)
        for knight in knights_config.values()
    }

    knight_instances["Lancelot"].attack(knight_instances["Mordred"])
    knight_instances["Arthur"].attack(knight_instances["Red Knight"])

    return {knight.name: knight.hp for knight in knight_instances.values()}
