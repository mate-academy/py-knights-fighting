from app.knights.knight import Knight


def battle(knights_config: str) -> None:
    """Simulate battles between knights and return their final HP."""
    # Create knights
    knights = {
        name: Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data.get("armour", []),
            weapon=data["weapon"],
            potion=data.get("potion"),
        )
        for name, data in knights_config.items()
    }

    # Prepare all knights
    for knight in knights.values():
        knight.prepare_for_battle()

    # Battle 1: Lancelot vs. Mordred
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # Battle 2: Arthur vs. Red Knight
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    # Return battle results
    return {knight.name: knight.hp for knight in knights.values()}
