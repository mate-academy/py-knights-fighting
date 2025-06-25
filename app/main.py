from app.characters.knights_config import KNIGHTS
from app.characters.knight import Knight
from app.tournament.tournament import Tournament


def battle(knights_config: dict) -> dict:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    tournament = Tournament(
        [
            (lancelot, mordred),
            (arthur, red_knight)
        ]
    )

    return tournament.battle()


if __name__ == "__main__":
    print(battle(KNIGHTS))
