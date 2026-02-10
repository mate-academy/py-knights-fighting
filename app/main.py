from app.knights.knight_info import KNIGHTS
from app.fights.battle_prep import prepare_knights
from app.fights.battle import battle as _impl_battle


def battle(*args, **kwargs) -> dict:
    return _impl_battle(*args, **kwargs)


def main() -> None:
    knights = prepare_knights(KNIGHTS)
    results = battle(knights)

    if __name__ == "__main__":
        print(results)


if __name__ == "__main__":
    main()
