from app.knights.apply_armour import Armour
from app.tournament.start_fight import Battle


def battle(knights: dict) -> dict:
    for_battle = {}
    for hero in knights:
        for_battle.update(Armour({hero: knights[hero]}).apply_armour())

    return Battle(for_battle).start_fight()
