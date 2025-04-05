from app.knights import Knight
from app.battle import battle
from app.data.knights_data import KNIGHTS


def mai() -> None:
    knights = {name: Knight(**stats) for name, stats in KNIGHTS.items()}

    print(knights)
    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    final_results = {**result1, **result2}
    print("Battle Results:", final_results)


if __name__ == "__main__":
    mai()
