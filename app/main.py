from app.knights_constant import KNIGHTS
from app.knights import Knights
from app.battle import Battle


def battle(config: dict) -> dict:
    lancelot = Knights.create_knight(config, "lancelot")
    mordred = Knights.create_knight(config, "mordred")
    arthur = Knights.create_knight(config, "arthur")
    red_knight = Knights.create_knight(config, "red_knight")
    first_battle = Battle(lancelot, mordred)
    second_battle = Battle(arthur, red_knight)
    Battle.before_start()
    first_battle.start_battle()
    second_battle.start_battle()

    return Battle.battles_result()


if __name__ == "__main__":
    battle(KNIGHTS)
