from app.configs import KNIGHTS
from battle import battle

if __name__ == "__main__":
    result = battle(KNIGHTS)
    print("Battle results:")
    for knight, hp in result.items():
        print(f"{knight}: {hp} HP")
