from app.knights import Knight
from app.battle import Battle
from app.knight_config import KNIGHTS


def battle(knight_a_key: str, knight_b_key: str) -> dict[str, int]:
    knight_a: Knight = Knight(KNIGHTS[knight_a_key])
    knight_b: Knight = Knight(KNIGHTS[knight_b_key])
    return Battle(knight_a, knight_b).fight()
