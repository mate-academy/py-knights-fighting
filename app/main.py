from app.knights_config import KNIGHTS
from app.fighting import battle

if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
