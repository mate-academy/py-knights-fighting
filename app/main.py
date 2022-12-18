from app.knights.knight import Knight
from app.tournament.start_fight import Battle


def battle(knights: dict) -> dict:
    for_battle = {}
    for hero in knights:
        for_battle.update({hero: Knight(knights[hero])})
    return Battle(for_battle).start_fight()
