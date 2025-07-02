"""Application entry point exposing the battle function."""
from .battle import battle
from .data import KNIGHTS


if __name__ == "__main__":
    print(battle(KNIGHTS))
