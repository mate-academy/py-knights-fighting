from app.knight import Knight


def create_battle_list(knights: dict) -> list:
    return [Knight(knights[knight]) for knight in knights.keys()]
