from app.service.make_knight import make_knight


def make_knights(knights: dict) -> dict:
    new_knights = {}
    for knight_name in knights:
        new_knights[knight_name] = make_knight(knights[knight_name])
    return new_knights
