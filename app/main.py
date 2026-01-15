from app.configuration.battle import knight_duel
from app.configuration.prepare_knight import knight_prepared
from app.models.knight import Knight
from app.utils.data import KNIGHTS


def battle(knights_config: dict) -> dict:

    knights = {
        name: Knight(**config)
        for name, config in knights_config.items()
    }

    for knight in knights.values():
        knight_prepared(knight)

    knight_duel(knights["lancelot"], knights["mordred"])
    knight_duel(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


def main() -> None:
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
