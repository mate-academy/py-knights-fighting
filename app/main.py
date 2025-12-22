from app.warriors import KNIGHTS
from app.warrior.knight import Knight
from app.arena.arena import Arena
from app.arena.arena_errors import MissingWarriorError


def battle(knights: dict) -> dict | None:
    knights = Knight.from_dict(knights)
    duels = (
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight")
    )
    arena = Arena(knights, duels)
    try:
        return arena.battle()
    except MissingWarriorError as e:
        print(e)


if __name__ == "__main__":
    print(battle(KNIGHTS))
