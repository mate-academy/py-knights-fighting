from app.Preparations.knights import knights
from app.Preparations.config_human import Knight
from app.Battle.fight import Fight


def battle(knight: dict) -> dict:

    human_instance = Knight(knight)

    dict_knights = human_instance.change_config()

    lancelot = dict_knights.get("lancelot")
    arthur = dict_knights.get("arthur")
    mordred = dict_knights.get("mordred")
    red_knight = dict_knights.get("red_knight")

    lancelot_vs_artur = Fight(lancelot, mordred)
    mordred_vs_red_knight = Fight(arthur, red_knight)

    fight1 = lancelot_vs_artur.battle()
    fight2 = mordred_vs_red_knight.battle()

    return {**fight1, **fight2}


if __name__ == "__main__":
    print(battle(knights))
