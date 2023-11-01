from app.knights.knight import Knight


def battle_preparation(knights_config: dict) -> dict:
    knights = {}
    for name, config in knights_config.items():
        knight = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config.get("potion"),
        )
        knight.add_armour()
        knight.add_weapon()
        knight.add_potion()
        knights[name] = knight
    return knights
