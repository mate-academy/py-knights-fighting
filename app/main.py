from app.units.knight_config import KNIGHTS
from app.units.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = Knight.create_knights(knights_config)
    knights_with_staff =\
        (Knight.calculate_knights_with_staff(knights))
    knights_battle = Knight.knights_battle(knights_with_staff)
    return knights_battle


print(battle(KNIGHTS))
