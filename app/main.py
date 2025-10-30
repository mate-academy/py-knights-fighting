from app.barracks.knights import KNIGHTS
from app.arena.duel import battle


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
