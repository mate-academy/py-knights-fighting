from app.fight import Fight
from app.knight import Knight


def create_knights(knights_config: dict) -> list:
    knights = []
    for knight_config in knights_config.values():
        knights.append(Knight(name=knight_config["name"],
                              power=knight_config["power"],
                              hp=knight_config["hp"],
                              armour=knight_config["armour"],
                              weapon=knight_config["weapon"],
                              potion=knight_config["potion"]))
    return knights


def battle(knights_config: dict) -> dict:
    knights = create_knights(knights_config)
    Fight(knights[0], knights[2])
    Fight(knights[1], knights[3])
    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp,
    }
