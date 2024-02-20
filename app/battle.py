from knight import Knight


def create_knight(config: dict) -> Knight:
    return Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"],
        armour=config.get("armour", []),
        weapon=config["weapon"],
        potion=config.get("potion")
    )


def battle(knightsconfig: dict) -> dict:
    knights = {
        name: create_knight(info) for name, info in knightsconfig.items()
    }

    # Lancelot vs Mordred
    knights["lancelot"].receive_damage(knights["mordred"].power)
    knights["mordred"].receive_damage(knights["lancelot"].power)

    # Arthur vs Red Knight
    knights["arthur"].receive_damage(knights["red_knight"].power)
    knights["red_knight"].receive_damage(knights["arthur"].power)
    return {knight.name: knight.hp for knight in knights.values()}
