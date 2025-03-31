from app.game.battle import battle
from config import KNIGHTS


def main() -> None:
    """
    Main entry point for the application. Simulates a battle between two knights
    and prints the results to the console.
    """
    lancelot = KNIGHTS["lancelot"]
    mordred = KNIGHTS["mordred"]

    result: dict[str, int] = battle(lancelot, mordred)
    for knight, hp in result.items():
        print(f"{knight} имеет {hp} HP после боя.")


if __name__ == "__main__":
    main()