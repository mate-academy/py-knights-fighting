from app.config_knights import ConfigKnights
from app.preparation import Preparation
from app.battles import Battles


def battle(knights_config: dict) -> dict:
    preparation = Preparation()
    prepared_knights = preparation.prepare_all(knights_config)

    battles = Battles()
    return battles.run(prepared_knights)


class Main:

    @staticmethod
    def start() -> None:
        config = ConfigKnights()

        results = battle(config.knights)

        print(results)


if __name__ == "__main__":
    Main.start()
