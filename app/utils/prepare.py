from app.knights.knight import Knight


def prepare_knight(data: dict) -> Knight:
    knight = Knight(**data)
    knight.prepare_for_battle()
    return knight
