from app.config.battle_config import BATTLE_CONFIG
from app.application.battle import battle


def main() -> None:
    battle(BATTLE_CONFIG)


if __name__ == "__main__":
    main()
