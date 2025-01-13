from app.knights.knight import Knight
from app.knights.data import knights_attr
from app.contest.contest import Contest


def battle(knights_attr) -> None:
    knights = Knight.create_knights_from_data(knights_attr)
    new_contest = Contest(knights)
    new_contest.make_all_contest_preparations()
    new_contest.make_battle("lancelot", "mordred")
    new_contest.make_battle("arthur", "red_knight")
    print(new_contest.battle_results)


