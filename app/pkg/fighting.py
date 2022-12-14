# from app.pkg.knight_config import KNIGHTS


def check_hp_knight(hp: int) -> int:
    if hp <= 0:
        hp = 0
    return hp


def fighting(first_knight: str, second_knight: str, knights: dict) -> None:

    knights[first_knight]["hp"] -= knights[second_knight]["power"] \
        - knights[first_knight]["protection"]
    knights[second_knight]["hp"] -= knights[first_knight]["power"] \
        - knights[second_knight]["protection"]

    knights[first_knight]["hp"] = check_hp_knight(knights[first_knight]["hp"])
    knights[second_knight]["hp"] = check_hp_knight(knights[second_knight]["hp"])
