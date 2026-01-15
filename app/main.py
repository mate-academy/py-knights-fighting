from copy import deepcopy
from .data import KNIGHTS
from .logic import battle


if __name__ == "__main__":
    result = battle(deepcopy(KNIGHTS))
    for knight, hp in result.items():
        print(f"{knight}: {hp} hp")
