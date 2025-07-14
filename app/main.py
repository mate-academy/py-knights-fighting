from app.knights import Knight
from app.battle import Battle
from app.knight_config import KNIGHTS  # wherever your data lives


def battle(knight_a_key, knight_b_key):
    knight_a = Knight(KNIGHTS[knight_a_key])
    knight_b = Knight(KNIGHTS[knight_b_key])

    return Battle(knight_a, knight_b).fight()
