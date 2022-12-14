def check_hp_knight(hp: int) -> int:
    if hp <= 0:
        hp = 0
    return hp


def fighting(first: str, second: str, knights: dict) -> None:

    knights[first]["hp"] -= knights[second]["power"] \
        - knights[first]["protection"]
    knights[second]["hp"] -= knights[first]["power"] \
        - knights[second]["protection"]

    knights[first]["hp"] = check_hp_knight(knights[first]["hp"])
    knights[second]["hp"] = check_hp_knight(knights[second]["hp"])
