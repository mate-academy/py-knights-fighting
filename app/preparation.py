from app.knight import Knight


def create_knight(name: str, power: int, hp: int, armour:list, wearpon: list, potion: list | None = None):
    return Knight(name, power, hp, armour, wearpon, potion)

def prepare_to_battle(knights: list):

