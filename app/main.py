from app.units.knight_config import KNIGHTS
from app.units.knights import Knight


knights = Knight.create_knights(KNIGHTS)
knights_with_staff =\
    (Knight.calculate_knights_with_staff(knights))
knights_battle = Knight.knights_battle(knights_with_staff)
print(knights_battle)
