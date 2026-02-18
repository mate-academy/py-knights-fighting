from app.config import KNIGHTS
from app.battle import battle

if __name__ == "__main__":
    results = battle(KNIGHTS)
    print("Battle results:")
    for name, hp in results.items():
        print(f"{name}: {hp} HP")
