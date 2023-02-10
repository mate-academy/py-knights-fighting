from typing import Dict

from app.warriors import Knight
from app.data import KNIGHTS


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    knights = {}

    for warrior, config in knights_config.items():
        knight = Knight(name=config["name"],
                        power=config["power"],
                        hp=config["hp"],
                        weapon=config["weapon"],
                        armour=config["armour"],
                        potion=config["potion"])
        knights[warrior] = knight

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {data.name: data.hp for data in knights.values()}


print(battle(KNIGHTS))
