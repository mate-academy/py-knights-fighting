from app.people.king import King
from app.kingdom.kingdom import Kingdom
from app.people.armed_people import KNIGHTS


def battle(knights_config: dict) -> dict:
    king_axel = King("Axel", 100)
    kingdom_of_axel = Kingdom(king_axel.name, king_axel.gold, knights_config)
    kingdom_of_axel.create_knights()
    contest = kingdom_of_axel.create_contest()
    contest.prepare_for_battle()
    contest.battle(contest.knights["lancelot"], contest.knights["mordred"])
    contest.battle(contest.knights["arthur"], contest.knights["red_knight"])
    return contest.get_battle_results()


print(battle(KNIGHTS))
