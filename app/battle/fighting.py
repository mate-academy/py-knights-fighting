from app.support.support_functions import if_someone_fell
from app.support.support_functions import fight


def fighting(knight_1: str, knight_2: str, data: dict) -> None:
    fight(knight_1, knight_2, data, ["hp", "power", "protection"])

    # check if someone fell in battle
    for knight in (knight_1, knight_2):
        if_someone_fell(knight, data)
