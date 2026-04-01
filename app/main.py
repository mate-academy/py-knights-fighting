from app.knights.knight import Knight
from app.contest.contest import Contest


def battle(knights_attr: dict) -> None:
    knights = Knight.create_knights_from_data(knights_attr)
    new_contest = Contest(knights)
    new_contest.make_all_contest_preparations()
    new_contest.make_battle("Lancelot", "Mordred")
    new_contest.make_battle("Arthur", "Red Knight")
    return new_contest.battle_results
