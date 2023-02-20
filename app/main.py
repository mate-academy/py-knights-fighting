from app.data import KNIGHTS
from app.battle_implement.implementation import create_knight
from app.battle_implement.battle_process import battle_process, battles_result


def battle(knights_dict: dict) -> dict:
    knights = {
        knight.get("name"): create_knight(knight)
        for knight
        in knights_dict.values()
    }

    lancelot = knights.get("Lancelot")
    artur = knights.get("Artur")
    mordred = knights.get("Mordred")
    red_knight = knights.get("Red Knight")

    battle_process(lancelot, mordred)
    battle_process(artur, red_knight)

    return battles_result(knights)


if __name__ == "__main__":
    print(battle(KNIGHTS))
