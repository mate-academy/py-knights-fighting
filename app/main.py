from app.utils.constants import KNIGHTS
from app.knights.knight_config import Knight


if __name__ == "__main__":
    knights_battle = Knight(KNIGHTS)
    battle_ = knights_battle.battle()
    print(battle_)
