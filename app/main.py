from app.knights_constant import KNIGHTS
from app.knights import Knight
from app.battle import Battle


def battle(config: dict) -> dict:
    knights = {}

    for knight in config.keys():
        knights[knight] = Knight.create_knight(config, knight)

    first_battle = Battle(knights.get("lancelot"), knights.get("mordred"))
    second_battle = Battle(knights.get("arthur"), knights.get("red_knight"))
    Battle.before_start()
    first_battle.start_battle()
    second_battle.start_battle()

    return Battle.battles_result()


if __name__ == "__main__":
    battle(KNIGHTS)
