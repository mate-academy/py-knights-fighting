from app.game.battle import battle
from app.game.config import KNIGHTS

if __name__ == "__main__":
    results = {
        "Lancelot vs Mordred": battle(KNIGHTS["lancelot"]),
        "Arthur vs Red Knight": battle(KNIGHTS["arthur"]),
    }

    for fight, result in results.items():
        print(f"{fight}: {result}")
