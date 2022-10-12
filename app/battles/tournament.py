from .fight_simulation import brawl
from app.heroes.fighter import Hero


def make_tournament_list(config: dict) -> list:
    lancelot = Hero(config["lancelot"])
    lancelot.apply_quip()

    mordred = Hero(config["mordred"])
    mordred.apply_quip()

    arthur = Hero(config["arthur"])
    arthur.apply_quip()

    red_knight = Hero(config["red_knight"])
    red_knight.apply_quip()

    brawl(lancelot, mordred)
    brawl(arthur, red_knight)

    return [lancelot, mordred, arthur, red_knight]
