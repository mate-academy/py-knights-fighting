from models import Knight, Item


def create_knights(config: dict) -> Knight:
    knights = []
    for key, data in config.items():
        knights.append(Knight(
            name=data["name"],
            base_power=data["power"],
            base_hp=data["hp"],
            armour=data["armour"],
            weapon=Item(**data["weapon"]),
            potion=data["potion"]
        ))
    return knights


def battle(knight1: dict, knight2: dict) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)
    return knight1, knight2
