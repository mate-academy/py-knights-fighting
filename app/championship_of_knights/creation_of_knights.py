from app.championship_of_knights.knight import Knight


def creation_of_knights(knights_data: dict) -> dict:
    knights = {}
    for key, data in knights_data.items():
        knight = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion")
        )
        knight.battle_preparations()
        knights[key] = knight
    return knights
