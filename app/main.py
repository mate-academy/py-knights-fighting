from utils import create_knights, battle
from config import KNIGHTS


def main() -> None:
    knights = create_knights(KNIGHTS)

    lancelot, mordred = battle(knights[0], knights[2])
    arthur, red_knight = battle(knights[1], knights[3])

    for knight in [lancelot, arthur, mordred, red_knight]:
        print(f"{knight.name}: {knight.hp} HP")


if __name__ == "__main__":
    main()
