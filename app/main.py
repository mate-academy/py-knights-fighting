from app.config.battle_config import BATTLE_CONFIG
from app.application.battle import battle


def main() -> None:
    result = battle(BATTLE_CONFIG)
    print(result)


if __name__ == "__main__":
    main()
