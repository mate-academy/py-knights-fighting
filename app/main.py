from app.game.battle import battle
from config import KNIGHTS


def main():
    lancelot = KNIGHTS["lancelot"]
    mordred = KNIGHTS["mordred"]

    result = battle(lancelot, mordred)
    for knight, hp in result.items():
        print(f"{knight} имеет {hp} HP после боя.")


if __name__ == "__main__":
    main()