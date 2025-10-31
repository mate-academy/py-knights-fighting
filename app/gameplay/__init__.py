from app.gameplay.game_logic import Logic
from app.gameplay.knight import Knight

if __name__ == "__main__":
    Logic.prepare_to_battle(Knight("", 1, 1, None, None, None))
