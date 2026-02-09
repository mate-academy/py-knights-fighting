from app.game.battle import battle
from app.game.config import KNIGHTS

if __name__ == "__main__":
    results = battle(KNIGHTS)

    for knight, hp in results.items():
        print(f"{knight}: {hp}")
