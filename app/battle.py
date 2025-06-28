from typing import Dict
import copy
from .knight import Knight


def create_knight_from_config(config: Dict) -> Knight:
    return Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"],
        armour=config["armour"],
        weapon=config["weapon"],
        potion=config["potion"]
    )


def conduct_duel(knight1: Knight, knight2: Knight) -> tuple[Knight, Knight]:
    damage1 = knight1.power
    damage2 = knight2.power

    knight1.take_damage(damage2)
    knight2.take_damage(damage1)
    return knight1, knight2


def battle(knights_config: Dict) -> Dict[str, int]:
    config_copy = copy.deepcopy(knights_config)

    knights = {
        key: create_knight_from_config(config)
        for key, config in config_copy.items()
    }

    conduct_duel(knights["lancelot"], knights["mordred"])
    conduct_duel(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


def display_battle_results(results: Dict[str, int]) -> None:
    for name, hp in results.items():
        print(f"{name}: {hp} HP")
