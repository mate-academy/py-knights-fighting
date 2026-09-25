"""Entry point of the knights fighting simulation."""

from app.battle import battle
from app.knights_data import KNIGHTS

if __name__ == "__main__":
    print(battle(KNIGHTS))
