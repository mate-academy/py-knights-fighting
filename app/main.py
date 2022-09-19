from app.heroes.config import KNIGHTS
from app.battles.tournament import make_tournament_list


def battle(fighter_config: dict) -> dict:
    fighters = make_tournament_list(fighter_config)

    return {hero.name: hero.hp for hero in fighters}
