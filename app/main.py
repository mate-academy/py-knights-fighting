from app.constants import KNIGHTS
from app.utils import battle


def main() -> None:
    result = battle(KNIGHTS)
    print(result)

