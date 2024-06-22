from knight import Knight


def create_knights(config: dict) -> dict:
    knights = {}
    for name, data in config.items():
        knights[name] = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion"),
        )

    return knights

