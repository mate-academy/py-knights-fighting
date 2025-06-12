from app.services.battle import battle
from app.config import KNIGHTS

def main():
    result = battle(KNIGHTS)
    print(result)

if __name__ == "__main__":
    main()
