from app import fight
from app.data import knights


def battle(knights: dict) -> dict:

    return fight.fight(knights)

if __name__ == "__main__":
    battle(knights)
